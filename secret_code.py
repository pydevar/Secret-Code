#! /usr/bin/env python

import random



def eleccion_procesador():
	grupo = []

	colores = {1:"rojo", 2: "amarillo", 3: "azul", 4: "verde", 5:"naranja" , 6: "violeta", 7 : "blanco", 8:"negro"}

	for i in range  (4):
	
		grupo.append (colores [random.randint (1,8)])

	return grupo

print eleccion_procesador ()

# def eleccion_humano ():
	
	
	# cuando hace click, se colorean, se cargan en la fila


	
	
	
	
	





