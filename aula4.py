import turtle
import math

janela = turtle.Screen()
janela.title("Space Shooter Side-Scrolling - Física")
janela.bgpic("fundo5.gif")
janela.bgcolor("Black")
janela.setup(width=800, height=600)
janela.tracer(0)

# 1. Nave (Inicia na Esquerda e aponta para a Direita)
nave = turtle.Turtle()
nave.shape("triangle")
nave.color("cyan")
nave.penup()
nave.setheading(0)        # 0 graus = Apontado para a direita
nave.goto(-350, 0)        # Posiciona no canto esquerdo da tela

# 2. Inimigo (Surgindo do lado Direito)
inimigo = turtle.Turtle()
inimigo.shape("circle")
inimigo.color("red")
inimigo.penup()
inimigo.goto(350, 0)      # Começa no canto direito
velocidade_inimigo = 0.2

# 3. Laser (Tiro Horizontal)
laser = turtle.Turtle()
laser.shape("square")
laser.color("yellow")
laser.shapesize(stretch_wid=0.2, stretch_len=1) # Formato horizontal
laser.penup()
laser.hideturtle()
velocidade_laser = 5
estado_laser = "pronto"

# Função para disparar para a direita
def atirar():
    global estado_laser
    if estado_laser == "pronto":
        estado_laser = "atirando"
        laser.goto(nave.xcor() + 10, nave.ycor())
        laser.showturtle()

# Movimentação Vertical da Nave (Eixo Y)
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

    # Movimento do Inimigo (Da direita para a esquerda)
    inimigo.setx(inimigo.xcor() - velocidade_inimigo)
    
    # Se o inimigo passar da borda esquerda, ele renasce na direita
    if inimigo.xcor() < -380:
        inimigo.goto(380, 0)

    # Movimento do Laser (Para a direita)
    if estado_laser == "atirando":
        laser.setx(laser.xcor() + velocidade_laser)

    # Se o laser passar da borda direita, recarrega
    if laser.xcor() > 100:
        laser.hideturtle()
        estado_laser = "pronto"

    # Colisão por distância (Laser x Inimigo)
    distancia = math.sqrt((laser.xcor() - inimigo.xcor())**2 + (laser.ycor() - inimigo.ycor())**2)
    if distancia < 10:
        laser.hideturtle()
        estado_laser = "pronto"
        inimigo.goto(380, 0) # Reseta o inimigo no canto direito