curso="Curso de Python" #Uma String é nada mais nada menos que um array de caracteres

#print(curso[0:5]) Consigo delimitar um intervalo na minha impressão
#print(curso.strip()) Metodo strip - remove os espaços
#print(curso.lower()) Metodo Lower - converte a string para minusculo
#print(curso.lower().strip()) - É possivel utilizar os dois metodos em conjunto
#Temos também o upper que a contrario do lower, ele deixa maiusculo
#print(curso.replace("Python","C#")) - Metodo para substituir String ou caractere

a=curso.split(" ")  #O metodo split faz com que o print haja da seguinte forma:
                    #nesse caso ele print todo o codigo até achar o espaço e para
                    #o que gerando uma array. Não precisa ser o espaço, poderia ser a letra P
                    #ai ele iria printar todo o codigo até achar o P de "Python
print(a[2])

print("Tamanho: " + str(len(curso))) #Metodo len - utilizado para verificar o tamanho da string
