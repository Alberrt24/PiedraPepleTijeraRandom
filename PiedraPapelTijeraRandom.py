import random
lista=["piedra","papel","tijera"]
print("Movimiento del jugador 1")
jugador1=input()
print("Movimiento del jugador 2")
jugador2=random.choice(lista)
if jugador1 == jugador2:
    print("Es un empate")
elif jugador1 == lista[0] and jugador2 == lista[1]:
     print("Jugador2 saco papel por lo tanto gana a jugador1")
elif jugador1 == lista[0] and jugador2 == lista[2]:
    print("Jugador1 uno saco piedra por lo tanto gana a jugador2")
elif jugador1 == lista[1] and jugador2 == lista[0]:
    print("Jugador1 saco papel por lo tanto gana a jugador2")
elif jugador1 == lista[1] and jugador2 == lista[2]:
    print("Jugador2 dos saco tijera por lo tanto gana a jugador1")
elif jugador1 == lista[2] and jugador2 == lista[0]:
    print("Jugador2 saco piedra por lo tanto gana a jugador1")
elif jugador1 == lista[2] and jugador2 == lista[1]:
    print("Jugador uno saco tijera por lo tanto gana a jugador2")

