'''
---Kaban Queue--- 
Elaborar um Kanban com WIP unico, recebendo itens por semana e no final apresentar a
quantidade de historias em um determinado tempo.
'''


#E possivel encapsular totalmente uma variavel usando descriptors de forma pura.
# class Desc_None(object):
# 		def __get__(self, instance, owner):
# 			return self.value
# 		def __set__(self, instance, value):
# 			self.value = value
#Agora para fazer comportamentos distintos, como por exemplo:
	#Inicializar uma variavel e so poder altera-la uma vez. ex: queu_wait
	# Inicializar uma varialvel e nao altera-la mais. ex: estimate

#E preciso alterar o comportamento do set no descriptor.


from datetime import datetime

class Story(object):

	class Desc_None(object):
		def __get__(self, instance, owner):
			return self.value
		def __set__(self, instance, value):
			if hasattr(self, 'value') and self.value==None:
				self.value = value
			elif not hasattr(self, 'value'):
				self.value = value

	class Desc(object):
		def __get__(self, instance, owner):
			return self.value
		def __set__(self, instance, value):
			if hasattr(self, 'value'):
				pass
			else:
				self.value = value

	def __init__(self, description):
		self.description = description
		self.enter_queue_time = datetime.today()
		self.estimate = self.set_estimate()
		self.queue_wait = None
		self.kanban_wait = None

	estimate = Desc()
	enter_queue_time = Desc()
	queue_wait = Desc_None()

	def queue_waits(self, start_kanban_time):
		wait = start_kanban_time - self.enter_queue_time
		self.queue_wait = wait

	def kanban_wait(self, finish_kanban_time):
		wait = finish_kanban_time - self.queue_wait
		self.kanban_wait = wait

	def set_estimate(self):
		estimativas = (('P', 1), ('M', 2), ('G', 3),)
		if not hasattr(self, 'estimate'):
			import random
			return random.choice(estimativas)



#em python e possivel criar atributos apos criar a classe, pensar sobre a necessidade de alguns
#atributos serem criados antes ou depois da criacao da classe. Criar atributos durante a execução,
#dificultam a documentação, pois fica mais facil encontra-los ja no init e tambem e complicado
#pq se quisermos bloquear a criacao de atributos da nossa classe no __setattr__ nao poderemos fazer
#pois necessitamos dos atributos em execução. No entanto existem atributos que so deveriam ser criados,
#apos a chamada de um metodo especifico e deixa-los no init, podemos altera-los sem o uso do metodo,
#e so depois bloquarmos a sua modificacao no descriptor.

#se vc so vai acessar um atributo apos ele estar setado, no fluxo natural do sistema, entao, nao 
#precisa se preoucupar com a tentativa de acessa-lo antes disso, se ele vai existir ou nao.


#muitas vezes nos criamos metodos para encapsular comportamentos de get e set e deixamos a classe
#aberta para esses atributos serem acessados normalmente, isso pode gerar erros para desenvolvedores
#futuros, que ao inves de usar os metodos usarao o atributo diretamente. Por isso e bom, tambem
#bloquear esses atributos. Para que ele de erro em tempo de execucao, se usado erradamente.

#Eu consigo bloquear um atributo, para ser acessado diretamente?? Eu consigo fazer com que ao chama-lo
#venha o get dele? Voce consegue fazer isso de forma correta e totalmente bloqueada usando Descriptors.
#propertys nao fazem esse trabalho tao bem, pois deixar o atributo ainda acessivel. 
#Com descriptors eu tambem consigo fazer com que um atributo so seja setado uma vez e depois mais nunca.


#Como inicializar um atributo via funcao no init e depois nao poder altera-lo??

#E melhor colocar os atributos no init  mesmo que so sejam usados depois, pq fica melhor pra documentacao
#e entendimento das classes.
