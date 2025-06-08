import tkinter as tk
from ui.gui import SudokuGUI

def main():
    root = tk.Tk()
    root.title("Sudoku con Emojis - Prototipo")
    
    # Obtener resolución de pantalla y usarla como tamaño inicial
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")

    emojis = ["🍎", "🍌", "🥑", "🍇", "🍓", "🍍", "🥝", "🍉", "🍒",
              "🍑", "🍈", "🍋", "🍊", "🥭", "🍏", "🍐", "🥥", "🥕", "🌽"]

    app = SudokuGUI(root, emojis)
    root.mainloop()

if __name__ == "__main__":
    main()