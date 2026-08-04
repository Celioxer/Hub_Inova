import turtle
import math
import random
from PIL import Image, ImageTk, ImageSequence

# 1. Configuração da Janela
LARGURA = 800
ALTURA = 600

janela = turtle.Screen()
janela.title("DEFENSOR ESPACIAL - EDICAO PARALLAX COMPLETE")
janela.bgcolor("black")
janela.setup(width=LARGURA, height=ALTURA)
janela.tracer(0)
janela.addshape("nave.gif")

# --- CARREGAR GIF ANIMADO COM PILLOW ---
try:
    gif_pil = Image.open("fundo9.gif")
    quadros_fundo = []

    # Extrai e converte todos os frames do GIF
    for frame in ImageSequence.Iterator(gif_pil):
        # Redimensiona para o tamanho exato da janela
        frame_resized = frame.copy().resize((LARGURA, ALTURA)).convert("RGBA")
        quadros_fundo.append(ImageTk.PhotoImage(frame_resized))

    canvas = janela.getcanvas()
    # No Turtle, (0, 0) já é o centro da tela!
    bg_item = canvas.create_image(0, 0, image=quadros_fundo[0])
    canvas.tag_lower(bg_item)  # Envia para o fundo absoluto
except FileNotFoundError:
    print("Erro: Arquivo 'fundo9.gif' não encontrado no diretório.")
    quadros_fundo = []

frame_fundo_atual = 0
contador_animacao = 0

# 2. CENÁRIO DE FUNDO (Estrelas em Parallax)
estrelas = []
for _ in range(25):
    estrela = turtle.Turtle()
    estrela.shape("circle")
    estrela.color("white")
    estrela.penup()
    tam = random.uniform(0.05, 0.25)
    estrela.shapesize(stretch_wid=tam, stretch_len=tam)
    estrela.velocidade = tam * 12
    estrela.goto(random.randint(-LARGURA // 2 + 10, LARGURA // 2 - 10),
                 random.randint(-ALTURA // 2 + 20, ALTURA // 2 - 20))
    estrelas.append(estrela)

# 3. ATORES DO JOGO
pontuacao = 0

# Placar
texto_placar = turtle.Turtle()
texto_placar.speed(0)
texto_placar.color("white")
texto_placar.penup()
texto_placar.hideturtle()
texto_placar.goto(-LARGURA // 2 + 50, ALTURA // 2 - 50)
texto_placar.write("Pontos: 0", font=("Courier", 18, "bold"))

# Nave Jogador
nave = turtle.Turtle()
nave.shape("nave.gif")
nave.color("cyan")
nave.penup()
nave.setheading(0)
nave.goto(-LARGURA // 2 + 50, 0)

# Inimigo
inimigo = turtle.Turtle()
inimigo.shape("circle")
inimigo.color("red")
inimigo.penup()
inimigo.goto(LARGURA // 2 - 20, random.randint(-ALTURA // 2 + 60, ALTURA // 2 - 60))
velocidade_inimigo = 3.5

# Laser
laser = turtle.Turtle()
laser.shape("square")
laser.color("yellow")
laser.shapesize(stretch_wid=0.2, stretch_len=1)
laser.penup()
laser.hideturtle()
laser.goto(-1000, -1000)
estado_laser = "pronto"

# 4. CONTROLES
def mover_esquerda():
    x = nave.xcor()
    if x > -370:
        nave.setx(x - 20)

def mover_direita():
    x = nave.xcor()
    if x < 370:
        nave.setx(x + 20)
def mover_cima():
    if nave.ycor() < ALTURA // 2 - 60:
        nave.sety(nave.ycor() + 25)

def mover_baixo():
    if nave.ycor() > -ALTURA // 2 + 60:
        nave.sety(nave.ycor() - 25)

def atirar():
    global estado_laser
    if estado_laser == "pronto":
        estado_laser = "atirando"
        laser.goto(nave.xcor() + 15, nave.ycor())
        laser.showturtle()

janela.listen()
janela.onkeypress(mover_esquerda, "a")
janela.onkeypress(mover_direita, "d")
janela.onkeypress(mover_cima, "Up")
janela.onkeypress(mover_baixo, "Down")
janela.onkeypress(mover_cima, "w")
janela.onkeypress(mover_baixo, "s")
janela.onkeypress(atirar, "space")

# 5. LOOP PRINCIPAL
jogo_rodando = True
while jogo_rodando:
    janela.update()

    # --- ANIMAÇÃO DO GIF DE FUNDO ---
    if quadros_fundo:
        contador_animacao += 1
        if contador_animacao % 5 == 0:  # Ajuste a velocidade da animação do GIF aqui
            frame_fundo_atual = (frame_fundo_atual + 1) % len(quadros_fundo)
            canvas.itemconfig(bg_item, image=quadros_fundo[frame_fundo_atual])

    # --- MOVIMENTO DO CENÁRIO (PARALLAX) ---
    for estrela in estrelas:
        estrela.setx(estrela.xcor() - estrela.velocidade)
        if estrela.xcor() < -LARGURA // 2:
            estrela.goto(LARGURA // 2, random.randint(-ALTURA // 2 + 20, ALTURA // 2 - 20))

    # --- MOVIMENTO DO INIMIGO ---
    inimigo.setx(inimigo.xcor() - velocidade_inimigo)
    if inimigo.xcor() < -LARGURA // 2 - 10:
        inimigo.goto(LARGURA // 2 - 20, random.randint(-ALTURA // 2 + 60, ALTURA // 2 - 60))

    # --- MOVIMENTO DO LASER ---
    if estado_laser == "atirando":
        laser.setx(laser.xcor() + 18)

    if laser.xcor() > LARGURA // 2 - 10:
        laser.hideturtle()
        laser.goto(-1000, -1000)
        estado_laser = "pronto"

    # --- COLISÃO: LASER X INIMIGO ---
    if estado_laser == "atirando":
        distancia_tiro = math.sqrt((laser.xcor() - inimigo.xcor()) ** 2 + (laser.ycor() - inimigo.ycor()) ** 2)
        if distancia_tiro < 25:
            laser.hideturtle()
            laser.goto(-1000, -1000)
            estado_laser = "pronto"
            inimigo.goto(LARGURA // 2 - 20, random.randint(-ALTURA // 2 + 60, ALTURA // 2 - 60))

            pontuacao += 10
            velocidade_inimigo += 0.2
            texto_placar.clear()
            texto_placar.write(f"Pontos: {pontuacao}", font=("Courier", 18, "bold"))

    # --- COLISÃO: INIMIGO X NAVE (GAME OVER) ---
    distancia_nave = math.sqrt((nave.xcor() - inimigo.xcor()) ** 2 + (nave.ycor() - inimigo.ycor()) ** 2)
    if distancia_nave < 30:
        texto_placar.goto(0, 0)
        texto_placar.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
        jogo_rodando = False

janela.mainloop()