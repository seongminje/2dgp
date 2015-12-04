from pico2d import *

import game_framework
import game_stage3
import game_title

clear_bgm=None
clearbg=None
loadfont=None
loadgradefont=None
received_hp=0
received_kill_mouse=0
received_kill_wildboar=0
received_kill_ironboar=0

def enter():
    global clearbg,loadfont,clear_bgm,loadgradefont
    clearbg = load_image('resource//scoreboard.png')
    loadfont=load_font('resource//하얀분필B.ttf',80)
    loadgradefont=load_font('resource//하얀분필B.ttf',160)
    clear_bgm=load_music('resource//sound//etc_stage_clear.ogg')

    clear_bgm.set_volume(56)
    clear_bgm.repeat_play()

def exit():
    global clearbg,loadfont,clear_bgm,loadgradefont
    del(clearbg)
    del(loadfont)
    del(clear_bgm)
    del(loadgradefont)

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
    clearbg.draw_to_origin(0,0,1600,900)
    loadfont.draw(420,715,'%d'%received_kill_mouse,(255,255,255))
    loadfont.draw(420,555,'%d'%received_kill_wildboar,(255,255,255))
    loadfont.draw(420,400,'%d'%received_kill_ironboar,(255,255,255))
    loadfont.draw(420,250,'%d'%received_hp,(255,255,255))

    loadfont.draw(830,715,'%d'%(received_kill_mouse*100),(255,255,255))
    loadfont.draw(830,555,'%d'%(received_kill_wildboar*100),(255,255,255))
    loadfont.draw(830,400,'%d'%(received_kill_ironboar*200),(255,255,255))
    loadfont.draw(830,250,'%d'%(received_hp*500),(255,255,255))
    loadfont.draw(1100,640,'%d'%(received_kill_mouse*100+received_kill_wildboar*100+received_kill_ironboar*200+received_hp*500),(255,255,255))

    if (received_kill_mouse*100+received_kill_wildboar*100+received_kill_ironboar*200+received_hp*500)>=23000:
        loadgradefont.draw(1160,325,'S',(255,255,255))
    elif (received_kill_mouse*100+received_kill_wildboar*100+received_kill_ironboar*200+received_hp*500)>=19000:
        loadgradefont.draw(1160,325,'A',(255,255,255))
    elif (received_kill_mouse*100+received_kill_wildboar*100+received_kill_ironboar*200+received_hp*500)>=15000:
        loadgradefont.draw(1160,325,'B',(255,255,255))
    else:
        loadgradefont.draw(1160,325,'C',(255,255,255))
    update_canvas()

def update():
    pass
def pause():
    pass
def resume():
    pass

def get_imformation(hp,death_mouse,death_wildboar,death_ironboar):
    global received_hp,received_kill_mouse,received_kill_wildboar,received_kill_ironboar
    received_hp=hp
    received_kill_mouse=death_mouse
    received_kill_wildboar=death_wildboar
    received_kill_ironboar=death_ironboar
