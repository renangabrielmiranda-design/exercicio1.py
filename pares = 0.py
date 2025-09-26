pares = 0
impares = 0

for _ in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")