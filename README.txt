Procedural abstraction - vc nao precisa saber oque esta dentro da caixa, apenas que ela funciona.ex: um metodo,
recebe um argumento e devolve uma resposta.Vc nao precisa saber da implementacao do metodo!

Operadores - RAL (Relacionais, Aritmeticos, Logicos(and, or, not)). Operadores logicos servem para interligar,
os operadores relacionais. ex: a==1 and b==2;


Algoritimo - passo a passo para resolver um problema.
Programa - algoritimo implementado em uma linguagem de programacao.

Collections - Qualquer colecao de dados, que possuem posicao relativa entre eles.
Strutura de dados lineares -Estruturas lineares pode ser pensado como tendo duas extremidades.
stack - lifo


Logica:

l1,l2,l3 = l2,l3,l1 Desta forma e possivel fazer com que todos os itens ocupem a primeira posicao apos alguns lopps.
'abcs' == 'abscccc' -  alguns algoritimos de anagrama podem falhar dizendo que as duas strings sao anagramas, pois,
procuram os chars da primeira na segunda, esquecendo dos chars que podem sobrar.

Python:

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

Algoritms:

1.Achar o menor valor em uma lista. chapter_2, list_functions.py
2. Detectar anagramas. chapter_2, anagram_functions.py
