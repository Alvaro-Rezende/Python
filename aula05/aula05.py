#Tipos numericos

import random 
'''Importamos uma biblioteca para randomizar numeros,
no meu caso eu randomizei numeros de 1 - 30'''

num_i = 2;
num_f = 6.3
num_c = 9j

num_r = [ #List/Array
    random.randrange(1, 30),
    random.randrange(1, 30),
    random.randrange(1, 30),
    random.randrange(1, 30),
]

x = num_r

print("Valor1: " + str(num_r[0]))
print("Valor1: " + str(num_r[1]))
print("Valor1: " + str(num_r[2]))
print("Valor1: " + str(num_r[3]))

#Casting - essas conversões de dados ex: para transformar em string - str(), int(), float()....

