def insert_char(c, word):
	lista = []
	print c
	print word

	for i in range(0, len(word)+1):
		new = word[:i] + c + word[i:]
		lista.append(new)

	return lista

def perm(word):
	permutations = []
	if not word:
		return [""]

	first = word[0]
	parcial_perms = perm(word[1:])
	for w in parcial_perms:
		# faz permutacoes
		permutations.extend(insert_char(first, w))

	return permutations



print perm("abc")

