#!/usr/bin/env python
#-*- coding: utf-8 -*-

#procesar fichero(auth.log) y guardar las fechas en un formato procesable (datetime)
#y que almacenen solo los autentication failure


from datetime import datetime
import sys
import re


dic = {}


ori = open ('authlog.txt', 'r')
for linea in ori.readlines():
	if "authentication failure" in linea:	
		buscarip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', linea)
		for ip in buscarip:
			if ip not in dic:
				dic[ip]=[]
			dic[ip].append(datetime.strptime(linea[:15], "%b %d %H:%M:%S"))		
print dic


#Para que la salida del programa se vea "bonita", despues de ejecutarlo con run programa.py escribir "dic" y pulsar enter




#https://www.daniweb.com/programming/software-development/threads/507019/python-program-to-extract-ip-addresses-from-a-log-file
#En el enlace de arríba viene como pillar las ip de un fichero sin hardcodear















#for ip in range(len(ipes)):
#	dic[ipes[ip]] = ipes.count(ipes[ip])
#print dic
				

#dic.setdefault
#las ips van de 121 a 141

ori.close()
#for dat in guardar:
#	print datetime.strftime(dat, "%m %d %H:%M:%S")
	



#Ahora guardar cada IP con una lista (ordenada de más reciente a más antiguo) de las fechas en las que no consiguió conectar.

