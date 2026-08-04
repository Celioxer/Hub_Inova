import turtle

janela = turtle.Screen()
janela.title("Space Shooter - Movimentação da Nave")
janela.bgcolor("black")
janela.setup(width=800, height=600)

# Criando a Nave
nave = turtle.Turtle()
nave.shape("triangle")
nave.color("cyan")
nave.penup()
nave.setheading(0)
nave.goto(0, -240)

# Criando o Texto de Apresentação
texto = turtle.Turtle()
texto.penup()
texto.hideturtle()
texto.color("white")
texto.goto(0, 200)
texto.write("SPACE SHOOTER\n\nMova a nave para começar!", 
            align="center", 
            font=("Times New Roman", 16, "bold"))

# Funções de movimento com a remoção do texto
def mover_esquerda():
    texto.clear()  # <-- Apaga a mensagem de apresentação da tela!
    x = nave.xcor()
    if x > -370:
        nave.setx(x - 20)

def mover_direita():
    texto.clear()  # <-- Apaga a mensagem de apresentação da tela!
    x = nave.xcor()
    if x < 370:
        nave.setx(x + 20)

def mover_cima():
    texto.clear()  # <-- Apaga a mensagem de apresentação da tela!
    y = nave.ycor()
    if y < 240:
        nave.sety(y + 20)

def mover_baixo():
    texto.clear()  # <-- Apaga a mensagem de apresentação da tela!
    y = nave.ycor()
    if y > -240:
        nave.sety(y - 20)

# Eventos do Teclado
janela.listen()
janela.onkeypress(mover_esquerda, "Left")
janela.onkeypress(mover_direita, "Right")
janela.onkeypress(mover_cima, "Up")
janela.onkeypress(mover_baixo, "Down")

janela.onkeypress(mover_esquerda, "a")
janela.onkeypress(mover_direita, "d")
janela.onkeypress(mover_cima, "w")
janela.onkeypress(mover_baixo, "s")

janela.mainloop()