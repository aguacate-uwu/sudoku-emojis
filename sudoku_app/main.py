import tkinter as tk

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Sudoku con Emojis - Prototipo")
    root.geometry("800x700")  # Tamaño de la ventana
    
    # Etiqueta de bienvenida
    label = tk.Label(root, text="¡Bienvenido al Sudoku con Emojis!", font=("Arial", 18))
    label.pack(pady=20)
    
    # Crear la cuadrícula 9x9 de botones
    grid_frame = tk.Frame(root)
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
    
    # Ejecutar el loop principal
    root.mainloop()

if __name__ == "__main__":
    main()
