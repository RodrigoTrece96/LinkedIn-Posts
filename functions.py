# Criando um jogo de adivinhação usando Programação Funcional


import random


def main():
    level = gerar_level()        
    resposta = lambda m: random.randint(1,m)
    print(f"Escolha um número entre 1 e {level}")
    print(avaliar_chute(resposta(level)))


def gerar_level():
    while True:
        try:
            level = int(input("Digite um level: "))
        except ValueError:
            pass
        else:
            if level > 0:
                return level
        
        print("O level deve ser um inteiro positivo")


def avaliar_chute(resposta_correta):
    while True:        
        try:
            chute = int(input("Chute: "))
        except ValueError:
            print("O chute deve ser um inteiro!")
        else:
            if chute == resposta_correta:
                return "Acertou!"
            elif chute > resposta_correta:
                print("Chute muito grande!")
            elif chute < resposta_correta:
                print("Chute muito pequeno!")             


if __name__ == "__main__":
    main()
