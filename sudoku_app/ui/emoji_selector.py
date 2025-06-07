import tkinter as tk

class EmojiSelector(tk.Frame):
    def __init__(self, parent, emojis, max_selection=9, on_confirm=None):
        super().__init__(parent)
        self.emojis = emojis
        self.max_selection = max_selection
        self.selected_emojis = set()
        self.default_bg = self.cget("bg")

        temp_btn = tk.Button(self)
        self.default_active_bg = temp_btn.cget("activebackground")
        temp_btn.destroy()

        self.on_confirm = on_confirm

        self.label_seleccion = tk.Label(self, text=f"Emojis seleccionados: 0/{self.max_selection}", font=("Arial", 14))
        self.label_seleccion.pack(pady=5)

        self.emojis_frame = tk.Frame(self)
        self.emojis_frame.pack(pady=10, fill="x")

        self.emojis_buttons = []
        cols = 9
        for i, em in enumerate(self.emojis):
            btn = tk.Button(self.emojis_frame, text=em, font=("Arial", 24),
                            width=3, bg=self.default_bg, activebackground=self.default_active_bg)
            btn.grid(row=i // cols, column=i % cols, padx=5, pady=5)
            btn.bind("<Enter>", lambda e, b=btn, em=em: self.on_enter(b, em))
            btn.bind("<Leave>", lambda e, b=btn, em=em: self.on_leave(b, em))
            btn.config(command=lambda e=em, b=btn: self.on_emoji_click(e, b))
            self.emojis_buttons.append(btn)

        self.confirm_btn = tk.Button(self, text="Confirmar selección", command=self.confirm_selection)
        self.confirm_btn.pack(pady=10)

    def on_emoji_click(self, emoji, btn):
        if emoji in self.selected_emojis:
            self.selected_emojis.remove(emoji)
            btn.config(bg=self.default_bg, activebackground=self.default_active_bg)
        else:
            if len(self.selected_emojis) < self.max_selection:
                self.selected_emojis.add(emoji)
                btn.config(bg="lightblue", activebackground="lightblue")
            else:
                print("Ya seleccionaste 9 emojis.")
        self.label_seleccion.config(text=f"Emojis seleccionados: {len(self.selected_emojis)}/{self.max_selection}")

    def on_enter(self, btn, emoji):
        if emoji not in self.selected_emojis:
            btn.config(bg="lightgray")

    def on_leave(self, btn, emoji):
        if emoji in self.selected_emojis:
            btn.config(bg="lightblue", activebackground="lightblue")
        else:
            btn.config(bg=self.default_bg, activebackground=self.default_active_bg)

    def confirm_selection(self):
        if len(self.selected_emojis) == self.max_selection:
            if self.on_confirm:
                self.on_confirm(list(self.selected_emojis))
        else:
            print(f"Selecciona exactamente {self.max_selection} emojis para continuar.")