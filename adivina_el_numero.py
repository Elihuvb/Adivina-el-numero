import random


def main():

    try:
        aleatorio = random.randint(1, 100)
        elegido = int(input("Elige un número del 1 al 100: "))
        while elegido != aleatorio:
            if elegido < aleatorio:
                print("Elige un número más alto")
            else:
                print("Busca un número más bajo")
            elegido = int(input("Elige otro número: "))
        print("¡Ganaste!")
    except ValueError:
        print("Debes colocar un número")


if __name__ == '__main__':
    main()
