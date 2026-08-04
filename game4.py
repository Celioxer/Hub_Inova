import turtle

janela = turtle.Screen()
janela.title("Pong - Movimento")
janela.bgcolor("black")
janela.setup(width=800, height=600)

# Raquete A (Jogador 1 - Esquerda)
raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("white")
raquete_a.shapesize(stretch_wid=5, stretch_len=1) # Ajusta tamanho (100px x 20px)
raquete_a.penup()
raquete_a.goto(-350, 0)

# Funções de movimentação
def raquete_a_subir():
    y = raquete_a.ycor()
    if y < 240: # Limite da borda superior
        raquete_a.sety(y + 20)

def raquete_a_descer():
    y = raquete_a.ycor()
    if y > -240: # Limite da borda inferior
        raquete_a.sety(y - 20)

# Mapeando o teclado
janela.listen()
janela.onkeypress(raquete_a_subir, "w")
janela.onkeypress(raquete_a_descer, "s")

janela.mainloop()