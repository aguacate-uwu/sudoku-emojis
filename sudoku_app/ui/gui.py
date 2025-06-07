import tkinter as tk
from ui.emoji_selector import EmojiSelector
from core.board import SudokuBoard

class SudokuGUI(tk.Frame):
    def __init__(self, parent, emojis, max_selection=9):
        super().__init__(parent)
        self.parent = parent
        self.emojis = emojis
        self.max_selection = max_selection
        self.selected_emojis = []
        self.active_emoji = None

        self.pack(fill="both", expand=True)
        self.configure(padx=20, pady=20)

        # Obtener el activebackground por defecto de un botón
        self.default_active_bg = tk.Button(self).cget("activebackground")

        self.create_widgets()

    def create_widgets(self):
        # Selector de emojis iniciales
        self.selector = EmojiSelector(self, self.emojis, max_selection=self.max_selection, on_confirm=self.on_emojis_confirmed)
        self.selector.pack()

        # Frame para emojis activos (después de confirmación)
        self.active_frame = tk.Frame(self)
        # (Se empacará más adelante cuando se confirme selección)

        # Frame para el tablero, aquí irá SudokuBoard
        self.board_frame = tk.Frame(self)
        # (Se empacará más adelante)

        self.active_buttons = []
        self.board = None  # Aquí guardamos la instancia de SudokuBoard

    def on_emojis_confirmed(self, selected_emojis):
        self.selected_emojis = selected_emojis
        self.selector.pack_forget()  # Ocultamos el selector

        self.create_active_emoji_selector()
        self.create_board()

    def create_active_emoji_selector(self):
        self.active_frame.pack(pady=(10, 20))
        for btn in self.active_buttons:
            btn.destroy()
        self.active_buttons.clear()

        for em in self.selected_emojis:
            btn = tk.Button(self.active_frame, text=em, font=("Arial", 24), width=3)
            btn.pack(side="left", padx=8)
            btn.bind("<Enter>", lambda e, b=btn, em=em: self.on_enter(b, em, seleccionando=False))
            btn.bind("<Leave>", lambda e, b=btn, em=em: self.on_leave(b, em, seleccionando=False))
            btn.config(command=lambda e=em: self.set_active_emoji(e))
            self.active_buttons.append(btn)

        self.set_active_emoji(self.selected_emojis[0])  # Emoji activo por defecto

    def create_board(self):
        self.board_frame.pack()
        # Crear el tablero usando SudokuBoard, pasamos el callback on_cell_click
        self.board = SudokuBoard(self.board_frame, self.on_cell_click)
        self.board.pack()

    def set_active_emoji(self, emoji):
        self.active_emoji = emoji
        for btn in self.active_buttons:
            if btn["text"] == emoji:
                btn.config(bg="lightblue", activebackground="lightblue")
            else:
                btn.config(bg=self.cget("bg"), activebackground=self.default_active_bg)

    def on_cell_click(self, row, col):
        if self.active_emoji and self.board:
            self.board.set_cell(row, col, self.active_emoji)

    def on_enter(self, btn, emoji, seleccionando=False):
        if seleccionando:
            if emoji in self.selected_emojis:
                btn.config(bg="lightblue", activebackground="lightblue")
            else:
                btn.config(bg="lightgray", activebackground="lightgray")
        else:
            if emoji == self.active_emoji:
                btn.config(bg="lightblue", activebackground="lightblue")
            else:
                btn.config(bg="lightgray", activebackground="lightgray")

    def on_leave(self, btn, emoji, seleccionando=False):
        if seleccionando:
            if emoji in self.selected_emojis:
                btn.config(bg="lightblue", activebackground="lightblue")
            else:
                btn.config(bg=self.cget("bg"), activebackground=self.default_active_bg)
        else:
            if emoji == self.active_emoji:
                btn.config(bg="lightblue", activebackground="lightblue")
            else:
                btn.config(bg=self.cget("bg"), activebackground=self.default_active_bg)