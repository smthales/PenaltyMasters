from PPlay.gameimage import GameImage
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *
from jogo import iniciar_jogo
from PPlay.sound import *


def menu():
    janela = Window(800, 345)
    janela.set_title("Penalty Masters")
    user_mouse = Mouse()
    fundo = GameImage("./assets/menu.png")
    fundo.set_position(janela.width/2 - fundo.width / 2, janela.height / 2 - fundo.height / 2)
    botao_jogar = Sprite("./assets/botao_jogar.png")
    botao_jogar.set_position(216, 229)

    som = Sound("world_anthem_spirits_40sec_master.ogg")


    while True:
        som.play()
        fundo.draw()
        botao_jogar.draw()
        janela.update()

        if user_mouse.is_over_object(botao_jogar) and user_mouse.is_button_pressed(1):
            iniciar_jogo()
