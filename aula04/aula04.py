#Tipo de dados

x = 1 #Int
x = 1.5 #Float
x = "Camelo" #String
x = True #Bool
n1=5;n2=3;n3=1;x = complex(1j)

x = ["moto", "lancha", "caminhao"] #Array/List
x = ("martelo", "serra", "alicate") #Tupla é igual ao Array porém não da pra alterar os dados

x = range(0,100) #List - cria uma lista de 0 a 100

x = { #Dict - dicionario
    "ferramenta": "Marreta",
    "local": "Obra",
    "nome": "Carlos"
}

'''
print("Valor: "+str(x))
print("Tipo: "+str(type(x)) )
'''
x = {3,6,7,2,0,5,1,2,2} #set - não imprime os valores duplicados
x = frozenset({3,6,7,2,0,5,1,2,2}) #set - congela esses caras


print("Valor: "+str(x))
print("Tipo: "+str(type(x)) )