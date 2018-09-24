# coding: utf-8

entrada = raw_input().split()

if int(entrada[0]) > int(entrada[1]):
	horas = 24 - int(entrada[0])
	horas = horas + int(entrada[1])
	
elif int(entrada[0]) < int(entrada[1]):
	horas = int(entrada[1]) - int(entrada[0])

elif int(entrada[0]) == int(entrada[1]):
	horas = 24
	
print "O JOGO DUROU %d HORA(S)" % horas
