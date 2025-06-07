import tkinter as tk

class EmojiSelector(tk.Frame):
    def __init__(self, parent, emojis, max_selection=9, on_confirm=None):
        super().__init__(parent)
        self.emojis = emojis
        self.max_selection = max_selection
        self.selected_emojis = []
        self.on_confirm = on_confirm
        self.default_bg = self.cget("bg")
        self.default_active_bg = tk.Button(self).cget("activebackground")

        self.label = tk.Label(self, text=f"Emojis seleccionados: 0/{self.max_selection}", font=("Arial", 14))
        self.label.pack(pady=(5, 10))

        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack(pady=(10, 20))

        self.emoji_buttons = []
        cols = 9
        for i, emoji in enumerate(self.emojis):
            btn = tk.Button(self.grid_frame, text=emoji, font=("Arial", 24), width=3)
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
                btn.config(bg="lightblue", activebackground="lightblue")
            else:
                btn.config(bg=self.default_bg, activebackground=self.default_active_bg)
        self.label.config(text=f"Emojis seleccionados: {len(self.selected_emojis)}/{self.max_selection}")

    def on_enter(self, btn, emoji, seleccionando=False):
        if seleccionando:
            if emoji in self.selected_emojis:
                btn.config(bg="lightblue", activebackground="lightblue")
            else:
                btn.config(bg="lightgray", activebackground="lightgray")
        else:
            # En EmojiSelector siempre seleccionando=True, pero por si acaso:
            if emoji in self.selected_emojis:
                btn.config(bg="lightblue", activebackground="lightblue")
            else:
                btn.config(bg="lightgray", activebackground="lightgray")

    def on_leave(self, btn, emoji, seleccionando=False):
        if seleccionando:
            if emoji in self.selected_emojis:
                btn.config(bg="lightblue", activebackground="lightblue")
            else:
                btn.config(bg=self.default_bg, activebackground=self.default_active_bg)
        else:
            if emoji in self.selected_emojis:
                btn.config(bg="lightblue", activebackground="lightblue")
            else:
                btn.config(bg=self.default_bg, activebackground=self.default_active_bg)

    def confirm_selection(self):
        if len(self.selected_emojis) == self.max_selection:
            if self.on_confirm:
                self.on_confirm(self.selected_emojis)
            self.pack_forget()
        else:
            print(f"Selecciona exactamente {self.max_selection} emojis para continuar.")