from pessoa import Pessoa
p1 = Pessoa('Felipe',1)
p2 = Pessoa('Fernanda',2)
print(p1.nome)
if p1.sexo == 1:
    print('Sexo: masculino')
else:
    print('Sexo: feminino')
print(p2.nome)
if p2.sexo == 1:
    print('Sexo: masculino')
else:
    print('Sexo: feminino')
from pessoa import Pais
pai1 = Pais('Jose',1,p1)
pai2 = Pais('Jessica',2,p2)
print(pai1.nome)
if pai1.sexo == 1:
    print('Sexo: masculino')
else:
    print('Sexo: feminino')
print('filho {}'.format(pai1.getCrianca))
print(pai2.nome)
if pai2.sexo == 1:
    print('Sexo: masculino')
else:
    print('Sexo: feminino')
print('filho {}'.format(pai2.getCrianca))
