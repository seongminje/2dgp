import random
from pico2d import *
import game_framework
import title

name = "stage1"

bg = None
character = None
tile = None
monster1 = None

class Background:
    image=None
    def __init__(self):
        #self.image = load_image('resource\\BG1.png')
        self.slide = 0
        if Background.image == None:
            Background.image = load_image('resource\\BG1.png')
    def draw(self):
        self.image.clip_draw_to_origin(self.slide,0,1600,900,0,0,1600-self.slide,900)
        self.image.clip_draw_to_origin(0,0,self.slide,900,1600-self.slide,0,self.slide,900)
    def update(self):
        self.slide+=5
        self.slide%=1600

class Tile:
    def __init__(self):
        self.image = load_image('resource\\tileblock.png')
        self.slide=0
    def draw(self):
        self.image.clip_draw_to_origin(self.slide,0,1600,100,0,0,1600-self.slide,100)
        self.image.clip_draw_to_origin(0,0,self.slide,100,1600-self.slide,0,self.slide,100)
    def update(self):
        self.slide+=15
        self.slide%=1600

class Monster1:
    image=None
    def __init__(self):
        if Monster1.image == None:
            self.image=load_image('resource\\monster1move.png')
        self.x=1600
        self.y=95
        self.frame=0
    def draw(self):
        self.image.clip_draw_to_origin(55*self.frame,0,55,43,self.x,self.y,80,60)
    def update(self):
        self.frame=(self.frame+1)%6
        self.x-=25
        if self.x <0:
            self.x=1600

class Character:
    RUN,JUMP,ATTACK=0,1,2

    def handle_run(self):
        self.run_frame = (self.run_frame + 1) % 6
        if self.keycheckup==True:
            self.y+=10
        if self.keycheckdown==True:
            self.y-=10
        if self.keycheckleft==True:
            self.x-=10
        if self.keycheckright==True:
            self.x+=10

    def handle_jump(self):
        self.y-=(self.jump_frame-3)*20
        self.jump_frame+=1
        # delay(0.03)
        if self.jump_frame==7 :
            self.state=self.RUN
            self.run_frame=0

    def handle_attack(self):
        self.attack_frame+=1
        if self.attack_frame==6 :
            self.state=self.RUN
            self.run_frame=0

    handle_state = {
        RUN : handle_run,
        JUMP : handle_jump,
        ATTACK : handle_attack
    }
    def update(self):
        self.handle_state[self.state](self)  # if가 없어짐 -> 처리속도,수정이 빠름

    def __init__(self):
        self.x, self.y = 160, 160
        self.run_frame,self.jump_frame,self.attack_frame = (0,0,0)
        self.run = load_image('resource\\character1run.png')
        self.jump = load_image('resource\\character1jump.png')
        self.attack = load_image('resource\\character1attack.png')
        self.hpbar=load_image('resource\\hpbar.png')
        self.keycheckup,self.keycheckdown,self.keycheckleft,self.keycheckright=(False,False,False,False)
        self.state=self.RUN
        self.hp=10

    def draw(self):
        if self.state==0:
            self.run.clip_draw(self.run_frame*160, 0, 160, 135, self.x, self.y)
        elif self.state==1:
            self.jump.clip_draw(self.jump_frame*130, 0, 130, 165, self.x, self.y+10)
        elif self.state==2:
            self.attack.clip_draw(self.attack_frame*220, 0, 220, 170, self.x+20, self.y+20)
        self.hpbar.clip_draw_to_origin(0,0,self.hp*27,15,50,850,self.hp*27,15)

def enter():
    global character1,tile,bg,monster1
    character1=Character()
    tile=Tile()
    bg=Background()
    monster1=Monster1()

def exit():
    global character1,tile,bg,monster1
    del(character1)
    del(tile)
    del(bg)
    del(monster1)

def pause():
    pass

def resume():
    pass

def handle_events():
    global character1
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and character1.state==character1.RUN:
            if event.key == SDLK_UP:
                character1.keycheckup = True
            elif event.key == SDLK_DOWN:
                character1.keycheckdown = True
            elif event.key == SDLK_LEFT:
                character1.keycheckleft = True
            elif event.key == SDLK_RIGHT:
                character1.keycheckright = True
            elif event.key == SDLK_z:
                character1.state=1
                character1.jump_frame=0
            elif event.key == SDLK_x:
                character1.state=2
                character1.attack_frame=0
            elif event.key==SDLK_ESCAPE:
                game_framework.change_state(title)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                character1.keycheckup = False
            elif event.key == SDLK_DOWN:
                character1.keycheckdown = False
            elif event.key == SDLK_LEFT:
                character1.keycheckleft = False
            elif event.key == SDLK_RIGHT:
                character1.keycheckright = False

def update():
    character1.update()
    tile.update()
    bg.update()
    monster1.update()
    delay(0.03)

def draw():
    clear_canvas()
    bg.draw()
    tile.draw()
    monster1.draw()
    character1.draw()


    update_canvas()