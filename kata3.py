def listas(numero):
  iterar=[0]*int(numero)
  lista=[]
  for x in iterar:
    y=raw_input("\nDame el numero a ingresar")
    lista.append(y)
  primer=lista[0]
  ultimo=lista[int(numero)-1]
  intermedio=lista[1:len(lista)-1]
  print "\nEL primer numero en la lista es: "+ str(primer)
  print "\nEl ultimo numero en la lista es: "+ str(ultimo)
  if int(numero)<3:
    print "\nNo hay numeros intermedios"
  else:
    print "\nLos numeros intermedios son: "+', '.join (intermedio)

print "Programa que ingresa una lista y otroga el primer y ultimo valor de la lista, ademas de dar todos los numero que estan en medio de estos\n"
numero=raw_input("Cuantos elementos quieres en la lista")
listas(numero)
