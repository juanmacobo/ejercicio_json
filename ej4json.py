# -*- coding: utf-8 -*-

#4- Pedir por teclado el codigo postal y mostrar el nombre y las coordenadas dondes se encuentra la calle.

import json

with open("ejerciciojson.json") as archivo:
	doc=json.load(archivo)

codigopostal=raw_input("Dime el codigo postal: ")

for cod in doc["result"]:
	if cod["codPos"] == codigopostal:
		print cod["calle"]["title"]
		