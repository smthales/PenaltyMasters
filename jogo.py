from menu import *
from PPlay.keyboard import *
from random import randint
from chute import *


def iniciar_jogo():
    # Criar a janela do jogo e importar mouse
    janela = Window(800, 345)
    teclado = Keyboard()

    # Criar sprites
    fundo = GameImage("./assets/area_penalti.png")
    jogador_costas = Sprite("./assets/jogador_costas.png")
    jogador_costas.set_position(358, 253)
    bola = Sprite("./assets/Ball_2x2_Sheet_2.png")
    bola.set_position(396, 235)
    gol = Sprite("./assets/gol.png")
    gol.set_position(335, 90)
    cursor = Sprite("./assets/Cursor.png")
    cursor.set_position(392, 230)
    goleiro = Sprite("./assets/goleiro.png")
    goleiro.set_position(388, 142)
    torcida_1 = Sprite("./assets/torcida_200_3x3.png")
    torcida_1.set_position(18, 165)
    torcida_2 = Sprite("./assets/torcida_200_3x3.png")
    torcida_2.set_position(18, 223)
    torcida_3 = Sprite("./assets/torcida_200_3x3.png")
    torcida_3.set_position(727, 161)
    torcida_4 = Sprite("./assets/torcida_200_3x3.png")
    torcida_4.set_position(727, 222)
    torcida_principal = Sprite("./assets/torcida_principal.png")
    torcida_principal.set_position(81, 20)
    
    

    num = randint(1, 3)

    while True:
        if teclado.key_pressed("ESCAPE"):
            return 0
        

        
        
        if teclado.key_pressed("SPACE"):
            chute()

            



        
        fundo.draw()
        jogador_costas.draw()
        gol.draw()
        cursor.draw()
        bola.draw()
        goleiro.draw()
        torcida_1.draw()
        torcida_2.draw()
        torcida_3.draw()
        torcida_4.draw()
        torcida_principal.draw()
       
        janela.update()
