# coding: utf-8

soma = 0
count = 0
for i in range(6):
	num = float(raw_input())
	if num > 0:
		count += 1
		soma += num
		
print "%d valores positivos" % count
print "%.1f" % (soma / float(count))
