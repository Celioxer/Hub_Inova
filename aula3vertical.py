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

# 3.1 - Criando o Ator (Tiro) - CORRIGIDO
tiro = turtle.Turtle()
tiro.speed(0)           # NOVO: Animação na velocidade máxima para não acumular lag
tiro.shape("square")    # Formato do laser
tiro.color("yellow")    # Cor do tiro estilo neon
tiro.shapesize(stretch_wid=0.5, stretch_len=0.2) # Deixa o quadrado fininho e comprido igual um laser
tiro.penup()            # Não deixa linha desenhada
tiro.setheading(90)     # Aponta o tiro para cima
tiro.goto(0, 1000)      # NOVO: Posiciona o tiro fora da área visível da tela
tiro.hideturtle()       # Esconde o tiro até o jogador apertar o botão
estado_tiro = "pronto"  # Controle de estado: "pronto" para atirar ou "disparado" na tela

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

# 4.1 - Funções de disparo e movimentação do tiro - CORRIGIDO
def atirar():
    global estado_tiro
    if estado_tiro == "pronto": # Permite apenas 1 tiro por vez na tela
        estado_tiro = "disparado"
        tiro.goto(nave.xcor(), nave.ycor() + 10) # Posiciona o tiro na ponta da nave
        tiro.showturtle() # Mostra o tiro na tela

def mover_tiro():
    global estado_tiro
    if estado_tiro == "disparado":
        y = tiro.ycor()  # Pega a posição Y atual do tiro
        y += 20          # Soma 20 pixels para subir no eixo vertical
        tiro.sety(y)     # Atualiza a nova posição do tiro

        if y > 280:      # Verifica se ultrapassou o topo da tela
            tiro.hideturtle()  # Esconde o tiro
            tiro.goto(0, 1000) # NOVO: Envia o tiro de volta para fora da tela visível
            estado_tiro = "pronto" # Libera para o jogador atirar novamente

    janela.ontimer(mover_tiro, 20) # Chama essa mesma função a cada 20 milissegundos para manter o tiro subindo

# 5 - Leitura de eventos de teclado (Setas e WASD, espaço)
janela.listen()#() Ativa a leitura de eventos do teclado
janela.onkeypress(mover_esquerda, "Left")
janela.onkeypress(mover_direita, "Right")
janela.onkeypress(mover_cima, "Up")
janela.onkeypress(mover_baixo, "Down")
janela.onkeypress(mover_esquerda, "a")
janela.onkeypress(mover_direita, "d")
janela.onkeypress(mover_cima, "w")
janela.onkeypress(mover_baixo, "s")
janela.onkeypress(atirar, "space") # Ativa o disparo ao pressionar a tecla ESPAÇO

# 6 - Iniciando a movimentação automática do tiro
mover_tiro() # Liga o temporizador do tiro antes de iniciar a janela

# 2.2 - Mantendo a janela aberta
janela.mainloop()#() Mantém a janela aberta até que seja fechada pelo usuário