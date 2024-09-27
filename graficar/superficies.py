import matplotlib.pyplot as plt

def graficar_multiples_superficies(x, y, funciones_a_graficar):
    colores = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
    titulos = list(funciones_a_graficar.keys())
    funciones = funciones_a_graficar.values()
    
    column = len(titulos)  # número de columnas
    filas = 1  # número de filas necesarias
	
    # Crear la figura
    fig = plt.figure(figsize=(12, 6 * filas))  # Ajustar tamaño en función del número de filas

    # Graficar cada función en un subplot independiente
    color = 0
    for i, funcion in enumerate(funciones):
        ax = fig.add_subplot(filas, column, i + 1, projection='3d')  # Crear cada subplot
        ax.plot_surface(x, y, funcion, cmap=colores[color])  # Graficar la superficie
        ax.set_title(titulos[i])  # Asignar título a cada gráfico
        color = color + 1 if color < len(funciones) else 0

    plt.show()
