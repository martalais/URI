# coding: utf-8
# @MartaLaís 1018
valor = int(raw_input())

print valor

valor100 = valor/100

valor = valor - (valor100 * 100)
valor50 = valor/50

valor = valor - (valor50 *50)
valor20 = valor/20

valor = valor - (valor20 *20)
valor10 = valor/10

valor = valor - (valor10 *10)
valor5 = valor/5

valor = valor - (valor5 * 5)
valor2 = valor/2

valor = valor - (valor2 * 2)
valor1 = valor/1

valor = valor - (valor1 * 1)

print "%d nota(s) de R$ 100,00" % valor100
print "%d nota(s) de R$ 50,00" % valor50
print "%d nota(s) de R$ 20,00" % valor20
print "%d nota(s) de R$ 10,00" % valor10
print "%d nota(s) de R$ 5,00" % valor5
print "%d nota(s) de R$ 2,00" % valor2
print "%d nota(s) de R$ 1,00" % valor1
