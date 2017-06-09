def chequeo(lon):
    lista=[0]*int(lon)
    for x in lista:
        numero=raw_input("Dame un numero para la lista ")
        lista[x]=numero

    print lista

print "Programa que ingresa una lista de numeros y revisa si un numero dado se encuentra en esta"
lon=raw_input("De cuantos valores sera tu lista ")
chequeo(lon)
