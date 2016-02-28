# -*- coding: utf-8 -*-

#3- Pedir por teclado el codigo de la calle y mostrar el nombre de las calles que tienen ese código.

import json

with open("ejerciciojson.json") as archivo:
	doc=json.load(archivo)

codigo=raw_input("Dime el código de la calle: ")

for idcalle in doc["result"]:
	if idcalle["calle"]["id"] == codigo:
		print idcalle["calle"]["title"]
	