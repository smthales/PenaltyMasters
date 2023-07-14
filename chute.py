from PPlay.gameimage import GameImage
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.collision import *
from random import randint
import time
from score import scoreList


def getGoleiro(isBlue):
    if isBlue:
        goleiro = Sprite("./assets/goleiro_azul.png")
    else:
        goleiro = Sprite("./assets/goleiro.png")
    
    return goleiro

def getJogador(isBlue):
    if isBlue:
        jogador = Sprite("./assets/jogador_costas.png")
    else:
        jogador = Sprite("./assets/jogador_vermelho.png")
    
    return jogador


def chute(isBlue):
    entrou = time.time()
    isBlue = not(isBlue)
    janela = Window(800, 345)
    teclado = Keyboard()
    user_mouse = Mouse()
    
    fundo = GameImage("./assets/area_penalti.png")
    jogador = getJogador(isBlue)
    jogador.set_position(358, 253)
    
    bola = Sprite("./assets/Ball_2x2_Sheet_2.png")
    bola.set_position(396, 235)
    gol = Sprite("./assets/gol.png")
    gol.set_position(335, 90)
    
    cursor = Sprite("./assets/Cursor.png")
    cursor.set_position(392, 230)
    goleiro = getGoleiro(not(isBlue))
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

    esquerda = Sprite("./assets/esquerda.png")
    esquerda.set_position(50, 300)

    centro = Sprite("./assets/centro.png")
    centro.set_position(290, 300)
    
    direita = Sprite("./assets/direita.png")
    direita.set_position(750 - direita.width, 300)
    
    # janela.draw_text("DEFESA!", janela.width / 2 - 150, janela.height / 2, size=100, color=(255, 255, 255), font_name="Arial", bold=True, italic=False)
    # janela.draw_text("GOL!", janela.width / 2 - 150, janela.height / 2, size=100, color=(255, 255, 255), font_name="Arial", bold=True, italic=False)
    
    defesa = False
    chutou = False
    num = randint(1, 3)
    vez_vermelho = False
    vez_azul = True
    troca = False
    pontos_vermelho = 0
    pontos_azul = 0
    contou = False
    


    while True:
        
        
        if teclado.key_pressed("ESCAPE"):
            return 0
        
        fundo.draw()
        gol.draw()
        cursor.draw()
        bola.draw()

        if teclado.key_pressed("ENTER") and chutou == True:
            chute(isBlue)

        
            
        
        

        if user_mouse.is_button_pressed(1):
            if user_mouse.is_over_object(esquerda):
                chutou = True
                if num == 1:
                    if goleiro.x > 388 - (gol.width / 2) + 20:
                        goleiro.move_x(-0.70)
                    if bola.x > 265 and bola.y > 170:
                        bola.y -= 400 * janela.delta_time()
                        bola.x -= 250 * janela.delta_time()
                    defesa = True
                        
                if num == 3:
                    
                    if goleiro.x < 388 + (gol.width / 2) - 20:
                        goleiro.move_x(0.70)
                    if bola.x > 265 and bola.y > 150:    
                        bola.y -= 400 * janela.delta_time()
                        bola.x -= 250 * janela.delta_time()
                    
                if num == 2:
                    
                    if bola.x > 265 and bola.y > 150:    
                        bola.y -= 400 * janela.delta_time()
                        bola.x -= 250 * janela.delta_time()
                
                           
            if user_mouse.is_over_object(centro):
                chutou = True
                if num == 1:
                    
                    if goleiro.x > 388 - (gol.width / 2) + 20:
                        goleiro.move_x(-0.70)
                    if bola.y > 150:
                        bola.y -= 400 * janela.delta_time()
                    
                    
                if num == 3:
                    
                    if goleiro.x < 388 + (gol.width / 2) - 20:
                        goleiro.move_x(0.70)
                    if bola.y > 150:
                        bola.y -= 400 * janela.delta_time()
                    
                    
                if num == 2:
                    if bola.y > 170:
                        bola.y -= 400 * janela.delta_time()
                        defesa = True
                
            if user_mouse.is_over_object(direita):
                chutou = True
                if num == 1:
                    
                    if goleiro.x > 388 - (gol.width / 2) + 20:
                        goleiro.move_x(-0.70)
                    if bola.x < 458 and bola.y > 150:
                        bola.y -= 400 * janela.delta_time()
                        bola.x += 250 * janela.delta_time()
                    
                if num == 3:
                    if goleiro.x < 388 + (gol.width / 2) - 20:
                        goleiro.move_x(0.70)
                    if bola.x < 458 and bola.y > 170:
                        bola.y -= 400 * janela.delta_time()
                        bola.x += 250 * janela.delta_time()
                    defesa = True
                
                if num == 2:
                    if bola.x < 458 and bola.y > 150:
                        bola.y -= 400 * janela.delta_time()
                        bola.x += 250 * janela.delta_time()

           
            
            
        torcida_1.draw()
        torcida_2.draw()
        torcida_3.draw()
        torcida_4.draw()
        torcida_principal.draw()
        esquerda.draw()
        centro.draw()
        direita.draw()
        if defesa == True and chutou == True:
            aviso = Sprite("./assets/aviso_defesa.png")
            aviso.set_position(gol.x - 40, janela.height / 2 - 150)
            aviso.draw()
        elif defesa == False and chutou == True:
            if contou == False:
                contou = True
                if isBlue:
                    scoreList[0] += 1
                else:
                    scoreList[1] += 1

            aviso = Sprite("./assets/aviso_gol.png")
            aviso.set_position(gol.x - 275, janela.height / 2 - 300)
            aviso.draw()
        janela.draw_text(f"AZUL: {scoreList[0]}", janela.width / 2 - 230, janela.height / 2 - 40, size=15, color=(255, 255, 255), font_name="Arial", bold=True, italic=False)
        janela.draw_text(f"VERMELHO: {scoreList[1]}", janela.width / 2 + 140, janela.height / 2 - 40, size=15, color=(255, 255, 255), font_name="Arial", bold=True, italic=False)
        jogador.draw()
        goleiro.draw()
        janela.update()