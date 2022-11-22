nome_do_arquivo = 'exercicio 2.txt'
arquivo = open(nome_do_arquivo, 'r')
texto = arquivo.readlines()
from math import factorial
n = int(input('digite um número: '))
texto.append('o fatorial de {} é {}\n'.format(n,str(factorial(n))))
arquivo = open(nome_do_arquivo, 'a')
arquivo.writelines(texto)
arquivo.close()
