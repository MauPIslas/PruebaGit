def convertojaden(oracioncom):
  partes=len(oracioncom)
  oracion=oracioncom.split(" ")
  jadencode=[]
  if 0 < partes:
    for palabra in oracion:
      palabra=palabra.capitalize()
      jadencode.append(palabra)
    print ' '.join (jadencode)

  else:
    print "No introduciste nada"

print "Programa que convierte una oracion en Jaden Code"
oracioncom=raw_input("Dame la oración a convertir en Jaden Code: ")
convertojaden(oracioncom)
