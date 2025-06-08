import tkinter as tk
from ui.emoji_selector import EmojiSelector
from core.board import SudokuBoard
from core import solver
from core import generator
import copy

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

        self.default_active_bg = tk.Button(self).cget("activebackground")

        self.create_widgets()

    def create_widgets(self):
        self.selector = EmojiSelector(self, self.emojis, max_selection=self.max_selection, on_confirm=self.on_emojis_confirmed)
        self.selector.pack()

        self.active_frame = tk.Frame(self)
        self.board_frame = tk.Frame(self)

        self.result_label = tk.Label(self, text="", font=("Arial", 14), fg="blue")
        self.comprobar_button = tk.Button(self, text="Comprobar", command=self.comprobar_tablero)

        self.active_buttons = []
        self.board = None

        self.boton_generar = None

    def on_emojis_confirmed(self, selected_emojis):
        self.selected_emojis = selected_emojis
        self.selector.pack_forget()

        # Crear botón para generar Sudoku
        self.boton_generar = tk.Button(self, text="Generar Sudoku", font=("Arial", 14), command=self.generar_sudoku)  # NUEVO
        self.boton_generar.pack(pady=10)

    def generar_sudoku(self):
        tablero, solucion = generator.generar_sudoku(self.selected_emojis, dificultad="media")
        self.tablero_inicial = tablero
        self.solucion = solucion

        # Ocultar botón de generación
        if self.boton_generar:
            self.boton_generar.pack_forget()

        self.create_active_emoji_selector()
        self.create_board()

        # Rellenar las celdas con los emojis del tablero inicial
        for fila in range(9):
            for col in range(9):
                emoji = tablero[fila][col]
                if emoji:
                    self.board.set_initial_cell(fila, col, emoji)

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

        self.set_active_emoji(self.selected_emojis[0])

    def create_board(self):
        self.board_frame.pack()
        self.board = SudokuBoard(self.board_frame, self.on_cell_click)
        self.board.pack()

        # Mostrar botón de comprobar y etiqueta de resultado
        self.comprobar_button.pack(pady=10)
        self.result_label.pack()

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

    def comprobar_tablero(self):
        tablero_actual = self.board.get_board()
        tablero_copia = copy.deepcopy(tablero_actual)

        # Verificar si está completo
        if any("" in fila for fila in tablero_actual):
            self.result_label.config(text="Tablero incompleto ❗", fg="orange")
            return

        # Verificar si hay errores antes de intentar resolver
        if not solver.es_tablero_valido(tablero_actual):
            self.result_label.config(text="Hay errores ❌", fg="red")
            return

        # Intentar resolver con backtracking
        if solver.resolver(tablero_copia, self.selected_emojis):
            self.result_label.config(text="¡Correcto! ✅", fg="green")
        else:
            self.result_label.config(text="Hay errores ❌", fg="red")

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