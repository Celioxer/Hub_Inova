import turtle

# 1. Configurações da Janela
janela = turtle.Screen()
janela.title("Jogo de Nave - Controle de Movimento")
janela.bgcolor("black")
janela.setup(width=800, height=600)

# 2. Criando o Personagem (Nave)
nave = turtle.Turtle()
nave.shape("triangle")  # Usa o triângulo nativo para parecer uma nave
nave.color("red")      # Cor neon combina muito com tema de espaço
nave.penup()            # Evita que a nave risque a tela ao andar
nave.setheading(120)     # Gira o triângulo para apontar para cima

# 3. Funções de Movimentação (Estruturas com 'def')
def mover_cima():
    nave.sety(nave.ycor() + 20)

def mover_baixo():
    nave.sety(nave.ycor() - 20)

def mover_esquerda():
    nave.setx(nave.xcor() - 20)

def mover_direita():
    nave.setx(nave.xcor() + 20)

# 4. Mapeamento das Teclas do Teclado
janela.listen()
janela.onkeypress(mover_cima, "w")       # Tecla Seta para Cima
janela.onkeypress(mover_baixo, "s")    # Tecla Seta para Baixo
janela.onkeypress(mover_esquerda, "a") # Tecla Seta para Esquerda
janela.onkeypress(mover_direita, "d") # Tecla Seta para Direita

# Mantém a janela aberta e escutando eventos
janela.mainloop()