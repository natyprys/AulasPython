class Person(object):
     def set_name(self, name):
         if len(name) >= 2:
            self.name = name

woman = Person()
woman.set_name('Juliana')
print (woman.name)