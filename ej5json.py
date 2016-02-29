# -*- coding: utf-8 -*-

#5- Programa que cuente el número de barrios que hay en la ciudad y mostrar el nombre de cada uno de ellos.

import json

with open("ejerciciojson.json") as archivo:
	doc=json.load(archivo)

cont=0
for barrios in doc["result"]:
	if barrios["calle"]["tipo"]["name"] == barrio:
		cont=cont+1
print cont		
