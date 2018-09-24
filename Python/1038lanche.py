# coding: utf-8

entrada = raw_input().split()

if int(entrada[0]) == 1:
	print "Total: R$ %.2f" % (4.00 * (float(entrada[1])))
if int(entrada[0]) == 2:
	print "Total: R$ %.2f" % (4.50 * (float(entrada[1])))
if int(entrada[0]) == 3:
	print "Total: R$ %.2f" % (5.00 * (float(entrada[1])))
if int(entrada[0]) == 4:
	print "Total: R$ %.2f" % (2.00 * (float(entrada[1])))
if int(entrada[0]) == 5:
	print "Total: R$ %.2f" % (1.50 * (float(entrada[1])))
