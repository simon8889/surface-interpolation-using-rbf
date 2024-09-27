import numpy as np

def calcular_error_relativo(funcion_original, funcion_interpolante):
	return np.abs((funcion_original - funcion_interpolante) / funcion_original)