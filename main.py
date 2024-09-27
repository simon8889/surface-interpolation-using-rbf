from funciones.RBF import rbf_multicuadrica, rbf_poliarmonica 
from graficar.superficies import graficar_multiples_superficies
from graficar.errores import graficar_multiples_errores
from datos.espacio_tridimensional import generar_espacio_tridimensional, aplanar_datos
from errores.calcular import calcular_error_relativo

# Definimos la función f(x, y) a interpolar
f = lambda x, y: x**3 + y**3 - 3*x**2 - 4*y**2 - 5*x

# definimos los rangos
espacio_x, espacio_y = generar_espacio_tridimensional(-2, 4)

# Aplanamos los datos para usar en el interpolador
valores_x, valores_y = aplanar_datos(espacio_x, espacio_y)

# Creamos las funciones de interpolación
interpolante_multicuadrica = rbf_multicuadrica(f, valores_x, valores_y)
interpolante_poliarminica = rbf_poliarmonica(f, valores_y, valores_x)

# Evaluamos las funciones interpolantes en la cuadrícula
z = f(espacio_x, espacio_y)
z_multicuadrica= interpolante_multicuadrica(espacio_x, espacio_y)
z_poliarmonica = interpolante_poliarminica(espacio_x, espacio_y)

graficar_multiples_superficies(espacio_x, espacio_y, {"Funcion Original": z,
												      "Interpolacion Multicuadrica": z_multicuadrica,
												      "Interpolacion Poliarmonica(r^5)": z_poliarmonica})

# Calcular los errores relativos
error_multicuadrica = calcular_error_relativo(z, z_multicuadrica)
error_poliarmonica = calcular_error_relativo(z, z_poliarmonica)

graficar_multiples_errores(espacio_x, espacio_y, {"Error Relativo - Multicuadrica": error_multicuadrica,
												  "Error relativo - Poliarmónica (r^5)": error_poliarmonica})