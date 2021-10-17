class Person(object):
     pass
# Uma vez que a função foi declarada dentro da classe, toda vez que a função for chamada o nome da classe deve vir antes; isto é, chamar uma função declarada dentro de uma classe é como chamá-la de um módulo.


def set_name(person, name):
# Não aceita nomes com menos de duas letras
   if len(name) >= 2:
        person.name = name

woman = Person()
set_name (woman , 'Juliana')

 # Vai imprimir "Juliana"
print (woman.name)

# Não vai mudar o valor, pois len('J') < 2
set_name(woman, 'J')
 
# Vai imprimir "Juliana" de novo, pois não mudou o valor
print (woman.name)