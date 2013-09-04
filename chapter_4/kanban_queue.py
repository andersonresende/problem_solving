'''
---Kaban Queue---
Elaborar um Kanban com WIP unico, recebendo itens por semana e no final apresentar a
quantidade de historias em um determinado tempo.
'''

class Story(object):

	def __init__(self, description, enter_queue_time):
		self.description = description
		self.enter_queue_time = enter_queue_times
		#self.set_estimate()

	def __getattribute__(self, attr):
		if attr in object.__getattribute__(self, '__dict__'):
			

	def get_description(self):
		return self.description + 'sucesso'

	def queue_waiting(self, start_kanban_time):
		wait = start_kanban_time - self.enter_queue_time
		self.queue_wait = wait

	def get_queue_wait(self):
		return self.queue_wait

	def kanban_waiting(self, finish_kanban_time):
		wait = finish_kanban_time - self.queue_wait
		self.kanban_wait = wait

	def get_kanban_wait(self):
		return self.kanban_wait

	def set_estimate(self):
		import random
		estimativas = (('P', 1), ('M', 2), ('G', 3),)
		self.estimate =  random.choice(estimativas)

	def get_estimate_display(self):
		return self.estimate[0]

	def get_estimate_time(self):
		return self.estimate[1]




#em python e possivel criar atributos apos criar a classe, pensar sobre a necessidade de alguns
#atributos serem criados antes ou depois da criacao da classe.

#se vc so vai acessar um atributo apos ele estar setado, no fluxo natural do sistema, entao, nao 
#precisa se preoucupar com a tentativa de acessa-lo antes disso, se ele vai existir ou nao.


#muitas vezes nos criamos metodos para encapsular comportamentos de get e set e deixamos a classe
#aberta para esses atributos serem acessados normalmente, isso pode gerar erros para desenvolvedores
#futuros, que ao inves de usar os metodos usarao o atributo diretamente. Por isso e bom, tambem
#bloquear esses atributos. Para que ele de erro em tempo de execucao, se usado erradamente.

#Eu consigo bloquear um atributo, para ser acessado diretamente?? Eu consigo fazer com que ao chama-lo
#venha o get dele?





