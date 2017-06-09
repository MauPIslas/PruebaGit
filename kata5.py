def vs(usuario):
    from random import choice
    usuario= usuario.lower()
    maquina=(choice(("piedra", "papel", "tijera")))
    if usuario== "":
        print "No introduciste nada"
    elif usuario=="piedra" or usuario=="papel" or usuario=="tijera":
        if usuario=="piedra" and maquina== "papel":
            print "La maquina eligio "+maquina+"\n Gana la maquina"

        if usuario=="piedra" and maquina== "tijera":
            print "La maquina eligio "+maquina+"\n Gana el usuario"

        if usuario=="piedra" and maquina== "piedra":
            print "La maquina eligio "+maquina+"\n Hay un empate"



        if usuario=="papel" and maquina== "piedra":
            print "La maquina eligio "+maquina+"\n Gana el usuario"

        if usuario=="papel" and maquina== "tijera":
            print "La maquina eligio "+maquina+"\n Gana la maquina"





        if usuario=="tijera":

    else:
        print "No introdujiste piedra papel o tijera"



print "Piedra papel o tijera"
usuario= raw_input("Elige entre piedra papel o tijera ")
vs(usuario)
