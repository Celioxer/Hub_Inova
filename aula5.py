import turtle
import math
import random

# Configuração da Janela
janela = turtle.Screen()
janela.title("SIDE-SCROLLER ESPACIAL - JOGO FINAL")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

# ===== DICA DE SPRITES PERSONALIZADOS (.GIF) =====
# ventana.register_shape("nave_horizontal.gif")
# ventana.register_shape("inimigo.gif")
# nave.shape("nave_horizontal.gif")
# inimigo.shape("inimigo.gif")
# =================================================

pontuacao = 0

# Placar
texto_placar = turtle.Turtle()
texto_placar.speed(0)
texto_placar.color("white")
texto_placar.penup()
texto_placar.hideturtle()
texto_placar.goto(-350, 250)
texto_placar.write("Pontos: 0", font=("Courier", 18, "bold"))

# Nave Principal
nave = turtle.Turtle()
nave.shape("triangle")
nave.color("cyan")
nave.penup()
nave.setheading(0) # Aponta para a direita
nave.goto(-350, 0)

# Inimigo
inimigo = turtle.Turtle()
inimigo.shape("circle")
inimigo.color("red")
inimigo.penup()
inimigo.goto(380, random.randint(-240, 240))
velocidade_inimigo = 3

# Laser
laser = turtle.Turtle()
laser.shape("square")
laser.color("yellow")
laser.shapesize(stretch_wid=0.2, stretch_len=1)
laser.penup()
laser.hideturtle()
estado_laser = "pronto"

# Controles
def mover_cima():
    if nave.ycor() < 240: nave.sety(nave.ycor() + 25)

def mover_baixo():
    if nave.ycor() > -240: nave.sety(nave.ycor() - 25)

def atirar():
    global estado_laser
    if estado_laser == "pronto":
        estado_laser = "atirando"
        laser.goto(nave.xcor() + 15, nave.ycor())
        laser.showturtle()

janela.listen()
janela.onkeypress(mover_cima, "Up")
janela.onkeypress(mover_baixo, "Down")
janela.onkeypress(mover_cima, "w")
janela.onkeypress(mover_baixo, "s")
janela.onkeypress(atirar, "space")

# Loop Principal do Jogo
jogo_rodando = True
while jogo_rodando:
    janela.update()

    # Movimento do Inimigo (Esquerda)
    inimigo.setx(inimigo.xcor() - velocidade_inimigo)

    # Se o inimigo escapar pela esquerda, perde-se o ponto e ele regenera
    if inimigo.xcor() < -390:
        inimigo.goto(380, random.randint(-240, 240))

    # Movimento do Laser (Direita)
    if estado_laser == "atirando":
        laser.setx(laser.xcor() + 15)

    if laser.xcor() > 390:
        laser.hideturtle()
        estado_laser = "pronto"

    # Colisão: Laser x Inimigo
    distancia_tiro = math.sqrt((laser.xcor() - inimigo.xcor())**2 + (laser.ycor() - inimigo.ycor())**2)
    if distancia_tiro < 25:
        laser.hideturtle()
        estado_laser = "pronto"
        inimigo.goto(380, random.randint(-240, 240)) # Surge em altura aleatória
        
        # Pontuação & Aumento de Dificuldade
        pontuacao += 10
        velocidade_inimigo += 0.3
        texto_placar.clear()
        texto_placar.write(f"Pontos: {pontuacao}", font=("Courier", 18, "bold"))

    # Colisão: Inimigo x Nave (Game Over)
    distancia_nave = math.sqrt((nave.xcor() - inimigo.xcor())**2 + (nave.ycor() - inimigo.ycor())**2)
    if distancia_nave < 30:
        texto_placar.goto(0, 0)
        texto_placar.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
        jogo_rodando = False

janela.mainloop()