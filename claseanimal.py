class Animal(object):
    num_animales=0
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        Animal.num_animales+=1

    def hablar(self):
        print "El {} {} dice Hola".format(self.raza,self.nombre)

class Perro(Animal):
    num_perros=0
    def __init__(self, nombre, raza):
        Animal.__init__(self, nombre, raza)
        Perro.num_perros+=1

    def aullar(self):
        print "El {} {} dice GOOF".format(self.raza, self.nombre)

class Gato(Animal):
    num_gatos=0
    def __init__(self, nombre, raza):
        Animal.__init__(self, nombre, raza)
        Gato.num_gatos+=1

    def maullar(self):
        print "El {} {} dice Meow".format(self.raza, self.nombre)

dingo1=Perro("Dingo","Chihuahua")
dingo2=Perro("Dingo","Chihuahua")
dingo3=Perro("Dingo","Chihuahua")

juan=Gato("Juan", "Persa")

print Perro.num_perros
print Animal.num_animales



"""

dingo = Perro("Dingo","Chihuahua")
print dingo.nombre

"""
