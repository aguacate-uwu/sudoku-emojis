import tkinter as tk
from ui.emoji_selector import EmojiSelector

def main():
    root = tk.Tk()
    root.title("Sudoku con Emojis - Prototipo")
    root.geometry("830x700")

    emojis = ["🍎", "🍌", "🥑", "🍇", "🍓", "🍍", "🥝", "🍉", "🍒",
              "🍑", "🍈", "🍋", "🍊", "🥭", "🍏", "🍐", "🥥", "🥕", "🌽"]

    # Frame para emojis seleccionados + cuadrícula (se crea cuando confirme selección)
    game_frame = tk.Frame(root)

    def empezar_sudoku(seleccionados):
        selector.pack_forget()
        game_frame.pack(fill="both", expand=True)

        # Mostrar emojis seleccionados en fila
        frame_emojis = tk.Frame(game_frame)
        frame_emojis.pack(pady=20)
        for e in seleccionados:
            lbl = tk.Label(frame_emojis, text=e, font=("Arial", 32))
            lbl.pack(side="left", padx=10)

        # Crear cuadrícula 9x9
        grid_frame = tk.Frame(game_frame)
        grid_frame.pack(pady=20)
        grid_frame.config(bg="lightgray")

        buttons = []
        for fila in range(9):
            fila_botones = []
            for columna in range(9):
                btn = tk.Button(grid_frame, text="", width=4, height=2, font=("Arial", 14),
                                relief="ridge", borderwidth=1)
                btn.grid(row=fila, column=columna, padx=1, pady=1)
                fila_botones.append(btn)
            buttons.append(fila_botones)

    selector = EmojiSelector(root, emojis, max_selection=9, on_confirm=empezar_sudoku)
    selector.pack(pady=20, fill="x")

    root.mainloop()

if __name__ == "__main__":
    main()