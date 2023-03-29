# This is a sample Python script.
from dominio.impl.CreadorBarajaDomino import CreadorBarajaDomino
from dominio.impl.JugadorDomino import JugadorDomino

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


FICHAS = []


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    pozo_domino = CreadorBarajaDomino().crear_baraja()
    jugador1 = JugadorDomino("Juan")
    jugador2 = JugadorDomino("Alexis")
    jugador3 = JugadorDomino("Ulises")
    jugador4 = JugadorDomino("Emiliano")

    jugadores = [jugador1, jugador2, jugador3]

    for jugador in jugadores:
        for num in range(1, 8):
            jugador.mano.append(pozo_domino.pop())
        print(jugador.mano)

    for jugador in jugadores:
        print(f"Jugador: {jugador.nombre}")
        for ficha in jugador.mano:
            print(f"ficha: {ficha.cara1}, {ficha.cara2}")

    print(f"Pozo: {pozo_domino}")
    for ficha in pozo_domino:
        print(f"Ficha: {ficha.cara1}, {ficha.cara2}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
