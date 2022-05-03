from funciones_trabajo import *

def logica(datos_de_partida):
	
	movimientos_premitidos = datos_de_partida[1]
	comparar_lista = str(datos_de_partida[0]) 		#convierte la lista en cadena para que desarmar() no la modifique
	
	lista_de_juego = desarmar(datos_de_partida[0])[1]
	
	movimientos_hechos = 0

	generador_de_matriz(lista_de_juego)
	
	while True:
		

		print(f"""Movimientos: {movimientos_hechos}.\nMovimientos restantes: {movimientos_premitidos - movimientos_hechos}\nSi querés salir, escribí 'fin'.""")

		teclas = input("Movete (w,a,s,d): ")

		
		if 'w' in teclas or 'a' in teclas or 's' in teclas or 'd' in teclas:
			
			x = moverse(teclas, lista_de_juego)

			movimientos_hechos += x[0]

			lista_de_juego = x[1]
			
			generador_de_matriz(lista_de_juego)

			if comparar_lista == str(lista_de_juego):
				return 'win'
			
			elif movimientos_hechos >= movimientos_premitidos:
				return 'lose'
						
		
		if 'fin' in teclas:
			exit()
		

					


def main():

	print(f"""\n¡BIENVENIDO A FIFTEEN!""")
	
	new_game = input(f'Presioná ENTER para continuar\n')
	
	dificultad = seleccion_dificultad()
	
	salto()
	
	x = input(f"Elegiste jugar en {dificultad[0]}. Tenés {dificultad[1]} movimientos.")
	
	print(mensaje_filas_columnas())

	while True:
		n = input("Ingresá un número de filas y columnas: ")
		m = (" ") #agregar 4x4 automatico 

		if n == '' and m == '':
			n, m = 4, 4
			break
		if not n.isnumeric():
			
			print("Tiene que ser un número.")
			
			continue
		
		break	

	lista_inicial = generador_de_lista(int(n), int(n))
	
	datos_de_partida = [lista_inicial, int(dificultad[1])]

	log = logica(datos_de_partida)
		
	if log == 'win':
		print(f'¡GANASTE!. \n¡Gracias por jugar!')
	elif log == 'lose':
		print('Te quedaste sin movimientos. \n¡Gracias por jugar! ')
	
	
main()

"""
Un resumen general del codigo es el siguiente:

-La dificultad solo modifica el maximo de movimientos, los movimientos al azar son 500 y la dificultad que cumple con Z*5 es Facil.
-El codigo, en main, genera una lista de listas, en logica esta lista se desarma y se guarda una copia en forma de str (para que no sea modificada)
-Esta lista se muestra en 2D gracias a la funcion generador_de_matriz y se pide el movimiento
-La logica del movimiento es simple pero larga: 
	Se programo una funcion que recibe una cadena de letras wasd y las desarma.
	Para cada caracter aplica la funcion mover()
	mover() usa la funcion buscar_vacio() obtiene las coordenadas del jugador, luego aplica la intercambia por algun numero de su entorno,
	Ej: si el movimiento es w, remplaza el vacío por la letra de abajo y vice versa. Si no hay ningun numero abajo, no se ejecuta el movimiento.
-La funcion moverse devuelve una lista con los el numero de movimientos hechos y la lista modificada
-Esta lista se compara con la copia en str:
	si las listas son iguales return 'win', si son diferentes continue y si el numero de movimientos igual o excede el máximo, return 'lose'
-En todo momento, luego del inicio de la partida, se puede salir escribiendo 'end'.

"""