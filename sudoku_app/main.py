import tkinter as tk
from ui.gui import SudokuGUI

def main():
    root = tk.Tk()
    root.title("Sudoku con Emojis - Prototipo")
    root.geometry("830x700")

    emojis = ["🍎", "🍌", "🥑", "🍇", "🍓", "🍍", "🥝", "🍉", "🍒",
              "🍑", "🍈", "🍋", "🍊", "🥭", "🍏", "🍐", "🥥", "🥕", "🌽"]

    app = SudokuGUI(root, emojis)
    root.mainloop()

if __name__ == "__main__":
    main()