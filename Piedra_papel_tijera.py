'''Piedra - papel - tijera
Realiza un código que solicite al usuario una de las tres opciones (Piedra, papel, tijera) y ejecuta 
una función que aleatoriamente elija otra opción, posteriormente imprime cual fue la opción del usuario 
y la de la máquina, para finalizar imprime quién fue el ganador.

Información adicional:
Tijera corta papel.
Papel tapa roca.
Roca rompe tijera.'''
from random import choice

def game(options, option_player):
    option_pc = choice(options)
    print(f"Jugador: {option_player} vs Pc: {option_pc}")

    winnig_player_options = {"tijera": "papel", "papel": "piedra", "piedra": "tijera"}

    if option_player == option_pc:
        print("Resultado empate")
    elif winnig_player_options[option_player] == option_pc:
        print("Resultado ganador jugador")
    else:
        print("Resultado ganador pc")


options = ["tijera", "piedra", "papel"]

option_player = input("Ingresa tu elección piedra, papel o tijera: ").lower()
if option_player in options:
    game(options,option_player)
