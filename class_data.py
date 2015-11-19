# __author__ = 'Administrator'
import random
import json
from pico2d import *
from game_stage1 import  *

class Background:
    image=None
    PIXEL_PER_METER = (160.0/1.0)    # 160 pixel 100 cm
    RUN_SPEED_KMPH = 5.0           # KM / HOUR
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        #self.image = load_image('resource\\BG1.png')
        self.slide = 0
        if Background.image == None:
            Background.image = load_image('resource\\BG2.png')
    def draw(self):
        self.image.clip_draw_to_origin(self.slide,0,1600,900,0,0,1600-self.slide,900)
        self.image.clip_draw_to_origin(0,0,self.slide,900,1600-self.slide,0,self.slide,900)
    def update(self,frame_time):
        distance=self.RUN_SPEED_PPS*frame_time
        self.slide+=int(distance)
        self.slide%=1600

class Tile:
    image=None
    PIXEL_PER_METER = (160.0/1.0)    # 160 pixel 100 cm
    RUN_SPEED_KMPH = 10.0           # KM / HOUR
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        self.image = load_image('resource\\tileblock.png')
        self.slide=0
    def draw(self):
        self.image.clip_draw_to_origin(self.slide,0,1600,100,0,0,1600-self.slide,100)
        self.image.clip_draw_to_origin(0,0,self.slide,100,1600-self.slide,0,self.slide,100)
    def update(self,frame_time):
        distance=self.RUN_SPEED_PPS*frame_time
        self.slide+=int(distance)
        self.slide%=1600

class Monster_mouse:
    image=None
    PIXEL_PER_METER = (160.0/1.0)    # 160 pixel 100 cm
    RUN_SPEED_KMPH = 15.0           # KM / HOUR
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    def __init__(self):
        if Monster_mouse.image == None:
            self.image=load_image('resource\\monster1move.png')
        self.x=None
        self.y=None
        self.crush=False
        self.total_frames=0.0
        self.frame=random.randint(0,5)
    def draw(self):
        self.image.clip_draw_to_origin(55*self.frame,0,55,43,self.x,self.y,60,40)
    def update(self,frame_time):
        distance=self.RUN_SPEED_PPS*frame_time
        self.total_frames+=self.FRAMES_PER_ACTION * self.ACTION_PER_TIME*frame_time
        self.frame=int((self.total_frames)%6)
        # print(self.frame)
        self.x-=int(distance)
        # if self.x <0:
        #     self.x=1600

class Monster_wildboar:
    RUN,HIT,DEATH=0,1,2
    PIXEL_PER_METER = (160.0/1.0)    # 160 pixel 100 cm
    RUN_SPEED_KMPH = 15.0           # KM / HOUR
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION_RUN = 3
    FRAMES_PER_ACTION_HIT = 5
    FRAMES_PER_ACTION_DEATH = 3
    def handle_run(self,frame_time):
        distance=self.RUN_SPEED_PPS*frame_time
        self.total_frames+=self.FRAMES_PER_ACTION_RUN*self.ACTION_PER_TIME*frame_time
        # self.run_frame=(self.run_frame+1)%3
        self.run_frame=int(self.total_frames)%3
        # print(self.run_frame)
        self.x-=int(distance)
        # self.run_frame = (self.run_frame + 1) % 3
        # self.x-=20

    def handle_hit(self,frame_time):
        self.total_frames+=self.FRAMES_PER_ACTION_HIT*self.ACTION_PER_TIME*frame_time
        self.hit_frame=int(self.total_frames)
        if self.hit_frame==2 :
            self.state=self.DEATH
            self.hit_frame=0
            self.total_frames=0
            self.death_frame=0


    def handle_death(self,frame_time):
        self.total_frames+=self.FRAMES_PER_ACTION_DEATH*self.ACTION_PER_TIME*frame_time
        self.death_frame=int(self.total_frames)
        ###############################
        if self.death_frame==3:
            self.state=self.RUN
            #################### .remove()
            self.run_frame=0
            self.death_frame=0

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
        self.state=self.RUN
        self.total_frames=0.0
    def draw(self):
        if self.state==0:
            self.run.clip_draw_to_origin(73*self.run_frame,0,73,52,self.x,self.y,100,80)
        elif self.state==1:
            self.hit.clip_draw_to_origin(0,0,73,52,self.x,self.y,100,80)
        elif self.state==2:
            self.death.clip_draw_to_origin(75*self.death_frame%2,0,75,46,self.x,self.y,100,80)

    def update(self,frame_time):
        self.handle_state[self.state](self,frame_time)


class Character:
    RUN,JUMP,ATTACK=0,1,2
    PIXEL_PER_METER = (160.0/1.0)    # 160 pixel 100 cm
    JUMP_SPEED_MPS = 23   # M / SEC
    JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)
    GRAVITY = 10

    TIME_PER_ACTION_RUN = 0.2
    ACTION_PER_TIME_RUN = 1.0/TIME_PER_ACTION_RUN
    TIME_PER_ACTION_JUMP = 0.5
    ACTION_PER_TIME_JUMP = 1.0/TIME_PER_ACTION_JUMP
    TIME_PER_ACTION_ATTACK = 0.4
    ACTION_PER_TIME_ATTACK = 1.0/TIME_PER_ACTION_ATTACK
    FRAMES_PER_ACTION_RUN = 6
    FRAMES_PER_ACTION_JUMP = 7
    FRAMES_PER_ACTION_ATTACK = 6
    #s=v0t + 1/2a t^2
    def handle_run(self,frame_time):
        self.total_frames+=self.FRAMES_PER_ACTION_RUN*self.ACTION_PER_TIME_RUN*frame_time
        self.run_frame=int(self.total_frames)%6
        # self.run_frame = (self.run_frame + 1) % 6
        if self.keycheckup==True:
            self.y+=10
        if self.keycheckdown==True:
            self.y-=10
        if self.keycheckleft==True:
            self.x-=10
        if self.keycheckright==True:
            self.x+=10

    def handle_jump(self,frame_time):
        self.y+=self.JUMP_SPEED_MPS-self.GRAVITY/2*(2*self.jump_frame-1)
        print(self.jump_frame,self.y)
        self.total_frames+=self.FRAMES_PER_ACTION_JUMP*self.ACTION_PER_TIME_JUMP*frame_time
        self.jump_frame=int(self.total_frames)
        if self.jump_frame>=7 :
            self.state=self.RUN
            self.run_frame=0
            # self.y=160

    def handle_attack(self,frame_time):
        self.total_frames+=self.FRAMES_PER_ACTION_ATTACK*self.ACTION_PER_TIME_ATTACK*frame_time
        self.attack_frame=int(self.total_frames)
        if self.attack_frame==6 :
            self.state=self.RUN
            self.run_frame=0

    handle_state = {
        RUN : handle_run,
        JUMP : handle_jump,
        ATTACK : handle_attack
    }

    def update(self,frame_time):
        self.handle_state[self.state](self,frame_time)  # if가 없어짐 -> 처리속도,수정이 빠름

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
        self.total_frames=0.0

    def draw(self):
        if self.state==0:
            self.run.clip_draw(self.run_frame*160, 0, 160, 135, self.x, self.y)
        elif self.state==1:
            self.jump.clip_draw(self.jump_frame*130, 0, 130, 165, self.x, self.y+10)
        elif self.state==2:
            self.attack.clip_draw(self.attack_frame*220, 0, 220, 170, self.x+20, self.y+20)
        self.hpbar.clip_draw_to_origin(0,0,self.hp*27,15,50,850,self.hp*27,15)