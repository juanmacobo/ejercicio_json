# -*- coding: utf-8 -*-

#2- Contar el numero de calles que hay en Zaragoza.

import json

with open("ejerciciojson.json") as archivo:
	doc=json.load(archivo)

nombre=doc["result"]

print ""
print "NUMERO de calles en Zaragoza: ",len(nombre)
print ""
