def vs(usuario):
    from random import choice
    usuario= usuario.lower()
    maquina=(choice(("piedra", "papel", "tijera")))
    if usuario== "":
        print "No introduciste nada"
    elif usuario=="piedra" or usuario=="papel" or usuario=="tijera":
        if usuario=="piedra":
            piedra= "tijera"<"piedra"<"papel"
            print maquina
            print piedra

        if usuario=="papel" :
            print usuario
        if usuario=="tijera":
            print usuario
    else:
        print "No introdujiste piedra papel o tijera"



print "Piedra papel o tijera"
usuario= raw_input("Elige entre piedra papel o tijera ")
vs(usuario)
