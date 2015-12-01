import random
import json
from pico2d import *
import game_framework
import game_title
import game_stage2
import stage2_class
# import game_pause
from stage1_class import *

stage1bg = None
main_character = None
tile = None
minimap=None
monster_mouseset = None
monster_wildboarset = None
current_time= get_time()
cheat_fastframe = False
stage1_bgm=None
cheat_etc= None
game_pause=None
# font=None
time_pause=0.0
time_resume=0.0
time_return=0.0


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

def create_monster_wildboarset():
    monster_wildboar_data_file= open('resource\\jsons\\stage1_monster_wildboar_data.txt','r')
    monster_wildboar_data = json.load(monster_wildboar_data_file)
    monster_wildboar_data_file.close()
    monster_wildboarset=[]
    for num in monster_wildboar_data:
        monster_wildboar = Monster_wildboar()
        monster_wildboar.num = num
        monster_wildboar.x=monster_wildboar_data[num]['x']
        monster_wildboar.y=monster_wildboar_data[num]['y']
        monster_wildboarset.append(monster_wildboar)
    return monster_wildboarset

def enter():
    global main_character,tile,stage1bg,monster_mouseset,monster_wildboarset,current_time,minimap,stage1_bgm,cheat_etc,game_pause#,font
    main_character=Character()
    tile=Tile()
    minimap=Minimap()
    stage1bg=Background()
    monster_mouseset = create_monster_mouseset()
    monster_wildboarset = create_monster_wildboarset()
    current_time = get_time()
    stage1_bgm=load_music('resource//sound//bgm_title.ogg')
    stage1_bgm.set_volume(32)
    stage1_bgm.repeat_play()
    cheat_etc=load_wav('resource//sound//etc_cheat.wav')
    cheat_etc.set_volume(0)
    cheat_etc.repeat_play()
    game_pause=Pause()
    # font=Font('resource//하얀분필B.ttf',20)

def exit():
    global main_character,tile,stage1bg,monster_mouseset,monster_wildboarset,minimap,stage1_bgm,cheat_etc,game_pause#,font
    del(main_character)
    del(tile)
    del(minimap)
    del(stage1bg)
    del(monster_mouseset)
    del(monster_wildboarset)
    del(stage1_bgm)
    del(cheat_etc)
    del(game_pause)
    # del(font)

def pause():
    pass

def resume():
    pass

def handle_events():
    global main_character,cheat_fastframe,cheat_etc,game_pause,time_pause,time_resume,time_return
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
            elif event.key == SDLK_a:
                main_character.state=1
                main_character.jump_frame=0
                main_character.total_frames=0
                main_character.jump_sound.play()
            elif event.key == SDLK_s:
                main_character.state=2
                main_character.attack_frame=0
                main_character.total_frames=0
                main_character.attack_sound.play()
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
        if event.type == SDL_KEYDOWN and event.key == SDLK_0:
            cheat_fastframe=True
            cheat_etc.set_volume(32)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            if game_pause.pressed == False:
                game_pause.pressed = True
                time_pause=get_time()
                stage1_bgm.set_volume(0)
            else:
                game_pause.pressed = False
                time_resume=get_time()
                time_return+=time_resume-time_pause
                stage1_bgm.set_volume(32)
        elif event.type == SDL_KEYUP and event.key == SDLK_0:
            cheat_fastframe=False
            cheat_etc.set_volume(0)

def update():
    if game_pause.pressed == False:
        global main_character,monster_mouseset,monster_wildboarset,current_time,frame_time,cheat_fastframe
        frame_time = get_time() - current_time-time_return
        current_time +=frame_time
        if cheat_fastframe == False:
            main_character.update(frame_time)
            tile.update(frame_time)
            stage1bg.update(frame_time)
            for monster_mouse in monster_mouseset:
                monster_mouse.update(frame_time)
            for monster_wildboar in monster_wildboarset:
                monster_wildboar.update(frame_time)
            for monster_mouse in monster_mouseset:
                if collide_body(main_character,monster_mouse) and monster_mouse.crush==False:
                    main_character.hp-=1
                    main_character.hp_sound.play()
                    monster_mouse.crush=True
                elif monster_mouse.x<-100 and monster_mouse.crush==False:
                    monster_mouse.crush=True
                    main_character.kill_mouse_count+=1
            for monster_wildboar in monster_wildboarset:
                if monster_wildboar.return_death_frame()>=3:
                    monster_wildboarset.remove(monster_wildboar)
                if main_character.state==main_character.ATTACK and collide_weapon(main_character,monster_wildboar) and monster_wildboar.state==monster_wildboar.RUN:
                    monster_wildboar.state=monster_wildboar.HIT
                    monster_wildboar.death_sound.play()
                    monster_wildboar.total_frames=0.0
                    monster_wildboar.crush=True
                    main_character.kill_wildboar_count+=1
                elif collide_body(main_character,monster_wildboar) and monster_wildboar.crush==False:
                    main_character.hp-=1
                    main_character.hp_sound.play()
                    monster_wildboar.crush=True

        else :
            main_character.update(frame_time*10)
            tile.update(frame_time*10)
            stage1bg.update(frame_time*10)
            for monster_mouse in monster_mouseset:
                monster_mouse.update(frame_time*10)
            for monster_wildboar in monster_wildboarset:
                monster_wildboar.update(frame_time*10)

        if tile.minimap_scroll>17500:
            stage2_class.get_imformation(main_character.hp,main_character.kill_mouse_count,main_character.kill_wildboar_count,main_character.kill_ironboar_count)
            game_framework.change_state(game_stage2)
        elif main_character.hp==0:
            game_framework.change_state(game_title)

        delay(0.03)

def draw():
    clear_canvas()
    stage1bg.draw()
    minimap.draw()
    tile.draw()
    game_pause.draw()
    main_character.draw_minimap_character(tile)
    for monster_mouse in monster_mouseset:
        monster_mouse.draw()
        monster_mouse.draw_bb()
    for monster_wildboar in monster_wildboarset:
        monster_wildboar.draw()
        monster_wildboar.draw_bb()
    main_character.draw()
    main_character.draw_bb_body()
    if(main_character.state==main_character.ATTACK):
        main_character.draw_bb_weapon()
    # font.draw(800,450,str(main_character.y),(128,25,0))
    debug_print('%d,%d,%d,%d' %(main_character.hp,main_character.kill_mouse_count,main_character.kill_wildboar_count,main_character.kill_ironboar_count))
    update_canvas()

def collide_body(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_body()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collide_weapon(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_weapon()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True
