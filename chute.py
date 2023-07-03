from PPlay.gameimage import GameImage
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.collision import *
from random import randint
from time import sleep



def chute():
    

    janela = Window(800, 345)
    teclado = Keyboard()
    user_mouse = Mouse()
    
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
    
    while True:
        
        
        if teclado.key_pressed("ESCAPE"):
            return 0
        
        if user_mouse.is_over_object(esquerda) and user_mouse.is_button_pressed(1):
            chutou = True
            if num == 1:
                if goleiro.x > 388 - (gol.width / 2) + 20:
                    goleiro.move_x(-0.70)
                if bola.x > 265:    
                    bola.y -= 400 * janela.delta_time()
                    bola.x -= 250 * janela.delta_time()
                defesa = True
            
                
                    
            if num == 3:
                if goleiro.x < 388 + (gol.width / 2) - 20:
                    goleiro.move_x(0.70)
                if bola.x > 265:    
                    bola.y -= 400 * janela.delta_time()
                    bola.x -= 250 * janela.delta_time()
                
            if num == 2:
                if bola.x > 265:    
                    bola.y -= 400 * janela.delta_time()
                    bola.x -= 250 * janela.delta_time()
                
            
        
        if user_mouse.is_over_object(centro) and user_mouse.is_button_pressed(1):
            chutou = True
            if num == 1:
                if goleiro.x > 388 - (gol.width / 2) + 20:
                    goleiro.move_x(-0.70)
                bola.y -= 400 * janela.delta_time()
                
                
                
            if num == 3:
                if goleiro.x < 388 + (gol.width / 2) - 20:
                    goleiro.move_x(0.70)
                bola.y -= 400 * janela.delta_time()
                
                
            if num == 2:
                bola.y -= 400 * janela.delta_time()
                defesa = True
                

            
            
        
        if user_mouse.is_over_object(direita) and user_mouse.is_button_pressed(1):
            chutou = True
            if num == 1:
                if goleiro.x > 388 - (gol.width / 2) + 20:
                    goleiro.move_x(-0.70)
                if bola.x < 458:    
                    bola.y -= 400 * janela.delta_time()
                    bola.x += 250 * janela.delta_time()
               
            if num == 3:
                if goleiro.x < 388 + (gol.width / 2) - 20:
                    goleiro.move_x(0.70)
                if bola.x < 458:    
                    bola.y -= 400 * janela.delta_time()
                    bola.x += 250 * janela.delta_time()
                defesa = True
                
            if num == 2:
                if bola.x < 458:    
                    bola.y -= 400 * janela.delta_time()
                    bola.x += 250 * janela.delta_time()
                
        
        
        
        
        
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
        esquerda.draw()
        centro.draw()
        direita.draw()
        if defesa == True and chutou == True:
            aviso = Sprite("./assets/aviso_defesa.png")
            aviso.set_position(gol.x - 40, janela.height / 2 - 150)
            aviso.draw()
        elif defesa == False and chutou == True:
            aviso = Sprite("./assets/aviso_gol.png")
            aviso.set_position(gol.x - 275, janela.height / 2 - 300)
            aviso.draw()
        janela.update()