# Jogo simples de adivinhação
numero_secreto = 7

print("=== JOGO DA ADIVINHAÇÃO ===")
chute = int(input("Adivinhe um número entre 1 e 10: "))

if chute == numero_secreto:
    print(" Incrível! Você acertou!")
elif chute > numero_secreto:
    print(" Muito alto! Tente um número menor.")
else:
    print(" Muito baixo! Tente um número maior.")