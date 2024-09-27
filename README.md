# Interpolación de Superficies en Python

Este proyecto tiene como objetivo construir dos funciones de interpolación para aproximar la superficie generada por la función \( f(x, y) \) utilizando interpolación con funciones de base radial de dos tipos: 
1. **Multicuádrica**
2. **Poli-armónica** (\( r^5 \))

## Descripción

Se define la función \( f(x, y) \) en el archivo main como:

\[ f(x, y) = x^3 + y^3 - 3x^2 - 4y^2 - 5x \]

El código genera una cuadrícula de puntos en el plano \( xy \), evalúa la función en esos puntos y luego utiliza interpolación radial para estimar la superficie. Las superficies interpoladas se grafican para visualizar la precisión de los métodos de interpolación.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas de Python:

- `numpy`
- `matplotlib`

Puedes instalarlas utilizando `pip`:

```bash
pip install -r requirements.txt