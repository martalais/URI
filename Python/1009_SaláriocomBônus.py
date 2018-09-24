# coding: utf-8
# @MartaLaís 1009

nome_vendedor = str(raw_input())
salario_fixo = float(raw_input())
vendas = float(raw_input())

total = ((vendas * 15) / 100) + salario_fixo

print "TOTAL = R$ %.2f" % total 
