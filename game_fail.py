from pico2d import *

import game_framework
import game_stage1
import game_stage2
import game_stage3
import game_title

failbg=None
loadfont=None
received_hp=0
received_kill_mouse=0
received_kill_wildboar=0
received_kill_ironboar=0
브금만 넣으면 됨.

def enter():
    global failbg,loadfont
    failbg = load_image('resource//failboard.png')
    loadfont=load_font('resource//하얀분필B.ttf',80)

def exit():
    global failbg,loadfont
    del(failbg)
    del(loadfont)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(game_title)

def draw():
    clear_canvas()
    failbg.draw_to_origin(0,0,1600,900)
    loadfont.draw(350,380,'%d'%received_kill_mouse,(255,255,255))
    loadfont.draw(800,380,'%d'%received_kill_wildboar,(255,255,255))
    loadfont.draw(1250,380,'%d'%received_kill_ironboar,(255,255,255))
    update_canvas()

def update():
    pass
def pause():
    pass
def resume():
    pass

def get_imformation(death_mouse,death_wildboar,death_ironboar):
    global received_hp,received_kill_mouse,received_kill_wildboar,received_kill_ironboar
    received_kill_mouse=death_mouse
    received_kill_wildboar=death_wildboar
    received_kill_ironboar=death_ironboar
