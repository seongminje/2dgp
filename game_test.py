# direction으로 연속이동

from pico2d import *
import math
import os

def handle_events():
    global running
    global characterx
    global charactery
    global direction
    events=get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                direction=1
            elif event.key == SDLK_DOWN:
                direction=2
            elif event.key == SDLK_LEFT:
                direction=3
            elif event.key == SDLK_RIGHT:
                direction=4
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
                direction=0
    pass

open_canvas(1600,900)
os.chdir('c:/2dgp/2dgp/resource')
tile = load_image('tile1.png')
character = load_image('character1run.png')
monster1 = load_image('monster1move.png')
running = True
frame=0
characterx=70
charactery=160
monster1x=1500
direction=0

while(characterx<1500 and running):
    clear_canvas()
    for i in range(0,18):
        tile.clip_draw(14,176,90,60,45+i*90,30)
    character.clip_draw(frame*160,0,160,135,characterx,charactery)
    monster1.clip_draw(frame*55,0,55,43,monster1x,80)

    monster1x-=10
    if monster1x<35:
        monster1x=1600
    handle_events()
    if direction==1:
        charactery=charactery+10
    elif direction==2:
        charactery=charactery-10
    elif direction==4:
        characterx=characterx+10
    elif direction==3:
        characterx=characterx-10
    update_canvas()
    frame=(frame+1)%6
    delay(0.05)

close_canvas()

