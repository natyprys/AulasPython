class Person(object):
      def set_name(person, name):
         if len(name) >= 2:
              person.name = name
   
woman = Person()
   
# Nome da classe deve vir antes do uso da função, pois
# a função está dentro da classe.
Person.set_name(woman, 'Juliana')
   
# Vai imprimir "Juliana"
print (woman.name)