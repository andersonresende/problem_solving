def bb(lista):
	quant = len(lista)
	for q in range(quant,0,-1):
		for i in range(0,q-1):
			if lista[i] > lista[i+1]:
				lista[i], lista[i+1] = lista[i+1], lista[i]
		print lista
	return lista

print bb([7,5,8,3,4,2,9])