# __author__ = 'Administrator'
import random
import json
from pico2d import *
from game_stage1 import  *

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

class Monster_mouse:
    image=None
    def __init__(self):
        if Monster_mouse.image == None:
            self.image=load_image('resource\\monster1move.png')
        self.x=None
        self.y=None
        self.crush=False
        self.frame=random.randint(0,5)
    def draw(self):
        self.image.clip_draw_to_origin(55*self.frame,0,55,43,self.x,self.y,80,60)
    def update(self):
        self.frame=(self.frame+1)%6
        self.x-=10
        # if self.x <0:
        #     self.x=1600

class Monster_wildboar:
    RUN,HIT,DEATH=0,1,2

    def handle_run(self):
        self.run_frame = (self.run_frame + 1) % 3
        self.x-=20

    def handle_hit(self):
        self.hit_frame+=1
        if self.hit_frame==5 :
            self.state=self.DEATH
            self.hit_frame=0
            self.death_frame=0


    def handle_death(self):
        self.death_frame+=self.halfframe
        self.halfframe=(self.halfframe+1)%2
        if self.death_frame==3:
            self.state=self.RUN
            self.run_frame=0
            self.halfframe=0

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DEATH : handle_death
    }

    def __init__(self):
        self.x=800
        self.y=95
        self.run_frame,self.hit_frame,self.death_frame = (0,0,0)
        self.run = load_image('resource\\monster2move.png')
        self.hit = load_image('resource\\monster2hit.png')
        self.death = load_image('resource\\monster2death.png')
        self.crush=False
        self.halfframe=0;
        self.state=self.RUN

    def draw(self):
        if self.state==0:
            self.run.clip_draw_to_origin(73*self.run_frame,0,73,52,self.x,self.y,100,80)
        elif self.state==1:
            self.hit.clip_draw_to_origin(0,0,73,52,self.x,self.y,100,80)
        elif self.state==2:
            self.death.clip_draw_to_origin(75*self.death_frame%2,0,75,46,self.x,self.y,100,80)

    def update(self):
        self.handle_state[self.state](self)


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
        self.y-=(self.jump_frame-3)*10
        self.jump_frame+=self.halfframe
        self.halfframe=(self.halfframe+1)%2
        if self.jump_frame==7 :
            self.state=self.RUN
            self.run_frame=0
            self.halfframe=0


    def handle_attack(self):
        self.attack_frame+=self.halfframe
        self.halfframe=(self.halfframe+1)%2
        if self.attack_frame==6 :
            self.state=self.RUN
            self.run_frame=0
            self.halfframe=0

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
        self.halfframe=0;

    def draw(self):
        if self.state==0:
            self.run.clip_draw(self.run_frame*160, 0, 160, 135, self.x, self.y)
        elif self.state==1:
            self.jump.clip_draw(self.jump_frame*130, 0, 130, 165, self.x, self.y+10)
        elif self.state==2:
            self.attack.clip_draw(self.attack_frame*220, 0, 220, 170, self.x+20, self.y+20)
        self.hpbar.clip_draw_to_origin(0,0,self.hp*27,15,50,850,self.hp*27,15)