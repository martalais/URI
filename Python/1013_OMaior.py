# coding: utf-8
# @MartaLaís 1013

entrada = raw_input().split()

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

maiorAB = (a + b + abs(a - b)) / 2
maiorBC = (b + c + abs(b - c)) / 2
maiorABC = (maiorAB + maiorBC + abs(maiorAB - maiorBC)) / 2

print "%d eh o maior" % maiorABC
