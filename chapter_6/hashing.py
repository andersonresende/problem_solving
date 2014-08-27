
# coding=utf-8

#No hashing vc faz um mapeamento dos valores que vc deseja armazenar
#em uma tabela criando um indice automatico.
#Digamos que você deseje armazenar os itens como se fosse uma
#biblioteca. Onde cada um vai ter seu numero exato. Dessa forma,
#você so precisaria procura-lo pelo numero.

#1) Implementar a organização de uma biblioteca.


# class Prateleira(object):
# 	"""
# 	Essa classe organiza itens por indices em uma lista, no entanto, ela não faz hashing.
# 	Ex: nos não podemos cadastrar itens com indices maiores do que o size definido. E se
# 	nos criarmos um size infinito, estaremos perdendo memoria. Então esse e o grande ganho
# 	do hash em relação a essa class criada sem hash.
# 	"""

# 	def __init__(self):
# 		self.size = 11
# 		self.lista = [None] * 11

# 	def put(self, key, data):
# 		self.lista[key] = data

# 	def get(self, key):
# 		return self.lista[key]


# if __name__ == '__main__':

# 	p = Prateleira()
# 	p.put(2, 'Pedro Leopoldo')
# 	p.put(5, 'Joao Pedro')

# 	print p.get(2), p.get(5)



##Ao inves de elaborar uma sequential search usar hashing, pesquisando por
##um numero em uma lista de numeros.

##Para entender o hash imagine como seria uma busca por uma pessoa em um sistema usando sequential
##search e comparando usando hashing.

def hashing(valor, size):
	''' Funcao que cria o hash para um valor '''
	return valor%size

def hash_search(valor, lista, size):
	''' 
	Funcao que recebe uma lista, cria uma tabela hashing
	e pesquisa pelo valor passado.
	'''
	hash_table = [None] * size

	for item in lista:
		hash_value = hashing(item, size)
		hash_table[hash_value] = item

	return hash_table[hashing(valor, size)] != None

#print map(lambda x: hash_search(x,[1,2,3,4,5],11),[1,2,4,5,6,7])

##Implemente uma class que simule uma tabela Hasshing:

class TableHash(object):
	def __init__(self, size):
		self.size = size
		self.table = [None] * self.size

	def hashing(self, valor):
		return valor%self.size

	def put(self, valor):
		hash = self.hashing(valor)
		self.table[hash] = valor

	def search(self, valor):
		hash = self.hashing(valor)
		return self.table[hash] != None
	

table = TableHash(11)

map(lambda x: table.put(x), range(1,11,2))

print filter(lambda x: table.search(x) == True, range(2,11,3))



