# -*- coding: utf-8 -*-

#Prueba. Genera un fichero html con las calles:

ficherojson="index.html"
f=open(ficherojson,"w")

import json

with open("ejerciciojson.json") as archivo:
	doc=json.load(archivo)

for c in doc["result"]:
	f.write("<h1>"+c["calle"]["title"].encode("utf-8")+"</h1>"+"\n")
	f.write("<p>"+c["calle"]["tipo"]["name"].encode("utf-8")+"</p>"+"\n")
	f.write("<p>"+c["junta"]["title"].encode("utf-8")+"</p>"+"\n")
