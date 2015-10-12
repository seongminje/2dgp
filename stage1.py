import random
from pico2d import *
import game_framework
import title

name = "stage1"

character = None
tile = None
#font = None

class Tile:
    def __init__(self):
        self.image = load_image('resource\\tile1.png')

    def draw(self):
        for i in range(0,18):
            self.image.clip_draw(14,176,90,60,45+i*90,30)

class Character:
    def __init__(self):
        self.x, self.y = 160, 160
        self.frame = 0
        self.run = load_image('resource\\character1run.png')
        self.jump = load_image('resource\\character1jump.png')
        self.attack = load_image('resource\\character1attack.png')

    def update(self):
        self.frame = (self.frame + 1) % 6


    def draw(self):
        self.run.clip_draw(self.frame*160, 0, 160, 135, self.x, self.y)


def enter():
    global character1,tile
    character1=Character()
    tile=Tile()

def exit():
    global character1,tile
    del(character1)
    del(tile)

def pause():
    pass

def resume():
    pass

def handle_events():

    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.change_state(title)


def update():
    character1.update()

def draw():
    clear_canvas()
    character1.draw()
    tile.draw()
    delay(0.05)
    update_canvas()

"""
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

#open_canvas(1600,900)

os.chdir('c:/2dgp/2dgp/resource')
tile = load_image('tile1.png')
character = load_image('character1run.png')
monster1 = load_image('monster1move.png')
running = True
frame=0
frame2=0
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
    character.clip_draw(frame*160,0,160,135,characterx,charactery)
    monster1.clip_draw(frame2*55,0,55,43,monster1x,80)
    #monster1.clip_draw_to_origin(frame*70,254,70,46,monster1x,80,50,43)

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
    frame2=(frame2+1)%6
    delay(0.05)

close_canvas()

"""