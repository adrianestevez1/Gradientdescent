import matplotlib.pyplot as plt
from numpy.random import randint
from numpy import linspace
import sympy as sp

from scipy.misc import derivative




def main():
	# Ejemplo del gradiente descendente aplicado a la función y = x^4 + 3x^3
	# La ecuación matemática para el gradiente (derivada) es = 2*x

	x_inicial = randint(10)
	alpha = 0.2
	n_iteraciones = 300

	iteraciones = []
	y = []

	x = x_inicial
	for i in range(n_iteraciones):
		print('------------------------')
		print('iteración ', str(i+1))

		# Calcular gradiente
		gradiente = dameGradiente(x)

		# Actualizar "x" usando gradiente descendente
		x = x - alpha*gradiente

		# Almacenar iteración y valor correspondiente
		y.append(x**4 + 3*x**3)
		iteraciones.append(i+1)

		# Imprimir resultados
		print('x = ', str(x), ', y = ', str(x**4 + 3*x**3))

	#plt.subplot(1, 2, 1)
	#plt.plot(iteraciones, y)
	#plt.xlabel('Iteración')
	#plt.ylabel('y')

	X = linspace(-5, 5, 100)
	Y = X**4 + 3*X**3
	plt.subplot(1, 2, 2)
	plt.plot(X, Y,'ro')
	plt.xlabel('x')
	plt.ylabel('y')

	plt.show()


def dameGradiente(x):
	d1fU = derivative(f,float(x))
	return int(d1fU)

def f(x):
	return x**4 + 3*x**3

main()
