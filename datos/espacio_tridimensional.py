import numpy as np

def generar_espacio_tridimensional(limite_inferior, limite_superior):
	x = np.linspace(limite_inferior, limite_superior, 30)
	y = np.linspace(limite_inferior, limite_superior, 30)
	return np.meshgrid(x, y)
	
def aplanar_datos(datos_x, datos_y):
	return datos_x.flatten(), datos_y.flatten()