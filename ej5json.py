# -*- coding: utf-8 -*-

#5- Programa que cuente el número de barrios que hay en la ciudad y mostrar el nombre de cada uno de ellos.

import json

with open("ejerciciojson.json") as archivo:
	doc=json.load(archivo)


b=doc["result"]
cont=0
for ba in b:
	count=0
	for s in ba:
		if s == "barrio":
			count=count+1
	if count>0:
		cont=cont+1	
print cont		



#b=doc["result"]

#for ba in b:
#	count=0
#	for s in ba:
#		if s == "barrio":
#			count=count+1
#	print count		
#if = 1 ... +1



#cont=0
#for barrios in doc["result"]:
#	if barrios["calle"]["tipo"]["name"] == "Barrio":
#		cont=cont+1
#print cont		
