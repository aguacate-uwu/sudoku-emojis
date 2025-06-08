import tkinter as tk

class SudokuBoard(tk.Frame):
    def __init__(self, parent, cell_click_callback=None):
        super().__init__(parent)
        self.cell_click_callback = cell_click_callback
        self.cells = {}
        self.locked_cells = set()  # NUEVO: conjunto de celdas bloqueadas

        btn_size = 40
        line_thickness = 3

        for row in range(9):
            for col in range(9):
                if col > 0 and col % 3 == 0:
                    sep = tk.Frame(self, width=line_thickness, height=btn_size, bg="black")
                    sep.grid(row=row*2, column=col*2-1, sticky="ns")

                if row > 0 and row % 3 == 0:
                    sep = tk.Frame(self, height=line_thickness, width=btn_size, bg="black")
                    sep.grid(row=row*2-1, column=col*2, sticky="ew")

                btn = tk.Button(self, text="", font=("Arial", 20), width=3, height=2)
                btn.grid(row=row*2, column=col*2, sticky="nsew")

                self.cells[(row, col)] = btn

                if self.cell_click_callback:
                    btn.config(command=lambda r=row, c=col: self.on_click(r, c))

        for i in range(17):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)

    def on_click(self, row, col):
        if (row, col) not in self.locked_cells and self.cell_click_callback:
            self.cell_click_callback(row, col)

    def set_cell(self, row, col, emoji):
        if (row, col) in self.cells and (row, col) not in self.locked_cells:
            self.cells[(row, col)].config(text=emoji)

    def set_initial_cell(self, row, col, emoji):
        """
        Coloca un emoji en una celda fija, bloqueándola para edición.
        """
        if (row, col) in self.cells:
            self.cells[(row, col)].config(text=emoji, state="disabled", disabledforeground="black", bg="#f0f0f0")
            self.locked_cells.add((row, col))

    def get_board(self):
        board_data = []
        for row in range(9):
            fila = []
            for col in range(9):
                btn = self.cells[(row, col)]
                texto = btn["text"]
                fila.append(texto if texto else "")
            board_data.append(fila)
        return board_data