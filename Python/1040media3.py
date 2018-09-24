# coding: utf-8
notas = raw_input().split()

media = ((float(notas[0]) * 2) + (float(notas[1]) * 3) + (float(notas[2]) * 4) + (float(notas[3]) * 1)) / 10.0 

if media >= 7.0:
	print "Media: %.1f" % media
	print "Aluno aprovado."
elif media < 5.0:
	print "Media: %.1f" % float(media)
	print "Aluno reprovado."
elif media >= 5.0 and media <= 6.9:
	print "Media: %.1f" % media
	print "Aluno em exame."
	nova_exame = float(raw_input())
	print "Nota do exame: %.1f" % nova_exame
	media_final = (nova_exame + media) / 2.0
	if media_final >= 5.0:
		print "Aluno aprovado."
		print "Media final: %.1f" % media_final
	else:
		print "Aluno reprovado."
		print "Media final: %.1f" % media_final 
