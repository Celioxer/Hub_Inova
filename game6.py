import turtle

# 1. Configuração da Tela
janela = turtle.Screen()
janela.title("Pong Final - Curso de Games")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

# Placar inicial
placar_a = 0
placar_b = 0

# 2. Raquete A
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("cyan")
raquete_a.shapesize(stretch_wid=5, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350, 0)

# 3. Raquete B
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("magenta")
raquete_b.shapesize(stretch_wid=5, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)

# 4. Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 3
bola.dy = 3

# 5. Escrita do Placar na Tela
texto_placar = turtle.Turtle()
texto_placar.speed(0)
texto_placar.color("white")
texto_placar.penup()
texto_placar.hideturtle()
texto_placar.goto(0, 260)
texto_placar.write("Jogador A: 0  |  Jogador B: 0", align="center", font=("Courier", 18, "bold"))

# Controles
def raquete_a_subir():
    if raquete_a.ycor() < 240:
        raquete_a.sety(raquete_a.ycor() + 25)

def raquete_a_descer():
    if raquete_a.ycor() > -240:
        raquete_a.sety(raquete_a.ycor() - 25)

def raquete_b_subir():
    if raquete_b.ycor() < 240:
        raquete_b.sety(raquete_b.ycor() + 25)

def raquete_b_descer():
    if raquete_b.ycor() > -240:
        raquete_b.sety(raquete_b.ycor() - 25)

janela.listen()
janela.onkeypress(raquete_a_subir, "w")
janela.onkeypress(raquete_a_descer, "s")
janela.onkeypress(raquete_b_subir, "Up")
janela.onkeypress(raquete_b_descer, "Down")

# 6. Loop Principal do Jogo
while True:
    janela.update()

    # Mover bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Colisão com Teto e Chão
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    # Ponto do Jogador B (Bola passou da esquerda)
    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar_b += 1
        texto_placar.clear()
        texto_placar.write(f"Jogador A: {placar_a}  |  Jogador B: {placar_b}", align="center", font=("Courier", 18, "bold"))

    # Ponto do Jogador A (Bola passou da direita)
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar_a += 1
        texto_placar.clear()
        texto_placar.write(f"Jogador A: {placar_a}  |  Jogador B: {placar_b}", align="center", font=("Courier", 18, "bold"))

    # Colisão com Raquete A
    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < raquete_a.ycor() + 50 and bola.ycor() > raquete_a.ycor() - 50):
        bola.setx(-340)
        bola.dx *= -1

    # Colisão com Raquete B
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < raquete_b.ycor() + 50 and bola.ycor() > raquete_b.ycor() - 50):
        bola.setx(340)
        bola.dx *= -1