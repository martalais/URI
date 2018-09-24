# coding: utf-8
count = 0
for i in range(6):
	num = float(raw_input())
	if num > 0:
		count += 1

print "%d valores positivos" % count
