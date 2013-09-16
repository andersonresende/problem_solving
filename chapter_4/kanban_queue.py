'''
---Kaban Queue--- 
Elaborar um Kanban com WIP unico, recebendo itens por semana e no final apresentar a
quantidade de historias em um determinado tempo.
'''
from datetime import datetime

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


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


def main_execute_kanban():

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

	print '-----Kanban Finish Storys-----'
	q = kanban.finish_storys
	print q.size()
	while not q.isEmpty():
		s = q.dequeue()
		print 'Estimativa: %s / Espera no to-do: %s'  % (s.estimate, s.todo_wait)

main_execute_kanban()


