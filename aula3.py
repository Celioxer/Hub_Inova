# Aula 3 - Movimentação da Nave (Python para Games)
# 1 - Importando a biblioteca Turtle
import turtle
# 2 - Configurando a Janela do Jogo
janela = turtle.Screen()
janela.title("Space Shooter - Movimentação da Nave")
janela.bgcolor("black")
janela.setup(width=800, height=600)

# 3 - Criando o Ator (Nave)
nave = turtle.Turtle()
nave.shape("triangle")  # Formato nativo
nave.color("cyan")      # Cor no estilo neon
nave.penup()            # Não deixa linha desenhada
nave.setheading(90)     # Aponta o triângulo para cima
nave.goto(0, -240)      # Posiciona na parte inferior da tela (Eixo x, Eixo y)

# 4 - Funções de movimento com limite de tela
def mover_esquerda():
    x = nave.xcor()# (Eixo x da nave)
    if x > -370: # Limite da borda esquerda
        nave.setx(x - 20)

def mover_direita():
    x = nave.xcor()# (Eixo x da nave)
    if x < 370:  # Limite da borda direita
        nave.setx(x + 20)

def mover_cima():
    y = nave.ycor()# (Eixo y da nave)
    if y < 240:  # Limite superior
        nave.sety(y + 20)
    

def mover_baixo():
    y = nave.ycor()# (Eixo y da nave)
    if y > -240: # Limite inferior
        nave.sety(y - 20)

# 5 - Leitura de eventos de teclado (Setas e WASD)
janela.listen()#() Ativa a leitura de eventos do teclado
janela.onkeypress(mover_esquerda, "Left")
janela.onkeypress(mover_direita, "Right")
janela.onkeypress(mover_cima, "Up")
janela.onkeypress(mover_baixo, "Down")

janela.onkeypress(mover_esquerda, "a")
janela.onkeypress(mover_direita, "d")
janela.onkeypress(mover_cima, "w")
janela.onkeypress(mover_baixo, "s")


# 2.2 - Mantendo a janela aberta
janela.mainloop()#() Mantém a janela aberta até que seja fechada pelo usuário
