class NStack(object):
	
	def __init__(self):
		self.pilha = []
		self.size = 10

	def push(self, data):
		self.pilha.append(data)

	def pop(self):
		return self.pilha.pop()

	def pop_at(self, p):
		size = self.size
		if len(self.pilha) > (p-1) * size:
			if len(self.pilha) > p * size:
				return self.pilha.pop((p*size)-1)
			else:
				return self.pilha.pop(-1)

		return None


mypilha = NStack()
[ mypilha.push(n) for n in range(30)]

print mypilha.pilha
print mypilha.pop_at(2)
print mypilha.pilha
print mypilha.pop_at(3)
print mypilha.pilha
print mypilha.pop_at(2)
print mypilha.pilha