import random

numero_secreto = random.randint(1, 100)
palpite = 0 

print("Bem-vindo ao Jogo de Adivinhação!")
print("Estou pensando em um número entre 1 e 100.")

while palpite != numero_secreto:
    try:
        palpite = int(input("Qual é o seu palpite? "))

        if palpite < numero_secreto:
            print("É maior!")
        elif palpite > numero_secreto:
            print("É menor!")
        else:
            print(f"Parabéns! Você acertou o número secreto: {numero_secreto}!")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")