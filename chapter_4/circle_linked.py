"""
Modulo que simula uma ciranda, retirando os membros de forma randomica, ate que reste
uma unica pessoa, os membros estao ligados dentro de uma linked_lista.
"""
import random
from linked_list import UnorderedList


class People(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		boneco = ' --%s-- ' % self.name
		return boneco



def circle_simulation(quant_people):
	"Eu quero imprimir os bonequinhos em python :) todos ligadinhos pelos bracos "

	list_people = [ People(p) for p in range(quant_people) ]
	cadeia = UnorderedList()
	for lp in list_people:
		cadeia.add(lp)
	
	while cadeia.size() > 1:
		for p in list_people:
			print p,
		people = random.choice(list_people)
		list_people.remove(people)
		cadeia.remove(people)
		print ''

	print cadeia.head.data



circle_simulation(5)








