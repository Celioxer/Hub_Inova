import turtle

janela = turtle.Screen()
janela.title("Space Shooter - Movimentação da Nave")
janela.bgcolor("black")
janela.setup(width=800, height=600)

# Criando o Ator (Nave)
nave = turtle.Turtle()
nave.shape("triangle")  # Formato nativo
nave.color("cyan")      # Cor no estilo neon
nave.penup()            # Não deixa linha desenhada
nave.setheading(90)     # Aponta o triângulo para cima
nave.goto(0, -240)      # Posiciona na parte inferior da tela (Eixo x, Eixo y)

# Variável de controle do Menu/Pausa ---
jogo_pausado = False

# --- Caneta para desenhar o Menu ---
menu_pen = turtle.Turtle()
menu_pen.hideturtle()
menu_pen.penup()

def desenhar_menu():
    menu_pen.clear()
    # Título do Menu
    menu_pen.color("white")
    menu_pen.goto(0, 100)
    menu_pen.write("PAUSA", align="center", font=("Arial", 28, "bold"))
    
    # Botão Retornar
    menu_pen.goto(0, 10)
    menu_pen.color("lime")
    menu_pen.write("[ RETORNAR AO JOGO ]", align="center", font=("Arial", 18, "bold"))
    
    # Botão Sair
    menu_pen.goto(0, -50)
    menu_pen.color("red")
    menu_pen.write("[ SAIR DO JOGO ]", align="center", font=("Arial", 18, "bold"))

def alternar_menu():
    global jogo_pausado
    jogo_pausado = not jogo_pausado
    if jogo_pausado:
        desenhar_menu()
    else:
        menu_pen.clear()

def clicar_no_menu(x, y):
    global jogo_pausado
    if jogo_pausado:
        # Clique no botão "RETORNAR"
        if -150 < x < 150 and -10 < y < 40:
            jogo_pausado = False
            menu_pen.clear()
        # Clique no botão "SAIR"
        elif -150 < x < 150 and -70 < y < -30:
            janela.bye()

# Funções de movimento com limite de tela
def mover_esquerda():
    if jogo_pausado: return  # Trava o movimento se estiver no menu
    x = nave.xcor()# (Eixo x da nave)
    if x > -370: # Limite da borda esquerda
        nave.setx(x - 20)

def mover_direita():
    if jogo_pausado: return  # Trava o movimento se estiver no menu
    x = nave.xcor()# (Eixo x da nave)
    if x < 370:  # Limite da borda direita
        nave.setx(x + 20)

def mover_cima():
    if jogo_pausado: return  # Trava o movimento se estiver no menu
    y = nave.ycor()# (Eixo y da nave)
    if y < 240:  # Limite superior
        nave.sety(y + 20)

def mover_baixo():
    if jogo_pausado: return  # Trava o movimento se estiver no menu
    y = nave.ycor()# (Eixo y da nave)
    if y > -240: # Limite inferior
        nave.sety(y - 20)

# Leitura de eventos de teclado (Setas e WASD)
janela.listen()#() Ativa a leitura de eventos do teclado
janela.onkeypress(mover_esquerda, "Left")
janela.onkeypress(mover_direita, "Right")
janela.onkeypress(mover_cima, "Up")
janela.onkeypress(mover_baixo, "Down")

janela.onkeypress(mover_esquerda, "a")
janela.onkeypress(mover_direita, "d")
janela.onkeypress(mover_cima, "w")
janela.onkeypress(mover_baixo, "s")

# ---  Tecla ESC ou 'P' para abrir o menu e cliques de mouse ---
janela.onkeypress(alternar_menu, "Escape")
janela.onkeypress(alternar_menu, "p")
janela.onscreenclick(clicar_no_menu)

janela.mainloop()#() Mantém a janela aberta até que seja fechada pelo usuário