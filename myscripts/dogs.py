"""
Modulo composto por classes que tem por objetivo simular o cruzamento de caes belga em suas multiplas
variedades de cores. No final e aprensentada uma lista com todos os filhotes gerados seu pai e mae.
"""


class BelgianDog(object):

    belgian_colors = {
        (0, 0): 'Black',
        (0, 1): 'Fulvo',
        (1, 0): 'Tervruen',
        (1, 1): 'Groenendael',
    }

    def __init__(self, genFather, genMother):
        self.gens = (genFather, genMother)
        self.color = self.get_color()

    def get_color(self):
        return self.belgian_colors[self.gens]

    def get_prole(self):
        pass


class MaleBelgian(BelgianDog):

    def get_prole(self):
        gen_father = self.gens[0]
        gen_mother = self.gens[1]
        return 1 if gen_father and gen_mother else 0

    def __str__(self):
        return 'MaleBelgian: %s - %s : %s' % (self.color, self.gens, self.get_prole())


class FemaleBelgian(BelgianDog):

    def get_prole(self):
        gen_father = self.gens[0]
        gen_mother = self.gens[1]
        return 1 if gen_father or gen_mother else 0

    def __str__(self):
        return 'FemaleBelgian: %s - %s : %s' % (self.color, self.gens, self.get_prole())


m1 = MaleBelgian(1, 0)
print m1







#Um metodo que use propriedades staticas e propriedades do objeto, fudeu.
#por isso o python permite que nos acessemos atributos estaticos pelo self.
#quando um metodo possui o mesmo valor que um atributo, ou seja o valor de retorno dele e setado
#em um atributo, talvez seja duplicidade, fazer isso. ex:get_color()