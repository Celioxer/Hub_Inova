# 1ª FUNÇÃO: Boas-vindas e instrução inicial
def iniciar_sistema():
    print("=== SISTEMA DE COMBATE ESPACIAL ===")
    print("Inicializando módulos e verificando miras...")

# 2ª FUNÇÃO: O treinamento de mira (sua lógica original)
def treinar_mira():
    alvo_secreto = 5
    print("\n--- ETAPA 1: TREINAMENTO DE MIRA ---")
    
    for tentativa in range(1, 4):
        chute = int(input(f"Tentativa {tentativa}/3 - Escolha o ângulo do disparo (1 a 10): "))
        
        if chute == alvo_secreto:
            print(" Na mosca! Mira calibrada com sucesso.")
            return True  # Retorna True indicando sucesso
        elif chute > alvo_secreto:
            print("Tiro muito alto! Abaixe a mira.")
        else:
            print("Tiro muito baixo! Aumente a mira.")
            
    print(" Treinamento falhou. Tente novamente!")
    return False  # Retorna False se falhar

# 3ª FUNÇÃO: Relatório final do treinamento
def exibir_status(sucesso):
    print("\n--- RELATÓRIO FINAL ---")
    if sucesso:
        print(" Status: Piloto PRONTO para a missão!")
    else:
        print(" Status: Piloto precisa de MAIS TREINO!")


# === EXECUÇÃO (Chamando os 3 defs) ===
iniciar_sistema()                     # Chamada 1
acertou = treinar_mira()              # Chamada 2 (guarda o resultado True/False)
exibir_status(acertou)                # Chamada 3 (usa o resultado da função anterior)