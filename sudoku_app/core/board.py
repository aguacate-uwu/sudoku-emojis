import tkinter as tk

class SudokuBoard(tk.Frame):
    def __init__(self, parent, on_cell_click):
        super().__init__(parent)
        self.on_cell_click = on_cell_click
        self.buttons_grid = []
        self.create_board()

    def create_board(self):
        for r in range(9):
            row_buttons = []
            for c in range(9):
                btn = tk.Button(self, text="", font=("Arial", 18), width=4, height=2,
                                relief="ridge", borderwidth=1,
                                command=lambda row=r, col=c: self.on_cell_click(row, col))
                btn.grid(row=r, column=c, padx=1, pady=1)
                row_buttons.append(btn)
            self.buttons_grid.append(row_buttons)

    def set_cell(self, row, col, value):
        self.buttons_grid[row][col].config(text=value)