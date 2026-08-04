import turtle
import time

# ==========================================
# 1. CONFIGURAÇÃO DA TELA E CAMINHO DOS ARQUIVOS
# ==========================================
tela = turtle.Screen()
tela.title("Jogo de Nave - Side Scrolling com Imagens")
tela.setup(width=800, height=600)
tela.tracer(0)

# Caminho base da pasta de imagens
PASTA = "kenney_space-shooter-remastered"

# Imagem de fundo
IMAGEM_FUNDO  = f"{PASTA}/Backgrounds/darkPurple.gif"
tela.bgpic(IMAGEM_FUNDO)

# Mapeando os caminhos das imagens dos atores
IMG_NAVE   = f"{PASTA}/PNG/playerShip1_blue.gif"
IMG_LASER  = f"{PASTA}/PNG/Lasers/laserBlue01.gif"
IMG_INIMIGO = f"{PASTA}/PNG/ufoRed.gif"

# Registrando os shapes no Turtle para poder usá-los
tela.register_shape(IMG_NAVE)
tela.register_shape(IMG_LASER)
tela.register_shape(IMG_INIMIGO)

# ==========================================
# 2. CRIAÇÃO DO JOGADOR (NAVE)
# ==========================================
jogador = turtle.Turtle()
jogador.shape(IMG_NAVE)
jogador.penup()
jogador.speed(0)
jogador.goto(-330, 0) # Posição inicial no canto esquerdo
vel_jogador = 20

# ==========================================
# 3. CRIAÇÃO DO TIRO (LASER)
# ==========================================
laser = turtle.Turtle()
laser.shape(IMG_LASER)
laser.penup()
laser.speed(0)
laser.goto(-1000, -1000) # Esconde o laser fora da tela no início
laser.hideturtle()       # Mantém invisível até ser atirado

vel_laser = 15
laser_ativo = False # Estado do laser (True = em movimento, False = pronto para atirar)

# ==========================================
# 4. CRIAÇÃO DO INIMIGO (UFO)
# ==========================================
inimigo = turtle.Turtle()
inimigo.shape(IMG_INIMIGO)
inimigo.penup()
inimigo.speed(0)
inimigo.goto(350, 0)

inimigo.dx = -3  # Velocidade horizontal (anda para a esquerda)
inimigo.dy = 2   # Velocidade vertical (sobe/desce)

# ==========================================
# 5. FUNÇÕES DE MOVIMENTAÇÃO E DISPARO
# ==========================================
def mover_cima():
    if jogador.ycor() < 250:
        jogador.sety(jogador.ycor() + vel_jogador)

def mover_baixo():
    if jogador.ycor() > -250:
        jogador.sety(jogador.ycor() - vel_jogador)

def mover_esquerda():
    if jogador.xcor() > -370:
        jogador.setx(jogador.xcor() - vel_jogador)

def mover_direita():
    if jogador.xcor() < 370:
        jogador.setx(jogador.xcor() + vel_jogador)

def atirar():
    global laser_ativo
    # Só atira se o laser não estiver rodando na tela
    if not laser_ativo:
        laser_ativo = True
        laser.goto(jogador.xcor() + 30, jogador.ycor()) # Sai da frente da nave
        laser.showturtle()

# ==========================================
# 6. MAPEAMENTO DE TECLAS
# ==========================================
tela.listen()

# Movimentação (Setas e WASD)
tela.onkeypress(mover_cima, "Up")
tela.onkeypress(mover_baixo, "Down")
tela.onkeypress(mover_esquerda, "Left")
tela.onkeypress(mover_direita, "Right")

tela.onkeypress(mover_cima, "w")
tela.onkeypress(mover_baixo, "s")
tela.onkeypress(mover_esquerda, "a")
tela.onkeypress(mover_direita, "d")

# Atirar
tela.onkeypress(atirar, "space")

# ==========================================
# 7. GAMELOOP (LOOP PRINCIPAL DO JOGO)
# ==========================================
while True:
    tela.update()

    # --- MOVIMENTO DO INIMIGO ---
    inimigo.setx(inimigo.xcor() + inimigo.dx)
    inimigo.sety(inimigo.ycor() + inimigo.dy)

    # Inimigo quica no teto e no chão
    if inimigo.ycor() > 260 or inimigo.ycor() < -260:
        inimigo.dy *= -1

    # Se o inimigo sair da tela pela esquerda, reaparece no canto direito
    if inimigo.xcor() < -410:
        inimigo.goto(400, 0)

    # --- MOVIMENTO DO LASER ---
    if laser_ativo:
        laser.setx(laser.xcor() + vel_laser)

        # Se o laser passar do limite da tela, ele recarrega
        if laser.xcor() > 410:
            laser.hideturtle()
            laser_ativo = False

    # --- COLISÃO: LASER x INIMIGO ---
    if laser_ativo and laser.distance(inimigo) < 30:
        # Reseta o tiro
        laser.hideturtle()
        laser_ativo = False
        
        # Reseta o inimigo para o lado direito da tela
        inimigo.goto(400, 100)

    # --- COLISÃO: NAVE x INIMIGO ---
    if jogador.distance(inimigo) < 40:
        print("💥 COLISÃO! Fim de jogo!")
        time.sleep(1)
        
        # Reseta posições
        jogador.goto(-330, 0)
        inimigo.goto(350, 0)