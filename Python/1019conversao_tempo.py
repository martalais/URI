# coding: utf-8
# @MartaLaís 1019

entrada = int(raw_input())

horas = entrada / 3600
entrada = entrada - (horas * 3600)

minutos = entrada / 60
entrada = entrada - (minutos * 60)

segundos = entrada 

print "%d:%d:%d" % (horas,minutos,segundos)
