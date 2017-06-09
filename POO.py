class Perro:
    num_perros=0
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        Perro.num_perros+=1
    def aullar(self):
        print "El {} {} dice GOOF".format(self.raza,self.nombre)

dingo = Perro("Dingo","Chihuahua")

dingo.aullar()
print Perro.num_perros




#print dingo.raza
#print Perro.num_perros
