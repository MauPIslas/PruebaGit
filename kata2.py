def primos(num):
    residuo=int(num)%2
    if residuo==0:
        print ""+num+" no es un numero primo"
    else:
        print ""+num+" es un numero primo"


print "Programa que me dice si un numero es primo o no"
num=raw_input("Dame un numero: ")
primos(num)
