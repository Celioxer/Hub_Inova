import turtle
import math

janela = turtle.Screen()
janela.title("DEFENSOR ESPACIAL - JOGO FINAL")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)

# ===== MÁGICA DOS SPRITES =====
# Se eles tiverem as imagens gif prontas:
# janela.register_shape("minhanave.gif")
# janela.register_shape("alien.gif")
#
# Depois basta usar: nave.shape("minhanave.gif")
# ==============================

pontuacao = 0

# Placar
texto_placar = turtle.Turtle()
texto_placar.speed(0)
texto_placar.color("white")
texto_placar.penup()
texto_placar.hideturtle()
texto_placar.goto(-380, 260)
texto_placar.write("Pontos: 0", font=("Courier", 18, "bold"))

nave = turtle.Turtle()
nave.shape("triangle") # Trocar por "minhanave.gif"
nave.color("cyan")
nave.penup()
nave.setheading(90)
nave.goto(0, -250)

inimigo = turtle.Turtle()
inimigo.shape("circle") # Trocar por "alien.gif"
inimigo.color("red")          
inimigo.penup()
inimigo.goto(0, 250)
dx_inimigo = 2

laser = turtle.Turtle()
laser.shape("square")
laser.color("yellow")
laser.shapesize(stretch_wid=1, stretch_len=0.2)
laser.penup()
laser.hideturtle()
estado_laser = "pronto"

def mover_esq():
    if nave.xcor() > -380: nave.setx(nave.xcor() - 25)

def mover_dir():
    if nave.xcor() < 380: nave.setx(nave.xcor() + 25)

def atirar():
    global estado_laser
    if estado_laser == "pronto":
        estado_laser = "atirando"
        laser.goto(nave.xcor(), nave.ycor() + 10)
        laser.showturtle()

janela.listen()
janela.onkeypress(mover_esq, "Left")
janela.onkeypress(mover_dir, "Right")
janela.onkeypress(atirar, "space")

while True:
    janela.update()

    # Move inimigo
    inimigo.setx(inimigo.xcor() + dx_inimigo)
    if inimigo.xcor() > 380 or inimigo.xcor() < -380:
        dx_inimigo *= -1
        inimigo.sety(inimigo.ycor() - 40)

    # Move laser
    if estado_laser == "atirando":
        laser.sety(laser.ycor() + 15)

    if laser.ycor() > 300:
        laser.hideturtle()
        estado_laser = "pronto"

    # Colisão Tiro x Inimigo
    distancia_tiro = math.sqrt((laser.xcor() - inimigo.xcor())**2 + (laser.ycor() - inimigo.ycor())**2)
    if distancia_tiro < 25:
        laser.hideturtle()
        estado_laser = "pronto"
        inimigo.goto(0, 250)
        
        # Aumenta placar
        pontuacao += 10
        texto_placar.clear()
        texto_placar.write(f"Pontos: {pontuacao}", font=("Courier", 18, "bold"))
        
        # Aumenta dificuldade
        if dx_inimigo > 0:
            dx_inimigo += 0.5
        else:
            dx_inimigo -= 0.5

    # Game Over (Inimigo tocou na nave)
    distancia_nave = math.sqrt((nave.xcor() - inimigo.xcor())**2 + (nave.ycor() - inimigo.ycor())**2)
    if distancia_nave < 30 or inimigo.ycor() < -280:
        texto_placar.goto(0, 0)
        texto_placar.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
        break # Para o loop   