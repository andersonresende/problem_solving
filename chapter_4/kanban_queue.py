'''
---Kaban Queue--- 
Elaborar um Kanban com WIP unico, recebendo itens por semana e no final apresentar a
quantidade de historias em um determinado tempo.
'''


#E possivel encapsular totalmente uma variavel usando descriptors de forma pura.
# class Desc(object):
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

	class Desc(object):
		'''Get sem Set'''
		def __get__(self, instance, owner):
			return self.value
		def __set__(self, instance, value):
			if  not hasattr(self, 'value'):
				self.value = value

	def __init__(self, description, day):
		self.description = description
		self.enter_todo_time = day
		self.estimate = self.set_estimate()

	#estimate = Desc()
	enter_todo_time = Desc()
	todo_wait = Desc()

	def todo_wait(self, start_kanban_time):
		wait = start_kanban_time - self.enter_todo_time
		self.todo_wait = wait
	
	def set_estimate(self):
		estimativas = (('P', 1), ('M', 2), ('G', 3),)
		if not hasattr(self, 'estimate'):
			import random
			return random.choice(estimativas)


from queue import Queue
class Kanban(object):
	def __init__(self):
		self.todo_storys = Queue()
		self.finish_storys = Queue()
		self.__current_story = None

	def add_storys(self, storys, day):
		'''Add new storys in kanban'''
		for s in storys:
			self.todo_storys.enqueue(s)

	def set_todo_story(self, day):
		story = self.todo_storys.dequeue()
		story.todo_wait(day)
		self.__current_story = story

	def add_finish_story(self):
		self.finish_storys.enqueue(self.__current_story)
		self.__current_story = None

	def is_busy(self):
		return self.__current_story

	def time_story_conclude(self, cont):
		return True if self.__current_story.estimate[1] == cont else False


def execute_kanban():

	cont = 0
	kanban = Kanban()
	for day in range(1,11):
		
		if day == 1:
			storys = []
			for s in ['a','b','c','d','e','f','g','h']:
				st = Story(s, day)
				print st.estimate
				storys.append(st)
			kanban.add_storys(storys, day)

		if not kanban.is_busy():
			kanban.set_todo_story(day)

		cont += 1
		if kanban.time_story_conclude(cont):
			kanban.add_finish_story()
			cont = 0
	
	for q in kanban.todo_storys, kanban.finish_storys:
		print '-----'*5
		print q.size()
		while not q.isEmpty():
			print q.dequeue().estimate






execute_kanban()





#apenas metodos com de objeto, mesmo estando abaixo do init, podem ser usados no init.Os demais
#metodos, so sao reconhecidos se chamados a partir da classe Classe.method()





#em python e possivel criar atributos apos criar a classe, pensar sobre a necessidade de alguns
#atributos serem criados antes ou depois da criacao da classe. Criar atributos durante a execucao,
#dificultam a documentacao, pois fica mais facil encontra-los ja no init e tambem e complicado
#pq se quisermos bloquear a criacao de atributos da nossa classe no __setattr__ nao poderemos fazer
#pois necessitamos dos atributos em execucao. No entanto existem atributos que so deveriam ser criados,
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


#Existem dois comportamentos distintos um e da um erro, excecao em tempo de execucao. Outro e
# vc atribuir um valor errado a uma variavel.ex: alterar um atributo sem passar pelo set dele.
#O problema e que para o primeiro comportamento, python vai permitir compilar e so vai dar pau
#em tempo de execucao.

#se eu quiser que um metodo so seja chamado dentro da classe, talvez eu tenha que sobrescrever o
#__getattribute__. Se o valor que ele atribui ja existir eu nao permito a chamada do metodo. O ideal
#mesmo e usar o dunder score.


#quando vc usa o dunder antes de uma variavel ou metodo vc nao consegue chama-lo fora da classe ou
# a partir do objeto.