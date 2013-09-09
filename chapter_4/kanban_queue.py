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
		def __get__(self, instance, owner):
			return self.value
		def __set__(self, instance, value):
			if  not hasattr(self, 'value'):
				self.value = value				

	def __init__(self, description):
		self.description = description
		self.enter_queue_time = datetime.today()
		self.estimate = self.set_estimate()

	estimate = Desc()
	enter_queue_time = Desc()
	queue_wait = Desc()
	kanban_wait = Desc()

	def queue_wait(self, start_kanban_time):
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


from queue import Queue
class Kanban(object):
#kanban recebe uma historia vinda da fila, ele manipula ela de acordo com a sua estimativa
#e depois recebe outra historia. No final ele da a qauntidade de historias que ele trabalhou em um mes. 
#o kanban vai conter uma fila de storys. O kanban nao e uma fila pq ele precisa processar a historia,
#dividir em fazes, adicionar tempo.
#1. Kanban me de a quantidade de historias finalizadas em 30 dias
#2. Cada historia tenha registrado quanto tempo elas esperaram no to-do
#Adiciona as historias no kanban
#Em um loop de 30 dias
  #Pega a primeira historia do kanban
  #seta nela a data de entra no kanban
  #apos finalizar essa historia
  #adiciona ela na lista de finalizadas
  #ve se o kanban esta livre e pega uma nova historia
  #repete o processo ate acabar os 30 dias
	
	def __init__(self, storys):
		self.queue_storys = self.create_storys(storys)
		self.current_story = None

	def create_storys(storys):
		q = Queue()
		for s in storys:
			q.enqueue(s)
		return q

	# def start_kanban(self):




k = Kanban([1,2,3])
print k.queue_storys






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