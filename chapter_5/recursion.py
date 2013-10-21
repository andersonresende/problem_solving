
def listSum(numList):
	if len(numList) == 1:
		return numList[0]
	return numList[0] + listSum(numList[1:])


print listSum([1,3,5,7,9])


def factorial(num):
	if num <= 1:
		return num
	return num * factorial(num-1)


print factorial(4)


def convert_base(n, base):
	if n < base:
		return n
	return str(convert_base(n/base, base)) + str(n%base)

print convert_base(15,2)


def reverse_string(s):
	if len(s)<=1:
		return s

	return reverse_string(s[1:]) + s[0]

print reverse_string('123456')


def poli(s,n):
	if len(s)<=1:
		return s
	rev = poli(s[1:],n) + s[0]
	while len(rev)<n:
		return rev
	return rev == s

print poli('a311113a',len('a311113a'))


def poli_super(s):
	if len(s)<=1:
		return True
	if s[0] == s[-1]:
		return poli_super(s[1:-1])
	return False

print poli_super('ann1nna')





# a recursao funciona como uma pilha: os ultimos elementos sao retornados primeiro.
#qualquer numero dividido por dois vai restar 0 ou 1
#regra pra nao quebrar recursao se passar vazio if s<=1, usar <=

