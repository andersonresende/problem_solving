Procedural abstraction - vc nao precisa saber oque esta dentro da caixa, apenas que ela funciona.ex: um metodo,
recebe um argumento e devolve uma resposta.Vc nao precisa saber da implementacao do metodo!

Operadores - RAL (Relacionais, Aritmeticos, Logicos(and, or, not)). Operadores logicos servem para interligar,
os operadores relacionais. ex: a==1 and b==2;


Algoritimo - passo a passo para resolver um problema.
Programa - algoritimo implementado em uma linguagem de programacao.

Collections - Qualquer colecao de dados, que possuem posicao relativa entre eles.
Strutura de dados lineares -Estruturas lineares pode ser pensado como tendo duas extremidades.
    1. stack - lifo (entender que e uma pilha significa saber que sempre vai ser tirado o ultimo
                     elemento, vc so precisa se preocupar, quando e hora de adicionar ou retirar.
                     Mas vc sabe que sempre sera o ultimo.)
    2. queue - fifo
obs: nos pegamos situacoes do mundo real, filas, pilhas, e criamos classes que simulem esses
comportamentos.


Logica:

l1,l2,l3 = l2,l3,l1 Desta forma e possivel fazer com que todos os itens ocupem a primeira posicao apos alguns lopps.
'abcs' == 'abscccc' -  alguns algoritimos de anagrama podem falhar dizendo que as duas strings sao anagramas, pois,
procuram os chars da primeira na segunda, esquecendo dos chars que podem sobrar.

Python:

split - so cria lista se as strings tiverem espacos em branco, se nao e melhor usar list(word)
sorted(string) - ordena uma string, pode receber uma chave, key, como uma funcao para definir os criterios de ordencao.
por exemplo o tamanho de uma string.
ord(char) - retorna a posicao unicode de um char, pode ser usado para mapear a posicao de letras do alfabeto em uma
lista.
if [None,None] - a saida e True, False apenas quando a lista e vazia.
append e melhor que concatenacao para adicionar itens. e para retirar e melhor usar o pop() normal, ao inves do pop(0),
tirando os itens do inicio.
range() e melhor do que compression para criar uma lista com determinada quantidade de itens, mas ambos sao melhores do que
usar for com concatenacao ou append.
operador in - e O(1) em dicts, mas O(n) em listas.
Descriptors, Propertys and dunder - geralmente nao sao usados em python, a filosofia da linguagem acredita muito mais na leitura de codigo para um bom entendimento. 

Algoritms:

1.Achar o menor valor em uma lista. chapter_2, list_functions.py
2. Detectar anagramas. chapter_2, anagram_functions.py


OO:
1. vc tem que pensar o seguinte, se esta fazendo funcoes agrupadas em classe e para que a classe seja reutilizada
e nao as funcoes. logo nao deve pensar nessas funcoes sendo usadas soltas. Oque vc pode fazer se quiser reaproveitar
as funcoes e cria-las em modulos e utiliza-las em classes. No entanto, o poder de reutilizacao delas ficara, compre-
metido nas classes.
2. A grande sacada da orientacao a objetos  e que a simples escrita de um metodo ou atribuicao de uma variavel,
faca funcionar todo um grande projeto. Podemos pensar desta forma no uso das classes abstratas. LEmbrando que a classe
abstrata nada mais e do que uma classe como qualquer outra, que permite uma grande customizacao. ex: implementar os
metodos. E uma estrategia de heranca, para facilitar a extensao e implementacao de sistemas.
3.coisas de uma linha so, eu ja nao gosto de colocar em funcao por que dificulta a leitura.
outra coisa tem que pensar bem no quanto uma funcao tem qu ser generica, pq as vezes ela
comeca a ficar misturada. Tem que pensar bem no proposito de uma funcao e se ela pode ficar misturada.