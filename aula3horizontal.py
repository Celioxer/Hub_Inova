# Aula 3 - Movimentação da Nave (Modo Lateral / Side Shooter)
# 1 - Importando a biblioteca Turtle
import turtle

# 2 - Configurando a Janela do Jogo
janela = turtle.Screen()
janela.title("Space Shooter - Modo Lateral")
janela.bgcolor("black")
# janela.bgpic("fundo5.gif") # Adiciona o fundo do espaço
janela.setup(width=800, height=600)

# 3 - Criando o Ator (Nave)
nave = turtle.Turtle()
nave.shape("triangle")  # Formato nativo
nave.color("cyan")      # Cor no estilo neon
nave.penup()            # Não deixa linha desenhada
nave.setheading(0)      # ALTERADO: Aponta o triângulo para a DIREITA (0 graus)
nave.goto(-350, 0)      # ALTERADO: Posiciona na borda ESQUERDA da tela (Eixo x, Eixo y)

# 3.1 - Criando o Ator (Tiro Horizontal)
tiro = turtle.Turtle()
tiro.speed(0)           # Animação na velocidade máxima para não acumular lag
tiro.shape("square")    # Formato do laser
tiro.color("yellow")    # Cor do tiro estilo neon
tiro.shapesize(stretch_wid=0.2, stretch_len=0.5) # ALTERADO: Invertido para o laser ficar deitado na horizontal
tiro.penup()            # Não deixa linha desenhada
tiro.setheading(0)      # ALTERADO: Aponta o tiro para a DIREITA (0 graus)
tiro.goto(1000, 0)      # Posiciona o tiro fora da área visível da tela
tiro.hideturtle()       # Esconde o tiro até o jogador apertar o botão
estado_tiro = "pronto"  # Controle de estado: "pronto" para atirar ou "disparado" na tela

# 4 - Funções de movimento da Nave (Exclusivo Vertical: Cima e Baixo)
def mover_cima():
    y = nave.ycor()     # (Eixo y da nave)
    if y < 260:         # Limite da borda superior
        nave.sety(y + 20)

def mover_baixo():
    y = nave.ycor()     # (Eixo y da nave)
    if y > -260:        # Limite da borda inferior
        nave.sety(y - 20)
def mover_esquerda():
    x = nave.xcor()     # (Eixo x da nave)
    if x > -370:        # Limite da borda esquerda
        nave.setx(x - 20)
def mover_direita():
    x = nave.xcor()     # (Eixo x da nave)
    if x < 370:         # Limite da borda direita
        nave.setx(x + 20)

# 4.1 - Funções de disparo e movimentação do tiro (Eixo Horizontal)
def atirar():
    global estado_tiro
    if estado_tiro == "pronto": # Permite apenas 1 tiro por vez na tela
        estado_tiro = "disparado"
        tiro.goto(nave.xcor() + 10, nave.ycor()) # ALTERADO: Posiciona o tiro na frente da nave no eixo X
        tiro.showturtle() # Mostra o tiro na tela

def mover_tiro():
    global estado_tiro
    if estado_tiro == "disparado":
        x = tiro.xcor()  # ALTERADO: Pega a posição X atual do tiro
        x += 20          # ALTERADO: Soma 20 pixels para avançar no eixo HORIZONTAL
        tiro.setx(x)     # ALTERADO: Atualiza a nova posição X do tiro

        if x > 380:      # ALTERADO: Verifica se ultrapassou a borda DIREITA da tela
            tiro.hideturtle()  # Esconde o tiro
            tiro.goto(1000, 0) # Envia o tiro para fora da tela visível
            estado_tiro = "pronto" # Libera para o jogador atirar novamente

    janela.ontimer(mover_tiro, 20) # Chama essa mesma função a cada 20 milissegundos para manter o tiro andando

# 5 - Leitura de eventos de teclado (Setas, WASD e Espaço)
janela.listen()#() Ativa a leitura de eventos do teclado
janela.onkeypress(mover_cima, "Up")
janela.onkeypress(mover_baixo, "Down")

janela.onkeypress(mover_cima, "w")
janela.onkeypress(mover_baixo, "s")

janela.onkeypress(atirar, "space") # Ativa o disparo ao pressionar a tecla ESPAÇO

# 6 - Iniciando a movimentação automática do tiro
mover_tiro() # Liga o temporizador do tiro antes de iniciar a janela

# 2.2 - Mantendo a janela aberta
janela.mainloop()#() Mantém a janela aberta até que seja fechada pelo usuário