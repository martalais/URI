# coding: utf-8
# @MartaLaís 1012

entrada = raw_input().split()

a = entrada[0]
b = entrada[1]
c = entrada[2]

pi = 3.14159

triangulo = (float(a) * float(c)) / 2.0
circulo = pi * (float(c) ** 2.0)
trapezio = (float(c) * (float(a) + float(b))) / 2.0
quadrado = float(b) ** 2
retangulo = float(a) * float(b)

print "TRIANGULO: %.3f" % triangulo
print "CIRCULO: %.3f" % circulo
print "TRAPEZIO: %.3f" % trapezio
print "QUADRADO: %.3f" % quadrado
print "RETANGULO: %.3f" % retangulo
