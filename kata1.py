def cuando_cumplo_100(edad,nombre):
  ano=2017
  x=100
  ano_de_nacimiento= ano-edad
  los100= ano_de_nacimiento+x
  print str(nombre) + " cumpliras los 100 anos a en " + str(los100)
nombre=raw_input("Dame tu nombre: ")
edad=int (raw_input(" Hola "+ nombre + " dame tu edad: "))
cuando_cumplo_100(edad,nombre)
