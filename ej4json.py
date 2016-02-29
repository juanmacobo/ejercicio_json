# -*- coding: utf-8 -*-

#4- Pedir por teclado el codigo postal y mostrar el nombre y las coordenadas dondes se encuentra la calle.

import json

with open("ejerciciojson.json") as archivo:
	doc=json.load(archivo)

print ""
codigopostal=raw_input("Dime el codigo postal: ")

for cod in doc["result"]:
	if cod["codPos"] == codigopostal:
		print ""
		print "CODIGO POSTAL: ",cod["codPos"]
		print "NOMBRE calle: ",cod["calle"]["title"]
		print "COORDENADAS calle: ",cod["geometry"]["coordinates"]
