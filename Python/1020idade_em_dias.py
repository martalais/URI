# coding: utf-8

idade = int(raw_input())

anos = (idade - (idade % 365)) /365

meses = ((idade % 365) - ((idade % 365) % 30)) / 30

dias = (idade % 365) % 30

print "%d ano(s)" % anos
print "%d mes(es)" % meses
print "%d dia(s)" % dias
