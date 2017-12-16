#!/usr/bin/env python
#-*- coding: utf-8 -*-

#procesar fichero(auth.log) y guardar las fechas en un formato procesable (datetime)
#y que almacenen solo los autentication failure


from datetime import datetime
import sys
ipes = []
guardar = []
dic = {}


ori = open ('authlog.txt', 'r')
for linea in ori.readlines():
	if "authentication failure" in linea:	
		guardar.append(datetime.strptime(linea[:15], "%b %d %H:%M:%S"))
		ipes.append(linea[129:143])
		



for ip in range(len(ipes)):
	dic[ipes[ip]] = ipes.count(ipes[ip])
print dic
				



#dic.setdefault
#las ips van de 121 a 141

ori.close()
for dat in guardar:
	print datetime.strftime(dat, "%m %d %H:%M:%S")
	



#Ahora guardar cada IP con una lista (ordenada de más reciente a más antiguo) de las fechas en las que no consiguió conectar.

