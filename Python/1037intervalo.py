# coding: utf-8

entrada = float(raw_input())

if entrada >= 0 and entrada <= 25.00:
	print "Intervalo [0,25]"
elif entrada > 25.00 and entrada <= 50.00:
	print "Intervalo (25,50]"
elif entrada > 50.00 and entrada <= 75.00:
	print "Intervalo (50,75]"
elif entrada > 75.00 and entrada <= 100.00:
	print "Intervalo (75,100]"
else:
	print "Fora de intervalo" 
