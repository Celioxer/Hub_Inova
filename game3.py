import turtle

# 1. Configurando a janela do jogo
janela = turtle.Screen()
janela.title("Pong Game - Arena")
janela.bgcolor("black")
janela.setup(width=800, height=600)

# 2. Desenhando a linha central (Rede)
rede = turtle.Turtle()
rede.speed(0)
rede.color("white")
rede.penup()
rede.goto(0, -300)
rede.setheading(90) # Aponta para cima
rede.pendown()

# Desenha linha tracejada no meio
for _ in range(15):
    rede.forward(20)
    rede.penup()
    rede.forward(20)
    rede.pendown()

rede.hideturtle() # Esconde o ponteiro da caneta

# Mantém a janela aberta
janela.mainloop()