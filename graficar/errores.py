import matplotlib.pyplot as plt

def graficar_multiples_errores(x, y, errores_a_graficar):
    colores = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
    titulos = list(errores_a_graficar.keys())
    errores = list(errores_a_graficar.values())
    
    # Determinar número de filas y columnas
    column = len(titulos)  # número de columnas
    filas = 1  # número de filas necesarias
    
    # Crear la figura
    fig = plt.figure(figsize=(12, 6 * filas))  # Ajustar tamaño en función del número de filas
    
    # Graficar cada error en un subplot independiente
    for i, error in enumerate(errores):
        ax = fig.add_subplot(filas, column, i + 1)  # Crear cada subplot
        c1 = ax.imshow(error, cmap=colores[i % len(colores)], origin='lower', extent=[x.min(), x.max(), y.min(), y.max()])
        ax.set_title(titulos[i])  # Asignar título a cada gráfico
        plt.colorbar(c1, ax=ax)  # Añadir barra de color para referencia
    
    plt.show()