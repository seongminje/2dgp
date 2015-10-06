from pico2d import *
import math
import os

def handle_events():
    global running
    global characterx
    global charactery
    global keycheckup
    global keycheckdown
    global keycheckright
    global keycheckleft
    events=get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                keycheckup=True
            elif event.key == SDLK_DOWN:
                keycheckdown = True
            elif event.key == SDLK_LEFT:
                keycheckleft = True
            elif event.key == SDLK_RIGHT:
                keycheckright = True
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                keycheckup = False
            elif event.key == SDLK_DOWN:
                keycheckdown = False
            elif event.key == SDLK_LEFT:
                keycheckleft = False
            elif event.key == SDLK_RIGHT:
                keycheckright = False
    pass

open_canvas(1600,900)
os.chdir('c:/2dgp/2dgp/resource')
tile = load_image('tile1.png')
character = load_image('R_Monster2.png')
monster1 = load_image('monster1.png')
running = True
frame=0
characterx=70
charactery=160
monster1x=1500
keycheckup = False
keycheckdown = False
keycheckright = False
keycheckleft = False


while(characterx<1500 and running):
    clear_canvas()
    for i in range(0,18):
        tile.clip_draw(14,176,90,60,45+i*90,30)
    character.clip_draw(frame*170,400,170,200,characterx,charactery)
    monster1.clip_draw(frame*70,254,70,46,monster1x,80)

    monster1x-=10
    if monster1x<35:
        monster1x=1600
    handle_events()
    if keycheckup == True:
        charactery=charactery+10
    elif keycheckdown == True:
        charactery=charactery-10
    elif keycheckright == True:
        characterx=characterx+10
    elif keycheckleft == True:
        characterx=characterx-10
    update_canvas()
    frame=(frame+1)%6
    delay(0.05)

close_canvas()

