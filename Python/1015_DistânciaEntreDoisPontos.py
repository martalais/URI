# coding: utf-8
# @MartaLaís 1015
import math 

x = raw_input().split()
y = raw_input().split()

x1 = float(x[0])
x2 = float(x[1])

y1 = float(y[0])
y2 = float(y[1])


total = math.sqrt((x2 - y2) ** 2 + (y1 - x1) ** 2)

print "%.4f" % total 
