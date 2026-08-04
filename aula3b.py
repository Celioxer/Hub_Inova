import turtle
import math
import random

janela = turtle.Screen()
janela.title("Space Shooter Side-Scrolling - Física")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

# 1. Nave (Inicia na Esquerda e aponta para a Direita)
nave = turtle.Turtle()
nave.shape("triangle")
nave.color("cyan")
nave.penup()
nave.setheading(0)
nave.goto(-350, 0)

# 2. Inimigo (Surgindo do lado Direito)
inimigo = turtle.Turtle()
inimigo.shape("circle")
inimigo.penup()

# --- ontrole do padrão de movimento do inimigo ---
velocidade_inimigo = 0.2          # componente horizontal do movimento (vetor de velocidade)
inimigo_dy = 0                    # componente vertical do movimento (vetor de velocidade)
padrao_inimigo = "reta"           # pode ser "reta" ou "diagonal"

def novo_inimigo():
    """Sorteia um padrão de movimento e reposiciona o inimigo na direita."""
    global padrao_inimigo, inimigo_dy

    padrao_inimigo = random.choice(["reta", "diagonal"])

    if padrao_inimigo == "reta":
        inimigo.color("red")
        inimigo.shapesize(stretch_wid=1, stretch_len=1)
        inimigo_dy = 0
        y_inicial = random.choice([-150, -75, 0, 75, 150])  # aparece em alturas diferentes
    else:  # diagonal
        inimigo.color("orange")
        inimigo.shapesize(stretch_wid=1, stretch_len=1)
        # sorteia se ele vai descendo ou subindo em diagonal
        inimigo_dy = random.choice([-1, 1]) * random.uniform(0.8, 1.6)
        y_inicial = random.choice([-200, 200])  # começa perto de uma borda

    inimigo.goto(380, y_inicial)

novo_inimigo()  # posiciona o primeiro inimigo

# 3. Laser (Tiro Horizontal)
laser = turtle.Turtle()
laser.shape("square")
laser.color("yellow")
laser.shapesize(stretch_wid=0.3,stretch_len=1)
laser.penup()
laser.hideturtle()
velocidade_laser = 2
estado_laser = "pronto"

def atirar():
    global estado_laser
    if estado_laser == "pronto":
        estado_laser = "atirando"
        laser.goto(nave.xcor() + 10, nave.ycor())
        laser.showturtle()

def mover_cima():
    if nave.ycor() < 240:
        nave.sety(nave.ycor() + 20)

def mover_baixo():
    if nave.ycor() > -240:
        nave.sety(nave.ycor() - 20)

janela.listen()
janela.onkeypress(mover_cima, "Up")
janela.onkeypress(mover_baixo, "Down")
janela.onkeypress(mover_cima, "w")
janela.onkeypress(mover_baixo, "s")
janela.onkeypress(atirar, "space")

# === GAME LOOP ===
while True:
    janela.update()

    # Movimento do Inimigo
    inimigo.setx(inimigo.xcor() - velocidade_inimigo)

    if padrao_inimigo == "diagonal":
        inimigo.sety(inimigo.ycor() + inimigo_dy)
        # rebate ao tocar as bordas de cima/baixo, como uma bolinha quicando
        if inimigo.ycor() > 260 or inimigo.ycor() < -260:
            inimigo_dy = -inimigo_dy

    # Se o inimigo passar da borda esquerda, sorteia um novo padrão
    if inimigo.xcor() < -390:
        novo_inimigo()

    # Movimento do Laser
    if estado_laser == "atirando":
        laser.setx(laser.xcor() + velocidade_laser)

    if laser.xcor() > 390:
        laser.hideturtle()
        estado_laser = "pronto"

    # Colisão por distância (Laser x Inimigo)
    distancia = math.sqrt((laser.xcor() - inimigo.xcor())**2 + (laser.ycor() - inimigo.ycor())**2)
    if distancia < 20:
        laser.hideturtle()
        estado_laser = "pronto"
        novo_inimigo()