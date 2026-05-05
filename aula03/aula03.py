num1=num2=res=0

#canal="NicolasGomes" #Nesse contexto a variavel cana é declarada como uma variavel global

def cn():
    print(canal)
#cn()

'''Nesse caso criamos uma função cn que tem acesso a nossa variavel canal
Se chamamos a função com cn() ela printa o valor atribuido ao canal'''

 

def cn():
    canal="NicolasGomes" #Nesse contexto canal é uma variavel exclusiva da função cn
    print(canal)
#cn()

'''print(canal)
Se tentarmos printar o valor de canal não conseguimos, pois não é uma variavel global'''

def cn():
    global canal
    canal="NicolasGomes" #Nesse caso declaramos canal como uma variavel global, com isso podemos acessar novamente seus valores
    print(canal)
cn()

print(canal)
