from timeit import Timer
import random

for q in range(10000,1000001,20000):
    x = [x for x in range(q)]
    t = Timer('random.randrange(%d) in x'%q,'from __main__ import random,x')
    exe = t.timeit(number = 1000)
    print('list',exe)
    x = {x:None for x in range(q)}
    exe = t.timeit(number = 1000)
    print('dict',exe)





