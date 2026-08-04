import turtle

janela = turtle.Screen()
janela.title("Pong - Física da Bola")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0) # Otimização de desempenho

# Criando a Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)

# Velocidades da bola (dx e dy representam deslocamento)
bola.dx = 3
bola.dy = 3

# Game Loop Principal
while True:
    janela.update()

    # Mover a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Colisão com o teto
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1 # Inverte o sentido vertical

    # Colisão com o chão
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1