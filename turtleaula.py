import turtle

# ==========================================
# 1. CONFIGURAÇÃO DA TELA
# ==========================================
tela = turtle.Screen()
tela.title("Jogo de Nave - Side Scrolling")
tela.bgcolor("black")  # Fundo preto para o espaço
tela.setup(width=800, height=600) # Largura x Altura
tela.tracer(0) # Desliga a animação padrão do turtle para o jogo rodar mais rápido

# ==========================================
# 2. CRIAÇÃO DO ATOR (JOGADOR)
# ==========================================
jogador = turtle.Turtle()
jogador.shape("triangle") # Forma de triângulo parecida com uma nave
jogador.color("cyan")
jogador.penup() # Não desenhar linha ao se mover
jogador.speed(0) # Velocidade máxima de animação
jogador.setheading(0) # Aponta para a direita (graus: 0=Dir, 90=Cima, 180=Esq, 270=Baixo)
jogador.goto(-350, 0) # Posição inicial (canto esquerdo da tela)

# Velocidade de movimento da nave
vel_jogador = 20

# ==========================================
# 3. FUNÇÕES DE MOVIMENTO E DESAFIO DOS LIMITES
# ==========================================
# O Desafio é não deixar passar de +/- 280 no Y (topo/chão) e +/- 380 no X (lados)

def mover_cima():
    y = jogador.ycor()
    if y < 280: # Limite do teto (Metade de 600 - margem de 20)
        jogador.sety(y + vel_jogador)

def mover_baixo():
    y = jogador.ycor()
    if y > -280: # Limite do chão
        jogador.sety(y - vel_jogador)

def mover_esquerda():
    x = jogador.xcor()
    if x > -380: # Limite esquerdo
        jogador.setx(x - vel_jogador)

def mover_direita():
    x = jogador.xcor()
    if x < 380: # Limite direito
        jogador.setx(x + vel_jogador)

# ==========================================
# 4. EVENTOS DE TECLADO (MAPEAMENTO)
# ==========================================
tela.listen() # Faz a tela "ouvir" o teclado

# Mapeando as Setas
tela.onkeypress(mover_cima, "Up")
tela.onkeypress(mover_baixo, "Down")
tela.onkeypress(mover_esquerda, "Left")
tela.onkeypress(mover_direita, "Right")

# Mapeando W/A/S/D (maiúsculas e minúsculas por precaução)
tela.onkeypress(mover_cima, "w")
tela.onkeypress(mover_baixo, "s")
tela.onkeypress(mover_esquerda, "a")
tela.onkeypress(mover_direita, "d")

# ==========================================
# 5. LOOP PRINCIPAL (GAMELOOP)
# ==========================================
while True:
    tela.update() # Atualiza a tela a cada repetição do loop