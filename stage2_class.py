# __author__ = 'Administrator'
import random
import json
from pico2d import *
from game_stage2 import *
import game_stage1
received_hp = 0


class Pause:
    image=None
    def __init__(self):
        if Pause.image == None:
            Pause.image = load_image('resource\\pause.png')
        self.pressed=False
    def draw(self):
        if self.pressed == True:
            self.image.clip_draw_to_origin(0,0,1366,350,300,300,1000,300)

class Minimap:
    image=None
    def __init__(self):
        if Minimap.image == None:
            Minimap.image = load_image('resource\\stage2_minimap.png')
    def draw(self):
        self.image.clip_draw_to_origin(0,0,1000,60,300,700,1030,60)

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
    minimap_scroll=0.0
    def __init__(self):
        self.image = load_image('resource\\tileblock_stage2.png')
        self.slide=0
    def draw(self):
        self.image.clip_draw_to_origin(self.slide,0,1600,100,0,300,1600-self.slide,100)
        self.image.clip_draw_to_origin(0,0,self.slide,100,1600-self.slide,300,self.slide,100)
    def update(self,frame_time):
        distance=self.RUN_SPEED_PPS*frame_time
        self.slide+=int(distance)
        self.minimap_scroll+=distance
        self.slide%=1600

class Monster_mouse_upside:
    image=None
    PIXEL_PER_METER = (160.0/1.0)    # 160 pixel 100 cm
    RUN_SPEED_KMPH = 20.0           # KM / HOUR
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    def __init__(self):
        if Monster_mouse_upside.image == None:
            self.image=load_image('resource\\monster1move.png')
        self.x=None
        self.y=None
        self.crush=False
        self.total_frames=0.0
        self.frame=random.randint(0,5)
    def draw(self):
        self.image.clip_draw_to_origin(55*self.frame,0,55,43,self.x,self.y,80,60)
    def update(self,frame_time):
        distance=self.RUN_SPEED_PPS*frame_time
        self.total_frames+=self.FRAMES_PER_ACTION * self.ACTION_PER_TIME*frame_time
        self.frame=int((self.total_frames)%6)
        self.x-=int(distance)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x , self.y , self.x + 80, self.y + 60

class Monster_mouse_downside:
    image=None
    PIXEL_PER_METER = (160.0/1.0)    # 160 pixel 100 cm
    RUN_SPEED_KMPH = 20.0           # KM / HOUR
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    def __init__(self):
        if Monster_mouse_downside.image == None:
            self.image=load_image('resource\\monster1move_reverse.png')
        self.x=None
        self.y=None
        self.crush=False
        self.total_frames=0.0
        self.frame=random.randint(0,5)
    def draw(self):
        self.image.clip_draw_to_origin(55*self.frame,0,55,43,self.x,self.y,80,60)
    def update(self,frame_time):
        distance=self.RUN_SPEED_PPS*frame_time
        self.total_frames+=self.FRAMES_PER_ACTION * self.ACTION_PER_TIME*frame_time
        self.frame=int((self.total_frames)%6)
        self.x-=int(distance)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x , self.y , self.x + 80, self.y + 60

class Monster_wildboar_upside:
    RUN,HIT,DEATH=0,1,2
    PIXEL_PER_METER = (160.0/1.0)    # 160 pixel 100 cm
    RUN_SPEED_KMPH = 20.0           # KM / HOUR
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION_RUN = 3
    FRAMES_PER_ACTION_HIT = 5
    FRAMES_PER_ACTION_DEATH = 3
    death_sound=None
    def handle_run(self,frame_time):
        distance=self.RUN_SPEED_PPS*frame_time
        self.total_frames+=self.FRAMES_PER_ACTION_RUN*self.ACTION_PER_TIME*frame_time
        self.run_frame=int(self.total_frames)%3
        # print(self.run_frame)
        self.x-=int(distance)

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

    def return_death_frame(self):
        return self.death_frame

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DEATH : handle_death
    }

    def __init__(self):
        self.x=None
        self.y=None
        self.run_frame,self.hit_frame,self.death_frame = (0,0,0)
        self.run = load_image('resource\\monster2move.png')
        self.hit = load_image('resource\\monster2hit.png')
        self.death = load_image('resource\\monster2death.png')
        self.crush=False
        self.state=self.RUN
        self.total_frames=0.0
        if Monster_wildboar_upside.death_sound==None:
            Monster_wildboar_upside.death_sound = load_wav('resource//sound//etc_wildboar_hit.wav')
            Monster_wildboar_upside.death_sound.set_volume(64)
    def draw(self):
        if self.state==0:
            self.run.clip_draw_to_origin(73*self.run_frame,0,73,52,self.x,self.y,120,100)
        elif self.state==1:
            self.hit.clip_draw_to_origin(0,0,73,52,self.x,self.y,120,100)
        elif self.state==2:
            self.death.clip_draw_to_origin(75*self.death_frame%2,0,75,46,self.x,self.y,120,100)

    def update(self,frame_time):
        self.handle_state[self.state](self,frame_time)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x , self.y , self.x + 120, self.y + 100

class Monster_wildboar_downside:
    RUN,HIT,DEATH=0,1,2
    PIXEL_PER_METER = (160.0/1.0)    # 160 pixel 100 cm
    RUN_SPEED_KMPH = 20.0           # KM / HOUR
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION_RUN = 3
    FRAMES_PER_ACTION_HIT = 5
    FRAMES_PER_ACTION_DEATH = 3
    death_sound=None
    def handle_run(self,frame_time):
        distance=self.RUN_SPEED_PPS*frame_time
        self.total_frames+=self.FRAMES_PER_ACTION_RUN*self.ACTION_PER_TIME*frame_time
        self.run_frame=int(self.total_frames)%3
        # print(self.run_frame)
        self.x-=int(distance)

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

    def return_death_frame(self):
        return self.death_frame

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DEATH : handle_death
    }

    def __init__(self):
        self.x=None
        self.y=None
        self.run_frame,self.hit_frame,self.death_frame = (0,0,0)
        self.run = load_image('resource\\monster2move_reverse.png')
        self.hit = load_image('resource\\monster2hit_reverse.png')
        self.death = load_image('resource\\monster2death_reverse.png')
        self.crush=False
        self.state=self.RUN
        self.total_frames=0.0
        if Monster_wildboar_downside.death_sound==None:
            Monster_wildboar_downside.death_sound = load_wav('resource//sound//etc_wildboar_hit.wav')
            Monster_wildboar_downside.death_sound.set_volume(64)
    def draw(self):
        if self.state==0:
            self.run.clip_draw_to_origin(73*self.run_frame,0,73,52,self.x,self.y,120,100)
        elif self.state==1:
            self.hit.clip_draw_to_origin(0,0,73,52,self.x,self.y,120,100)
        elif self.state==2:
            self.death.clip_draw_to_origin(75*self.death_frame%2,0,75,46,self.x,self.y,120,100)

    def update(self,frame_time):
        self.handle_state[self.state](self,frame_time)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x , self.y , self.x + 120, self.y + 100


class Monster_ironboar_upside:
    RUN,HIT,DEATH=0,1,2
    PIXEL_PER_METER = (160.0/1.0)    # 160 pixel 100 cm
    RUN_SPEED_KMPH = 20.0           # KM / HOUR
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    RUN_KNOCKBACK_KMPH = 60.0
    RUN_KNOCKBACK_MPM =  (RUN_KNOCKBACK_KMPH * 1000.0/60.0)
    RUN_KNOCKBACK_MPS = RUN_KNOCKBACK_MPM/60.0
    RUN_KNOCKBACK_PPS = (RUN_KNOCKBACK_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION_RUN = 2
    FRAMES_PER_ACTION_HIT = 5
    FRAMES_PER_ACTION_DEATH = 4

    hit_sound=None
    death_sound=None

    def handle_run(self,frame_time):
        distance=self.RUN_SPEED_PPS*frame_time
        self.total_frames+=self.FRAMES_PER_ACTION_RUN*self.ACTION_PER_TIME*frame_time
        self.run_frame=int(self.total_frames)%2
        self.x-=int(distance)

    def handle_hit(self,frame_time):
        self.total_frames+=self.FRAMES_PER_ACTION_HIT*self.ACTION_PER_TIME*frame_time
        distance=self.RUN_KNOCKBACK_PPS*frame_time
        self.hit_frame=int(self.total_frames)
        if self.hp==1:
            self.x+=int(distance/(self.hit_frame+1))
        if self.hit_frame==2  and self.hp==0:
            self.state=self.DEATH
            self.death_sound.play()
            self.hit_frame=0
            self.total_frames=0
            self.death_frame=0
        elif self.hit_frame==3 and self.hp==1:
            self.state=self.RUN
            self.run_frame=0
            self.total_frames=0
            self.hit_frame=0

    def handle_death(self,frame_time):
        self.total_frames+=self.FRAMES_PER_ACTION_DEATH*self.ACTION_PER_TIME*frame_time
        self.death_frame=int(self.total_frames)

    def return_death_frame(self):
        return self.death_frame

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DEATH : handle_death
    }

    def __init__(self):
        self.x=800
        self.y=495
        self.run_frame,self.hit_frame,self.death_frame = (0,0,0)
        self.run = load_image('resource\\monster3move.png')
        self.hit = load_image('resource\\monster3hit.png')
        self.death = load_image('resource\\monster3death.png')
        self.crush=False
        self.hp=2
        self.state=self.RUN
        self.total_frames=0.0
        if Monster_ironboar_upside.death_sound==None:
            Monster_ironboar_upside.death_sound = load_wav('resource//sound//etc_wildboar_hit.wav')
            Monster_ironboar_upside.death_sound.set_volume(64)
        if Monster_ironboar_upside.hit_sound==None:
            Monster_ironboar_upside.hit_sound = load_wav('resource//sound//etc_ironboar_hit.wav')
            Monster_ironboar_upside.hit_sound.set_volume(64)
    def draw(self):
        if self.state==0:
            self.run.clip_draw_to_origin(70*self.run_frame,0,70,65,self.x,self.y,120,100)
        elif self.state==1:
            self.hit.clip_draw_to_origin(0,0,75,68,self.x,self.y,120,100)
        elif self.state==2:
            self.death.clip_draw_to_origin(70*self.death_frame%2,0,70,63,self.x,self.y,120,100)

    def update(self,frame_time):
        self.handle_state[self.state](self,frame_time)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x , self.y , self.x + 120, self.y + 100

class Monster_ironboar_downside:
    RUN,HIT,DEATH=0,1,2
    PIXEL_PER_METER = (160.0/1.0)    # 160 pixel 100 cm
    RUN_SPEED_KMPH = 20.0           # KM / HOUR
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    RUN_KNOCKBACK_KMPH = 60.0
    RUN_KNOCKBACK_MPM =  (RUN_KNOCKBACK_KMPH * 1000.0/60.0)
    RUN_KNOCKBACK_MPS = RUN_KNOCKBACK_MPM/60.0
    RUN_KNOCKBACK_PPS = (RUN_KNOCKBACK_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION_RUN = 2
    FRAMES_PER_ACTION_HIT = 5
    FRAMES_PER_ACTION_DEATH = 4

    hit_sound=None
    death_sound=None

    def handle_run(self,frame_time):
        distance=self.RUN_SPEED_PPS*frame_time
        self.total_frames+=self.FRAMES_PER_ACTION_RUN*self.ACTION_PER_TIME*frame_time
        self.run_frame=int(self.total_frames)%2
        self.x-=int(distance)

    def handle_hit(self,frame_time):
        self.total_frames+=self.FRAMES_PER_ACTION_HIT*self.ACTION_PER_TIME*frame_time
        distance=self.RUN_KNOCKBACK_PPS*frame_time
        self.hit_frame=int(self.total_frames)
        if self.hp==1:
            self.x+=int(distance/(self.hit_frame+1))
        if self.hit_frame==2  and self.hp==0:
            self.state=self.DEATH
            self.death_sound.play()
            self.hit_frame=0
            self.total_frames=0
            self.death_frame=0
        elif self.hit_frame==3 and self.hp==1:
            self.state=self.RUN
            self.run_frame=0
            self.total_frames=0
            self.hit_frame=0

    def handle_death(self,frame_time):
        self.total_frames+=self.FRAMES_PER_ACTION_DEATH*self.ACTION_PER_TIME*frame_time
        self.death_frame=int(self.total_frames)

    def return_death_frame(self):
        return self.death_frame

    handle_state = {
        RUN : handle_run,
        HIT : handle_hit,
        DEATH : handle_death
    }

    def __init__(self):
        self.x=800
        self.y=495
        self.run_frame,self.hit_frame,self.death_frame = (0,0,0)
        self.run = load_image('resource\\monster3move_reverse.png')
        self.hit = load_image('resource\\monster3hit_reverse.png')
        self.death = load_image('resource\\monster3death_reverse.png')
        self.crush=False
        self.hp=2
        self.state=self.RUN
        self.total_frames=0.0
        if Monster_ironboar_downside.death_sound==None:
            Monster_ironboar_downside.death_sound = load_wav('resource//sound//etc_wildboar_hit.wav')
            Monster_ironboar_downside.death_sound.set_volume(64)
        if Monster_ironboar_downside.hit_sound==None:
            Monster_ironboar_downside.hit_sound = load_wav('resource//sound//etc_ironboar_hit.wav')
            Monster_ironboar_downside.hit_sound.set_volume(64)
    def draw(self):
        if self.state==0:
            self.run.clip_draw_to_origin(70*self.run_frame,0,70,65,self.x,self.y,120,100)
        elif self.state==1:
            self.hit.clip_draw_to_origin(0,0,75,68,self.x,self.y,120,100)
        elif self.state==2:
            self.death.clip_draw_to_origin(70*self.death_frame%2,0,70,63,self.x,self.y,120,100)

    def update(self,frame_time):
        self.handle_state[self.state](self,frame_time)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x , self.y , self.x + 120, self.y + 100

class Character_upside:
    global tile
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

    run_sound=None
    jump_sound=None
    attack_sound=None
    hp_sound=None

    #s=v0t + 1/2a t^2
    def handle_run(self,frame_time):
        if self.run_frame==0:
            self.run_sound.play()
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
        # print(self.jump_frame,self.y)
        self.total_frames+=self.FRAMES_PER_ACTION_JUMP*self.ACTION_PER_TIME_JUMP*frame_time
        self.jump_frame=int(self.total_frames)
        if self.jump_frame>=7 :
            self.state=self.RUN
            self.run_frame=0
            self.y=460

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
        global re_hp
        self.x, self.y = 160, 460
        self.run_frame,self.jump_frame,self.attack_frame = (0,0,0)
        self.run = load_image('resource\\character1run.png')
        self.jump = load_image('resource\\character1jump.png')
        self.attack = load_image('resource\\character1attack.png')
        self.hpbar=load_image('resource\\hpbar.png')
        self.keycheckup,self.keycheckdown,self.keycheckleft,self.keycheckright=(False,False,False,False)
        self.state=self.RUN
        self.hp = received_hp
        self.total_frames=0.0
        if Character_upside.run_sound==None:
            Character_upside.run_sound = load_wav('resource//sound//etc_character_run.wav')
            Character_upside.run_sound.set_volume(64)
        if Character_upside.jump_sound==None:
            Character_upside.jump_sound = load_wav('resource//sound//etc_character_jump.wav')
            Character_upside.jump_sound.set_volume(64)
        if Character_upside.attack_sound==None:
            Character_upside.attack_sound = load_wav('resource//sound//etc_character_attack.wav')
            Character_upside.attack_sound.set_volume(64)
        if Character_upside.hp_sound==None:
            Character_upside.hp_sound = load_wav('resource//sound//etc_character_hp.wav')
            Character_upside.hp_sound.set_volume(64)

    def draw(self):
        if self.state==self.RUN:
            self.run.clip_draw(self.run_frame*160, 0, 160, 135, self.x, self.y)
        elif self.state==self.JUMP:
            self.jump.clip_draw(self.jump_frame*130, 0, 130, 165, self.x, self.y+10)
        elif self.state==self.ATTACK:
            self.attack.clip_draw(self.attack_frame*220, 0, 220, 170, self.x+20, self.y+20)
        self.hpbar.clip_draw_to_origin(0,0,self.hp*27,15,50,850,self.hp*27,15)
    def draw_minimap_character(self,tile):
        self.run.clip_draw_to_origin(int(self.total_frames%6)*160, 0, 160, 135,300+tile.minimap_scroll/17.5,717, 40, 40)
    def draw_bb_body(self):
        draw_rectangle(*self.get_bb_body())
    def draw_bb_weapon(self):
        draw_rectangle(*self.get_bb_weapon())
    def get_bb_body(self):
        if(self.state==self.RUN):
            return self.x-80 , self.y-65 , self.x , self.y
        elif(self.state==self.JUMP):
            return self.x-70 , self.y-70 , self.x+20 , self.y
        elif(self.state==self.ATTACK):
            return self.x-80 , self.y-65 , self.x , self.y
    def get_bb_weapon(self):
        if(self.state==self.ATTACK):
            return self.x+70 , self.y-50 , self.x+140 , self.y+20

class Character_downside:
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

    run_sound=None
    jump_sound=None
    attack_sound=None

    def handle_run(self,frame_time):
        if self.run_frame==0:
            self.run_sound.play()
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
        self.y-=self.JUMP_SPEED_MPS-self.GRAVITY/2*(2*self.jump_frame-1)
        # print(self.jump_frame,self.y)
        self.total_frames+=self.FRAMES_PER_ACTION_JUMP*self.ACTION_PER_TIME_JUMP*frame_time
        self.jump_frame=int(self.total_frames)
        if self.jump_frame>=7 :
            self.state=self.RUN
            self.run_frame=0
            self.y=230

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
        self.x, self.y = 160, 230
        self.run_frame,self.jump_frame,self.attack_frame = (0,0,0)
        self.run = load_image('resource\\character2run.png')
        self.jump = load_image('resource\\character2jump.png')
        self.attack = load_image('resource\\character2attack.png')
        self.keycheckup,self.keycheckdown,self.keycheckleft,self.keycheckright=(False,False,False,False)
        self.state=self.RUN
        self.total_frames=0.0
        if Character_downside.run_sound==None:
            Character_downside.run_sound = load_wav('resource//sound//etc_character_run.wav')
            Character_downside.run_sound.set_volume(64)
        if Character_downside.jump_sound==None:
            Character_downside.jump_sound = load_wav('resource//sound//etc_character_jump.wav')
            Character_downside.jump_sound.set_volume(64)
        if Character_downside.attack_sound==None:
            Character_downside.attack_sound = load_wav('resource//sound//etc_character_attack.wav')
            Character_downside.attack_sound.set_volume(64)

    def draw(self):
        if self.state==self.RUN:
            self.run.clip_draw(self.run_frame*160, 0, 160, 135, self.x, self.y)
        elif self.state==self.JUMP:
            self.jump.clip_draw(self.jump_frame*130, 0, 130, 165, self.x, self.y+10)
        elif self.state==self.ATTACK:
            self.attack.clip_draw(self.attack_frame*220, 0, 220, 170, self.x+20, self.y-20)

    def draw_bb_body(self):
        draw_rectangle(*self.get_bb_body())
    def draw_bb_weapon(self):
        draw_rectangle(*self.get_bb_weapon())
    def get_bb_body(self):
        if(self.state==self.RUN):
            return self.x-80 , self.y , self.x , self.y+65
        elif(self.state==self.JUMP):
            return self.x-70 , self.y+20 , self.x+20 , self.y+90
        elif(self.state==self.ATTACK):
            return self.x-80 , self.y , self.x , self.y+65
    def get_bb_weapon(self):
        if(self.state==self.ATTACK):
            return self.x+70 , self.y-15 , self.x+140 , self.y+55

def get_hp(stage1_hp):
    global received_hp
    received_hp = stage1_hp
    pass