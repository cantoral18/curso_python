import random

while True:
    aleatorio = random.randrange(0, 3)
    elijePc =""
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion=int(input("Elige tu opción "))
    if opcion == 1:
        elijeUsuario ="Piedra" 
    elif opcion == 2:
        elijeUsuario ="Papel" 
    elif opcion == 3:
        elijeUsuario = "Tijera"
    print("Elejiste: ", elijeUsuario)

    if aleatorio == 0:
        elijePc = "Piedra"
    elif aleatorio == 1:
        elijePc = "Papel" 
    elif aleatorio == 2:
        elijePc = "Tijera"
    print("La máquina elijio: ", elijePc)
    print("...")
    if elijePc == "Piedra" and elijeUsuario == "Papel":

        print("Ganaste, papel tapa ala  Piedra")
    elif elijePc =="Papel" and elijeUsuario == "Tijera": 
        print("Ganaste, Tijera corta papel")
    elif elijePc== "Tijera" and elijeUsuario == "Piedra":
        print("Ganaste, Piedra gana Tijera")
    if elijePc == "Papel" and elijeUsuario == "Piedra": 
        print("perdiste, Papel tapa ala  Piedra")
    elif elijePc == "Tijera" and elijeUsuario =="Papel": 
        print("perdiste, Tijera corta Papel")
    elif elijePc == "Piedra" and elijeUsuario == "Tijera":
        print("perdiste, Piedra gana Tijera") 
    elif elijePc == elijeUsuario:
        print("empate")

    play_again = input("quieres jugar de nuevo (s/n): ")
    if play_again.lower() !="s":
        break
