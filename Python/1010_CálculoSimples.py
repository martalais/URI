# coding: utf-8
# @MartaLaís 1010

entrada1 = raw_input().split()
entrada2 = raw_input().split()

total1 = int(entrada1[1]) * float(entrada1[2])
total2 = int(entrada2[1]) * float(entrada2[2])

print "VALOR A PAGAR: R$ %.2f" % float(total1 + total2)
