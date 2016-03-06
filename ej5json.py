# -*- coding: utf-8 -*-

#5- Programa que cuente el número de barrios que hay en la ciudad y mostrar el nombre de cada uno de ellos.

import json

with open("ejerciciojson.json") as archivo:
	doc=json.load(archivo)

print ""
cont=0
for b in doc["result"]:
	contador=0
	for barrios in b:
		if barrios == "barrio":
			contador=contador+1
	if contador>0:		
		cont=cont+1	
		print "NOMBRE barrio: ",b["barrio"]["title"]	
print ""			
print "En la ciudad hay un total de ",cont,"barrios."	
print ""
