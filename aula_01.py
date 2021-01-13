# variáveis
a = 8 +9
print(a)
print()

# Valores Booleanos

True
False

print(not True)
print(not False)
print()

print("Porta OR")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()

print("Porta AND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print()

print('Expressões Booleanas')
print(6 > 5, 6 < 5, 5 <= 5, 5 == 5, 5 != 5)
print()

# Desvios condicionais
# Escreva um código que, dada a idade da pessoa, diga se ela é menor de idade.
print('O primeiro problema da idade.')
idade = 18
if idade < 18:
    print("É menor de idade")
else:
    print("É maior de idade")
print()

# Escreva um código que, dada a idade da pessoa, diga se ela é menor de idade, se ela é um adulto ou se é um idoso.

print('O segundo problema da idade.')
idade = 18
if idade < 18:
    print("É menor de idade")
elif idade < 65:
    print("É um adulto")
else:
    print("É um idoso")
print()

# Containers
print('Containers')
# String
print('1. String')
print(type(''), type("Renzo"))
print("Renzo's código")
print()
# Lista
print('2. String')
fruta_1 = 'Pera'
fruta_2 = 'Banana'
print(fruta_1, fruta_2)
print()
print('2. Listas')
frutas = ['Pera', 'Banana', 'Pessego']
print(frutas)
print(frutas[0], frutas[1], frutas[2])
tamanho = len(frutas)
print(tamanho)
print(frutas[-1])
print()
# 2.1 - Fatiamento
print('2.1 - Fatiamento')
numeros = list(range(1, 11))
print(numeros)
print(numeros[0:3])
print(numeros[:3])
tamanho = len(numeros)
print(numeros[tamanho-3:tamanho])
print(numeros[-3:])
print(numeros[1: 10 :2])
print(numeros[::-1])
renzo = 'Renzo Nuccitelli'
renzo2 = numeros.append('Renzo')
print(renzo2)
print(renzo[0])
print()
print('3. Tupla')
renzo_tupla = ('Renzo', 38)
print(renzo_tupla)
type(renzo_tupla)
print()
# 3. Laços de repetição
print('4. Laços de repetição')
# 1: Pera
# 2: Banana
# 3: Pêssego
indice = 0
for fruta in frutas:
    indice = indice +1
    print(indice,':',fruta)

for indice, fruta in enumerate(frutas, start=1):
    print(indice,':', fruta)

print()
# 5. Dicionário / Mapa / Hashmap / Lista esparsa
print('5. Dicionário / Mapa / Hashmap / Lista esparsa')
linguas = {'pt':'Portuguese', 'en': 'Ingles'}
print(linguas['pt'])
print(linguas['en'])
for chave in linguas:
    print(chave)
for chave in linguas.keys():
    print(chave)
for chave in linguas:
    print(chave, f': {linguas[chave]}')
for chave, valor in linguas.items(): # muita fera esta construção
    print(f'{chave}: {valor}')
print('Fim da Aula 01!')