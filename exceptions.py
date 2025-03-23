import re

def main():
    # print(lista_melhores_restaurantes())
    print(divide_inteiros())


# Compila os restaurantes favoritos do usuário
def lista_melhores_restaurantes():
    melhores_restaurantes = []

    while True:
        try:
            restaurante = input("Digite um ótimo restaurante: ").strip()
        except EOFError:
            return ", ".join(melhores_restaurantes).title()
        else:
            if re.search(r"^[\w ]+$", restaurante):
                melhores_restaurantes.append(restaurante)
             

# Lida com duas exceções: ValueError e ZeroDivisionError
def divide_inteiros():
    while True:
        try:
            x = int(input(("x = ")))
            y = int(input(("y = ")))
        except ValueError:
            print("Os valores de x e y devem ser inteiros")
        else:
            try:
                divisao = int(x/y)
            except ZeroDivisionError:
                print("y não pode ser zero")
            else:
                return f"x/y = {divisao}"


if __name__ == "__main__":
    main()
