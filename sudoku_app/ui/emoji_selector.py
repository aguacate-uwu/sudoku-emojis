import tkinter as tk
from ui.theme import BACKGROUND_COLOR, PRIMARY_COLOR, SECONDARY_COLOR, TEXT_COLOR

class EmojiSelector(tk.Frame):
    def __init__(self, parent, emojis, max_selection=9, on_confirm=None):
        super().__init__(parent)
        self.configure(bg=BACKGROUND_COLOR)

        self.emojis = emojis
        self.max_selection = max_selection
        self.selected_emojis = []
        self.on_confirm = on_confirm

        self.label = tk.Label(self, text=f"Emojis seleccionados: 0/{self.max_selection}", font=("Arial", 14), bg=BACKGROUND_COLOR)
        self.label.pack(pady=(5, 10))

        self.grid_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        self.grid_frame.pack(pady=(10, 20), expand=True, fill="both", anchor="center")

        self.emoji_buttons = []
        cols = 9
        for i, emoji in enumerate(self.emojis):
            btn = tk.Button(self.grid_frame, text=emoji, font=("Arial", 24), width=3, bg=SECONDARY_COLOR)
            btn.grid(row=i // cols, column=i % cols, padx=5, pady=5)
            btn.bind("<Enter>", lambda e, b=btn, em=emoji: self.on_enter(b, em, seleccionando=True))
            btn.bind("<Leave>", lambda e, b=btn, em=emoji: self.on_leave(b, em, seleccionando=True))
            btn.config(command=lambda em=emoji: self.toggle_selection(em))
            self.emoji_buttons.append(btn)

        self.confirm_btn = tk.Button(self, text="Confirmar selección", command=self.confirm_selection)
        self.confirm_btn.pack()

    def toggle_selection(self, emoji):
        if emoji in self.selected_emojis:
            self.selected_emojis.remove(emoji)
        elif len(self.selected_emojis) < self.max_selection:
            self.selected_emojis.append(emoji)
        self.update_ui()

    def update_ui(self):
        for btn in self.emoji_buttons:
            em = btn["text"]
            if em in self.selected_emojis:
                btn.config(bg=PRIMARY_COLOR, activebackground=PRIMARY_COLOR)
            else:
                btn.config(bg=SECONDARY_COLOR, activebackground=SECONDARY_COLOR)
        self.label.config(text=f"Emojis seleccionados: {len(self.selected_emojis)}/{self.max_selection}")

    def on_enter(self, btn, emoji, seleccionando=False):
        if seleccionando:
            if emoji in self.selected_emojis:
                btn.config(bg=PRIMARY_COLOR, activebackground=PRIMARY_COLOR)
            else:
                btn.config(bg=PRIMARY_COLOR, activebackground=PRIMARY_COLOR)
        else:
            # En EmojiSelector siempre seleccionando=True, pero por si acaso:
            if emoji in self.selected_emojis:
                btn.config(bg=PRIMARY_COLOR, activebackground=PRIMARY_COLOR)
            else:
                btn.config(bg=PRIMARY_COLOR, activebackground=PRIMARY_COLOR)

    def on_leave(self, btn, emoji, seleccionando=False):
        if seleccionando:
            if emoji in self.selected_emojis:
                btn.config(bg=PRIMARY_COLOR, activebackground=PRIMARY_COLOR)
            else:
                btn.config(bg=SECONDARY_COLOR, activebackground=SECONDARY_COLOR)
        else:
            if emoji in self.selected_emojis:
                btn.config(bg=PRIMARY_COLOR, activebackground=PRIMARY_COLOR)
            else:
                btn.config(bg=SECONDARY_COLOR, activebackground=SECONDARY_COLOR)

    def confirm_selection(self):
        if len(self.selected_emojis) == self.max_selection:
            if self.on_confirm:
                self.on_confirm(self.selected_emojis)
            self.pack_forget()
        else:
            print(f"Selecciona exactamente {self.max_selection} emojis para continuar.")