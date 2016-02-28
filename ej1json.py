# -*- coding: utf-8 -*-

#1- Lista el nombre de todas las calles de Zaragoza.

import json

with open("ejerciciojson.json") as archivo:
	doc=json.load(archivo)

for calles in doc["result"]:
	print ""
	print "NOMBRE calle: ",calles["calle"]["title"]
