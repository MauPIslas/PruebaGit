def chequeo(lon):
    iterar=[0] * int(lon)
    lista=[]
    for x in iterar:
        numero=raw_input("Dame un numero para la lista ")
        lista.append(numero)
    num=raw_input("Dame el numero a buscar en lista: ")
    vof=num in lista
    if vof==True:
        print num+" se encuentra dentro de la lista"
    else:
        print num+" no se encuentra en la lista"



print "Programa que ingresa una lista de numeros y revisa si un numero dado se encuentra en esta"
lon=raw_input("De cuantos valores sera tu lista ")
chequeo(lon)
