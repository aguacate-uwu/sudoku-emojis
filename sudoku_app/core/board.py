import tkinter as tk

class SudokuBoard(tk.Frame):
    def __init__(self, parent, cell_click_callback=None):
        super().__init__(parent)
        self.cell_click_callback = cell_click_callback
        self.cells = {}

        btn_size = 40
        line_thickness = 3
        small_line_thickness = 1

        for row in range(9):
            for col in range(9):
                # Insertamos separadores verticales antes de la columna 0,3,6 (excepto la 0)
                if col > 0 and col % 3 == 0:
                    sep = tk.Frame(self, width=line_thickness, height=btn_size,
                                   bg="black")
                    sep.grid(row=row*2, column=col*2-1, sticky="ns")

                # Insertamos separadores horizontales antes de la fila 0,3,6 (excepto la 0)
                if row > 0 and row % 3 == 0:
                    sep = tk.Frame(self, height=line_thickness, width=btn_size,
                                   bg="black")
                    sep.grid(row=row*2-1, column=col*2, sticky="ew")

                # Creamos botón para la celda
                btn = tk.Button(self, text="", font=("Arial", 20), width=3, height=2)
                btn.grid(row=row*2, column=col*2, sticky="nsew")

                # Guardamos botón en dict para actualizar texto después
                self.cells[(row, col)] = btn

                # Vinculamos el evento click
                if self.cell_click_callback:
                    btn.config(command=lambda r=row, c=col: self.cell_click_callback(r, c))

        for i in range(17):  # hay 17 filas/columnas
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)

    def set_cell(self, row, col, emoji):
        if (row, col) in self.cells:
            self.cells[(row, col)].config(text=emoji)