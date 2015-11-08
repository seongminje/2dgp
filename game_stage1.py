import random
import json
from pico2d import *
import game_framework
import game_title

stage1bg = None
main_character = None
tile = None
monster_mouseset = None
monster_wildboar = None

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

def create_monster_mouseset():
    monster_mouse_data_file= open('resource\\jsons\\stage1_monster_mouse_data.txt','r')
    monster_mouse_data = json.load(monster_mouse_data_file)
    monster_mouse_data_file.close()
    monster_mouseset=[]
    for num in monster_mouse_data:
        monster_mouse = Monster_mouse()
        monster_mouse.num = num
        monster_mouse.x=monster_mouse_data[num]['x']
        monster_mouse.y=monster_mouse_data[num]['y']
        monster_mouseset.append(monster_mouse)
    return monster_mouseset

def enter():
    global main_character,tile,stage1bg,monster_mouseset,monster_wildboar
    main_character=Character()
    tile=Tile()
    stage1bg=Background()
    monster_mouseset = create_monster_mouseset()
    monster_wildboar = Monster_wildboar()

def exit():
    global main_character,tile,stage1bg,monster_mouseset,monster_wildboar
    del(main_character)
    del(tile)
    del(stage1bg)
    del(monster_mouseset)
    del(monster_wildboar)

def pause():
    pass

def resume():
    pass

def handle_events():
    global main_character
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and main_character.state==main_character.RUN:
            if event.key == SDLK_UP:
                main_character.keycheckup = True
            elif event.key == SDLK_DOWN:
                main_character.keycheckdown = True
            elif event.key == SDLK_LEFT:
                main_character.keycheckleft = True
            elif event.key == SDLK_RIGHT:
                main_character.keycheckright = True
            elif event.key == SDLK_z:
                main_character.state=1
                main_character.jump_frame=0
            elif event.key == SDLK_x:
                main_character.state=2
                main_character.attack_frame=0
            elif event.key==SDLK_ESCAPE:
                game_framework.change_state(game_title)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                main_character.keycheckup = False
            elif event.key == SDLK_DOWN:
                main_character.keycheckdown = False
            elif event.key == SDLK_LEFT:
                main_character.keycheckleft = False
            elif event.key == SDLK_RIGHT:
                main_character.keycheckright = False

def update():
    global monster_mouseset,main_character,monster_wildboar
    main_character.update()
    for monster_mouse in monster_mouseset:
        if main_character.x in range(monster_mouse.x, monster_mouse.x+80) and main_character.y-65 in range(monster_mouse.y-30, monster_mouse.y+50) and monster_mouse.crush==False:
            main_character.hp-=1
            monster_mouse.crush=True
    if main_character.state==main_character.ATTACK and main_character.x+90 in range(monster_wildboar.x-20,monster_wildboar.x+40):
        monster_wildboar.state=monster_wildboar.HIT
        monster_wildboar.crush=True
    elif main_character.x in range(monster_wildboar.x-30,monster_wildboar.x+20) and monster_wildboar.crush==False:
        main_character.hp-=1
        monster_wildboar.crush=True
    tile.update()
    stage1bg.update()
    for monster_mouse in monster_mouseset:
        monster_mouse.update()
    monster_wildboar.update()
    if(main_character.hp==0):
        game_framework.change_state(game_title)

    delay(0.03)

def draw():
    clear_canvas()
    stage1bg.draw()
    tile.draw()
    for monster_mouse in monster_mouseset:
        monster_mouse.draw()
    main_character.draw()
    monster_wildboar.draw()
    update_canvas()