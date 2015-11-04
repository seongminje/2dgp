from pico2d import *

import game_framework
import game_title



image = None
logo_time = 0.0

def enter():
    global image
    open_canvas(1600,900)
    image=load_image('resource\\kpu_credit.png')

def exit():
    global image
    del(image)

def update():
    global logo_time

    if(logo_time>1.0):
        logo_time=0
        game_framework.push_state(game_title)
        #game_framework.quit()
    delay(0.01)
    logo_time+=0.01

def draw():
    global image #값 수정이 아니라 사용만 하는거면 global 안해줘도됨.
    clear_canvas()
    image.draw_to_origin(0,0,1600,900)

    #monster1.clip_draw_to_origin(frame*70,254,70,46,monster1x,80,50,43)
    update_canvas()

def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




