def salto():

	print(f'\n')


def moverse(teclas, lista_de_juego):
	"""desarma una cadena de direcciones y las aplica secuencialmente a la lista de juego, devuelve la lista modificada y la cdad de movimientos"""
	for c in teclas:
	
		lista_de_juego = mover(lista_de_juego, c) 


	return len(teclas), lista_de_juego


def buscar_vacio(lista):

	for p in lista:
	
		if '  ' in p:
		
			return int(lista.index(p)),  int(p.index('  '))


def mover(lista, direccion): 


	player = buscar_vacio(lista) #cordenada 0 corresponde a las filas y cordenada 1 corresponde a las columnas


	if (len(lista[0])-1 != player[0]) and direccion == 'w' :

			lista [player[0]] [player[1]], lista [player[0]+1][player[1]] = lista [player[0]+1] [player[1]], lista [player[0]] [player[1]] #limita el movimiento de "w" si el vacío esta al final de alguna columna

	
	elif direccion == 's' and (player[0]!= 0):

		lista [player[0]] [player[1]], lista [player[0]-1] [player[1]] = lista [player[0]-1] [player[1]], lista [player[0]] [player[1]] #limita el movimiento "s" si el vacío esta al principio de alguna columna

	elif direccion == 'a' and (player[1] != len(lista)-1):

		lista [player[0]] [player[1]], lista [player[0]] [player[1]+1] = lista [player[0]] [player[1]+1], lista [player[0]] [player[1]] #limita el movimiento de "a" si el vacío se encuentra al final de alguna fila

	
	elif direccion == 'd' and (player[1]!= 0):

		lista [player[0]] [player[1]], lista[player[0]] [player[1]-1] = lista [player[0]] [player[1]-1], lista [player[0]] [player[1]] #limita el movimiento de "d" si el vacío se encuentra al principio de alguna fila

		
	return lista


def generador_de_matriz(lista):
	"""Recibe una lista de listas y la imprime en forma de matriz de 2 dimensiones"""
	
	salto()

	print("Fifteen v1.0 . Brubru Games.sa")

	salto()
	
	for i in range(len(lista[0])):

		for j in range(len(lista)):
	
			print(str(lista[i][j]).center(5), end = '  |  ')
		
		salto()


def generador_de_lista(n, m):
	"""genera una lista de n listas de m numeros con un espacio vacío al final. Los numeros van de 1 a (n*m)-1"""
	lista_base = []
	numero = 0
	
	for i in range(n): 

		lista_interior = []

		for j in range (m):
			
			numero +=1

			if numero == n*m:
				
				lista_interior.append('  ')	
				
				break

			lista_interior.append(numero)
		
		lista_base.append(lista_interior)
	
	return lista_base


def desarmar(lista):

	import random
	movimientos_previos = []

	for i in range (500):

		movimiento = random.choice('wasd')

		movimientos_previos.append(movimiento) 
		

	cadena_generada = "".join(movimientos_previos) #une todos los caracteres para que se pueda utilizar moverse()
	
	for c in cadena_generada:
		
		datos = moverse(cadena_generada, lista)
		
	return datos


def seleccion_dificultad():
	
	while True:
	
		input_dificultad = input(mensaje_dificultad())

		if input_dificultad == '1':
			return 'Fácil', 2500
			
		if input_dificultad == '2':
			return 'Normal', 1500

		if input_dificultad == '3':
			return 'Difícil', 500
		
		if input_dificultad == '#secretosecreto123':			#pequeño easter egg
			
			print(easter_egg())
			x = input()
			if x == '0':
				continue
			else:
				return 'Extremo', 200


def mensaje_dificultad():
	mensaje = """

Seleccioná la difficultad: 

1. Fácil (2500 movimientos).
2. Normal (1500 movimientos).
3. Difícil (500 movimientos).

Seleccioná un número(1/2/3): """
	return mensaje

def mensaje_filas_columnas():
	mensaje = """
En Fifteen tenés que ordenar una matríz de dimensiones NxM. 
Lo recomendable es jugar en 4x4, pero podés configurarla como vos quieras.
Tené en cuenta que el tamaño del tablero es proporcional a la dificultad: Más grande -> más dificil
Si dejás en blanco, se configurará en 4x4 automáticamente."""
	return mensaje

def easter_egg():
	mensaje = """
DESBLOQUEASTE LA DIFICULTAD SECRETA

Movimientos: 200

Si no te animás, podés seleccionar otra dificultad(Ingresá 0)
si querés continuar, presioná cualquier tecla(Excepto 0)"""
	return mensaje