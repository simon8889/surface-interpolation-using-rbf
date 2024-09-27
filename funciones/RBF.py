import numpy as np

# Función de distancia euclidiana
def distancia_euclidiana(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Interpolación Multicuádrica
def rbf_multicuadrica(f, valores_x, valores_y, c=1):
    valores_z = f(valores_x, valores_y)
    n = len(valores_x)
    A = np.zeros((n, n))
    
    # Construimos la matriz A del sistema
    for i in range(n):
        for j in range(n):
            r = distancia_euclidiana(valores_x[i], valores_y[i], valores_x[j], valores_y[j])
            A[i, j] = np.sqrt(r**2 + c**2)  # función multicuádrica
    
    # Resolver el sistema A * alpha = valores_z para los coeficientes alpha
    alpha = np.linalg.solve(A, valores_z)
    
    # Definir la función interpolada
    def funcion_interpolante(x, y):
        resultado = np.zeros_like(x)
        for i in range(n):
            r = np.sqrt((x - valores_x[i])**2 + (y - valores_y[i])**2)
            resultado += alpha[i] * np.sqrt(r**2 + c**2)
        return resultado
    
    return funcion_interpolante

# Interpolación Poli-armónica (r^5)
def rbf_poliarmonica(f, valores_x, valores_y):
    valores_z = f(valores_x, valores_y)
    n = len(valores_x)
    matriz = np.zeros((n, n))
    
    # Construimos la matriz del sistema
    for i in range(n):
        for j in range(n):
            r = distancia_euclidiana(valores_x[i], valores_y[i], valores_x[j], valores_y[j])
            matriz[i, j] = r**5  # función poli-armónica (r^5)
    
    # Resolver el sistema para los obterner los coeficientes alpha
    alpha = np.linalg.solve(matriz, valores_z)
    
    # Definir la función interpolada
    def funcion_interpolante(x, y):
        resultado = np.zeros_like(x)
        for i in range(n):
            r = np.sqrt((x - valores_x[i])**2 + (y - valores_y[i])**2)
            resultado += alpha[i] * r**5
        return resultado
    
    return funcion_interpolante

