#juego simple: piedra, papel o tijera

def jueguito():
    while True:
        print("### hola, jugamos?")
        a = int(input("jugador 1 elige: 1= piedra, 2= papel, 3= tijera: "))
        b = int(input("jugador 2 elige: 1= piedra, 2= papel, 3= tijera: "))

        if a >= 4 or b >= 4 or a <= 0 or b <= 0:
            print("elige 1, 2, o 3")
        elif a == 1 and b == 3:
            print("gana el jugador 1")
        elif a == 2 and b == 1:
            print("gana el jugador 1")
        elif a == 3 and b == 2:
            print("gana el jugador 1")
        elif a == b:
            print("empate")
        else:
            print("gana el jugador 2")
        print("")
jueguito()