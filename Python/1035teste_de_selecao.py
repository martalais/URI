# coding: utf-8

entrada = raw_input().split()

if int(entrada[1]) > int(entrada[2]) and int(entrada[3]) > int(entrada[0]) and int(entrada[2]) + int(entrada[3]) > int(entrada[0]) + int(entrada[1]) and int(entrada[2]) > 0 and int(entrada[3]) > 0 and int(entrada[0]) % 2 == 0:
	print "Valores aceitos"
else:
	print "Valores nao aceitos"
