# === AULA 1: COMPUTADOR DE BORDO DA NAVE ===

print("=================================")
print("  SISTEMA DE DEFESA ESPACIAL OS  ")
print("=================================")

# Entrada de dados e variáveis
piloto = input("Digite o nome do piloto: ")
idade = int(input("Digite a sua idade: "))

# Operadores Matemáticos
municao_inicial = 50
poder_de_fogo = idade * 2

print(f"\nBem-vindo, Comandante {piloto}!")
print(f"Status: {municao_inicial} disparos de laser | Poder de Fogo: {poder_de_fogo}")

# Tomada de decisão (if / elif / else)
print("\n[ALERTA]: Um asteroide inimigo se aproxima!")
opcao = input("Escolha a ação (1 - Atirar | 2 - Desviar): ")

if opcao == "1":
    print(" POW! Você destruiu o asteroide com sucesso!")
elif opcao == "2":
    print(" Ufa! Você esquivou a tempo.")
else:
    print(" Opção inválida! O asteroide colidiu com o escudo.")