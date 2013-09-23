"""
Modulo composto por classes que tem por objetivo simular o cruzamento de caes belga em suas multiplas
variedades de cores. No final e aprensentada uma lista com todos os filhotes gerados seu pai e mae.
1. Cada cao so vai cruzar uma vez.
"""

import random


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


class BelgianDog(object):

    belgian_colors = {
        (0, 0): 'Black',
        (0, 1): 'Fulvo',
        (1, 0): 'Tervruen',
        (1, 1): 'Groenendael',
    }

    def __init__(self, genFather, genMother, cross = None):
        #nao sei se deveria passar o pai e mai, ja que eu os encontro no cruzamento.
        self.gens = (genFather, genMother)
        self.color = self.get_color()

    def get_color(self):
        '''faz mas sentido sme ser class pois a cor e do objeto e nao da classe'''
        return self.belgian_colors[self.gens]

    def get_prole(self):
        pass

class MaleBelgian(BelgianDog):

    gender = 'Male'

    def get_prole(self):
        gen_father = self.gens[0]
        gen_mother = self.gens[1]
        return 1 if gen_father and gen_mother else 0

    def __str__(self):
        return 'MaleBelgian: %s - %s : %s' % (self.color, self.gens, self.get_prole())


class FemaleBelgian(BelgianDog):

    gender = 'Female'

    def get_prole(self):
        gen_father = self.gens[0]
        gen_mother = self.gens[1]
        return 1 if gen_father or gen_mother else 0

    def __str__(self):
        return 'FemaleBelgian: %s - %s : %s' % (self.color, self.gens, self.get_prole())


class CrossDog(object):

    def __init__(self, fatherDog, motherDog):
        #vc so coloca os caes dessa forma, dentro do cruzamento, pq a quantidade deles e limitada.
        #Oque eu perco com isso, ao inves do relacionamento padrao nXn?
        #mas se nao for dessa forma como eu vou saber quem e a mae o pai e o filho.
        self.father = fatherDog
        self.mother = motherDog
        self.puppy  = self.cross()

    def cross(self):
        gender = random.choice([MaleBelgian, FemaleBelgian])
        father_prole = self.father.get_prole()
        mother_prole = self.mother.get_prole()
        puppy = gender(father_prole, mother_prole, self)
        return puppy

    def __str__(self):
        return 'Cruzamento: %s + %s, puppy: %s' % (self.father, self.mother, self.puppy)


def simulate_cross_dogs(parents = []):
    '''
    Funcao de simulacao, logo precisa de alguns
    parametros, ou melhor, condicoes de simulacao,
    para obter os resultados.
    '''
    male_dogs = Queue()
    female_dogs = Queue()
    cross_queue = Queue()

    for p in parents:
        if p.gender=='Male':
            male_dogs.enqueue(p)
        else:
            female_dogs.enqueue(p)

    while not male_dogs.isEmpty() and not female_dogs.isEmpty():
        father = male_dogs.dequeue()
        mother = female_dogs.dequeue()
        cross_dogs = CrossDog(father, mother)
        puppy = cross_dogs.puppy
        if puppy.gender == 'Male':
            male_dogs.enqueue(puppy)
        else:
            female_dogs.enqueue(puppy)
        cross_queue.enqueue(cross_dogs)

    while not cross_queue.isEmpty():
        print cross_queue.dequeue()


simulate_cross_dogs([MaleBelgian(1,0), FemaleBelgian(1,0), MaleBelgian(0,0), FemaleBelgian(0,0)])









#Um metodo que use propriedades staticas e propriedades do objeto, fudeu.
#por isso o python permite que nos acessemos atributos estaticos pelo self.
#quando um metodo possui o mesmo valor que um atributo, ou seja o valor de retorno dele e setado
#em um atributo, talvez seja duplicidade, fazer isso. ex:get_color()
# A diferenca entre usar uma classe ou uma funcao, e vc pensar que com as classes vc vai 
#estar armazenando informacoes. Se eu quero armazenar todos os cruzamentos ocorridos, eu
#preciso de uma classe. Senao poderia ser uma simples funcao.
#relacionamentos de um para um sao complicados, pq um dos lados sempre sai perdendo.
#se coloca o filho no cruzamento, o filho fica sem saber quem sao os pais. Se coloca o
#cruzamento nos filhos,
#relacionamentos de nXn com numeros limitados de quantidade???
#faz sentido eu modelar de forma relacional as classes se nao vou usar um banco de dados.
# quando uso o django, ele faz todo o mapeamento automatico entao faz sentido, mas se nao
#estou usando? e ae?
#qual o problema de duplicidade se nao vou usar banco??

#Staticos e Class so podem ser chamados tanto na class como no objeto, mas nunca podem ser chamados soltos.