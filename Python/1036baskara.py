# coding: utf-8
from math import sqrt
valores = raw_input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

delta = (b ** 2) - (4 * a * c)

if delta <= 0 or a <= 0:
	print "Impossivel calcular"
else:
	print "R1 = %.5f" % (((-b) + (sqrt(delta))) / (2.0 * a))
	print "R2 = %.5f" % (((-b) - (sqrt(delta))) / (2.0 * a))
