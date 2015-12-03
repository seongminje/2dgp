import random
import json
from pico2d import *
import game_framework
import game_title

from stage3_class import *

stage1bg = None
main_character = None
main_character2 = None
tile = None
minimap=None
monster_upside_mouseset = None
monster_upside_wildboarset = None
monster_upside_ironboarset=None
monster_downside_mouseset = None
monster_downside_wildboarset = None
monster_downside_ironboarset=None
current_time= get_time()
cheat_fastframe = False
stage2_bgm=None
game_pause=None
cheat_etc= None
time_pause=0.0
time_resume=0.0
time_return=0.0


def create_upside_monster_ironboarset():
    monster_upside_ironboar_data_file= open('resource\\jsons\\stage2_upside_monster_ironboar_data.txt','r')
    monster_upside_ironboar_data = json.load(monster_upside_ironboar_data_file)
    monster_upside_ironboar_data_file.close()
    monster_ironboarset=[]
    for num in monster_upside_ironboar_data:
        monster_ironboar = Monster_ironboar_upside()
        monster_ironboar.num = num
        monster_ironboar.x=monster_upside_ironboar_data[num]['x']+random.randint(0,500)
        monster_ironboar.y=monster_upside_ironboar_data[num]['y']
        monster_ironboarset.append(monster_ironboar)
    return monster_ironboarset

def create_upside_monster_mouseset():
    monster_upside_mouse_data_file= open('resource\\jsons\\stage2_upside_monster_mouse_data.txt','r')
    monster_upside_mouse_data = json.load(monster_upside_mouse_data_file)
    monster_upside_mouse_data_file.close()
    monster_upside_mouseset=[]
    for num in monster_upside_mouse_data:
        monster_mouse = Monster_mouse_upside()
        monster_mouse.num = num
        monster_mouse.x=monster_upside_mouse_data[num]['x']+random.randint(0,500)
        monster_mouse.y=monster_upside_mouse_data[num]['y']
        monster_upside_mouseset.append(monster_mouse)
    return monster_upside_mouseset

def create_upside_monster_wildboarset():
    monster_upside_wildboar_data_file= open('resource\\jsons\\stage2_upside_monster_wildboar_data.txt','r')
    monster_upside_wildboar_data = json.load(monster_upside_wildboar_data_file)
    monster_upside_wildboar_data_file.close()
    monster_upside_wildboarset=[]
    for num in monster_upside_wildboar_data:
        monster_wildboar = Monster_wildboar_upside()
        monster_wildboar.num = num
        monster_wildboar.x=monster_upside_wildboar_data[num]['x']+random.randint(0,500)
        monster_wildboar.y=monster_upside_wildboar_data[num]['y']
        monster_upside_wildboarset.append(monster_wildboar)
    return monster_upside_wildboarset

def create_downside_monster_ironboarset():
    monster_downside_ironboar_data_file= open('resource\\jsons\\stage2_downside_monster_ironboar_data.txt','r')
    monster_downside_ironboar_data = json.load(monster_downside_ironboar_data_file)
    monster_downside_ironboar_data_file.close()
    monster_downside_ironboarset=[]
    for num in monster_downside_ironboar_data:
        monster_ironboar = Monster_ironboar_downside()
        monster_ironboar.num = num
        monster_ironboar.x=monster_downside_ironboar_data[num]['x']+random.randint(0,500)
        monster_ironboar.y=monster_downside_ironboar_data[num]['y']
        monster_downside_ironboarset.append(monster_ironboar)
    return monster_downside_ironboarset

def create_downside_monster_mouseset():
    monster_downside_mouse_data_file= open('resource\\jsons\\stage2_downside_monster_mouse_data.txt','r')
    monster_downside_mouse_data = json.load(monster_downside_mouse_data_file)
    monster_downside_mouse_data_file.close()
    monster_downside_mouseset=[]
    for num in monster_downside_mouse_data:
        monster_mouse = Monster_mouse_downside()
        monster_mouse.num = num
        monster_mouse.x=monster_downside_mouse_data[num]['x']+random.randint(0,500)
        monster_mouse.y=monster_downside_mouse_data[num]['y']
        monster_downside_mouseset.append(monster_mouse)
    return monster_downside_mouseset

def create_downside_monster_wildboarset():
    monster_downside_wildboar_data_file= open('resource\\jsons\\stage2_downside_monster_wildboar_data.txt','r')
    monster_downside_wildboar_data = json.load(monster_downside_wildboar_data_file)
    monster_downside_wildboar_data_file.close()
    monster_downside_wildboarset=[]
    for num in monster_downside_wildboar_data:
        monster_wildboar = Monster_wildboar_downside()
        monster_wildboar.num = num
        monster_wildboar.x=monster_downside_wildboar_data[num]['x']+random.randint(0,500)
        monster_wildboar.y=monster_downside_wildboar_data[num]['y']
        monster_downside_wildboarset.append(monster_wildboar)
    return monster_downside_wildboarset

def enter():
    global main_character,main_character2,tile,stage1bg,current_time,minimap,stage2_bgm,cheat_etc,game_pause
    global monster_upside_mouseset,monster_upside_wildboarset,monster_upside_ironboarset
    global monster_downside_mouseset,monster_downside_wildboarset,monster_downside_ironboarset
    main_character=Character_upside()
    main_character2=Character_downside()
    tile=Tile()
    minimap=Minimap()
    stage1bg=Background()
    monster_upside_mouseset = create_upside_monster_mouseset()
    monster_upside_wildboarset = create_upside_monster_wildboarset()
    monster_upside_ironboarset = create_upside_monster_ironboarset()
    monster_downside_mouseset = create_downside_monster_mouseset()
    monster_downside_wildboarset = create_downside_monster_wildboarset()
    monster_downside_ironboarset = create_downside_monster_ironboarset()
    # up_monsters=monster_wildboarset+monster_mouseset # wildboar도 행렬이면 됨
    current_time = get_time()
    stage2_bgm=load_music('resource//sound//bgm_title.ogg')
    stage2_bgm.set_volume(32)
    stage2_bgm.repeat_play()
    cheat_etc=load_wav('resource//sound//etc_cheat.wav')
    cheat_etc.set_volume(0)
    cheat_etc.repeat_play()
    game_pause=Pause()

def exit():
    global main_character,main_character2,tile,stage1bg,minimap,stage2_bgm,cheat_etc
    global monster_upside_mouseset,monster_upside_wildboarset,monster_upside_ironboarset
    global monster_downside_mouseset,monster_downside_wildboarset,monster_downside_ironboarset
    del(main_character)
    del(main_character2)
    del(tile)
    del(minimap)
    del(stage1bg)
    del(monster_upside_mouseset)
    del(monster_upside_wildboarset)
    del(monster_upside_ironboarset)
    del(monster_downside_mouseset)
    del(monster_downside_wildboarset)
    del(monster_downside_ironboarset)
    del(stage2_bgm)
    del(cheat_etc)

def pause():
    pass

def resume():
    pass

def handle_events():
    global main_character,main_character2,cheat_fastframe,cheat_etc,time_pause,time_resume,time_return
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                game_framework.change_state(game_title)
                break
            if main_character.state==main_character.RUN:
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
            if main_character2.state==main_character2.RUN:
                if event.key == SDLK_UP:
                    main_character2.keycheckup = True
                elif event.key == SDLK_DOWN:
                    main_character2.keycheckdown = True
                elif event.key == SDLK_LEFT:
                    main_character2.keycheckleft = True
                elif event.key == SDLK_RIGHT:
                    main_character2.keycheckright = True
                elif event.key == SDLK_z:
                    main_character2.state=1
                    main_character2.jump_frame=0
                    main_character2.total_frames=0
                    main_character2.jump_sound.play()
                elif event.key == SDLK_x:
                    main_character2.state=2
                    main_character2.attack_frame=0
                    main_character2.total_frames=0
                    main_character2.attack_sound.play()
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                main_character.keycheckup = False
                main_character2.keycheckup = False
            elif event.key == SDLK_DOWN:
                main_character.keycheckdown = False
                main_character2.keycheckdown = False
            elif event.key == SDLK_LEFT:
                main_character.keycheckleft = False
                main_character2.keycheckleft = False
            elif event.key == SDLK_RIGHT:
                main_character.keycheckright = False
                main_character2.keycheckright = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_0:
            cheat_fastframe=True
            cheat_etc.set_volume(32)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            if game_pause.pressed == False:
                game_pause.pressed = True
                time_pause=get_time()
                stage2_bgm.set_volume(0)
            else:
                game_pause.pressed = False
                time_resume=get_time()
                time_return+=time_resume-time_pause
                stage2_bgm.set_volume(32)
        elif event.type == SDL_KEYUP and event.key == SDLK_0:
            cheat_fastframe=False
            cheat_etc.set_volume(0)

def update():
    if game_pause.pressed == False:
        global main_character,main_character2,current_time,frame_time,cheat_fastframe
        global monster_upside_mouseset,monster_upside_wildboarset,monster_upside_ironboarset
        global downside_mouseset,monster_downside_wildboarset,monster_downside_ironboarset
        frame_time = get_time() - current_time-time_return
        current_time +=frame_time

        if cheat_fastframe == False:
            main_character.update(frame_time)
            main_character2.update(frame_time)
            tile.update(frame_time)
            stage1bg.update(frame_time)
            for monster_mouse in monster_upside_mouseset:
               monster_mouse.update(frame_time)
            for monster_wildboar in monster_upside_wildboarset:
                monster_wildboar.update(frame_time)
            for monster_ironboar in monster_upside_ironboarset:
                monster_ironboar.update(frame_time)
            for monster_mouse in monster_downside_mouseset:
                monster_mouse.update(frame_time)
            for monster_wildboar in monster_downside_wildboarset:
                monster_wildboar.update(frame_time)
            for monster_ironboar in monster_downside_ironboarset:
                monster_ironboar.update(frame_time)
            for monster_mouse in monster_upside_mouseset:
                if collide_body(main_character,monster_mouse) and monster_mouse.crush==False:
                    main_character.hp-=1
                    main_character.hp_sound.play()
                    monster_mouse.crush=True
                elif monster_mouse.x<-100 and monster_mouse.crush==False:
                    monster_mouse.crush=True
                    main_character.kill_mouse_count+=1
            for monster_wildboar in monster_upside_wildboarset:
                if monster_wildboar.return_death_frame()>=3:
                    monster_upside_wildboarset.remove(monster_wildboar)
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
            for monster_ironboar in monster_upside_ironboarset:
                if monster_ironboar.return_death_frame()>=3:
                        monster_upside_ironboarset.remove(monster_ironboar)
                if main_character.state==main_character.ATTACK and collide_weapon(main_character,monster_ironboar) and monster_ironboar.state==monster_ironboar.RUN:
                        monster_ironboar.state=monster_ironboar.HIT
                        monster_ironboar.hit_sound.play()
                        monster_ironboar.total_frames=0.0
                        monster_ironboar.hp-=1
                        if monster_ironboar.hp==0:
                            main_character.kill_ironboar_count+=1
                elif collide_body(main_character,monster_ironboar) and monster_ironboar.hp>0 and monster_ironboar.crush==False:
                        main_character.hp-=1
                        main_character.hp_sound.play()
                        monster_ironboar.crush=True

            for monster_mouse in monster_downside_mouseset:
                if collide_body(main_character2,monster_mouse) and monster_mouse.crush==False:
                    main_character.hp-=1
                    main_character.hp_sound.play()
                    monster_mouse.crush=True
                elif monster_mouse.x<-100 and monster_mouse.crush==False:
                    monster_mouse.crush=True
                    main_character.kill_mouse_count+=1
            for monster_wildboar in monster_downside_wildboarset:
                if monster_wildboar.return_death_frame()>=3:
                    monster_downside_wildboarset.remove(monster_wildboar)
                if main_character2.state==main_character2.ATTACK and collide_weapon(main_character2,monster_wildboar) and monster_wildboar.state==monster_wildboar.RUN:
                    monster_wildboar.state=monster_wildboar.HIT
                    monster_wildboar.death_sound.play()
                    monster_wildboar.total_frames=0.0
                    monster_wildboar.crush=True
                    main_character.kill_wildboar_count+=1
                elif collide_body(main_character2,monster_wildboar) and monster_wildboar.crush==False:
                    main_character.hp-=1
                    main_character.hp_sound.play()
                    monster_wildboar.crush=True
            for monster_ironboar in monster_downside_ironboarset:
                if monster_ironboar.return_death_frame()>=3:
                        monster_downside_ironboarset.remove(monster_ironboar)
                if main_character2.state==main_character2.ATTACK and collide_weapon(main_character2,monster_ironboar) and monster_ironboar.state==monster_ironboar.RUN:
                        monster_ironboar.state=monster_ironboar.HIT
                        monster_ironboar.hit_sound.play()
                        monster_ironboar.total_frames=0.0
                        monster_ironboar.hp-=1
                        if monster_ironboar.hp==0:
                            main_character.kill_ironboar_count+=1
                elif collide_body(main_character2,monster_ironboar) and monster_ironboar.hp>0 and monster_ironboar.crush==False:
                        main_character.hp-=1
                        monster_ironboar.crush=True
        else :
            main_character.update(frame_time*10)
            main_character2.update(frame_time*10)
            tile.update(frame_time*10)
            stage1bg.update(frame_time*10)
            for monster_mouse in monster_upside_mouseset:
               monster_mouse.update(frame_time*10)
            for monster_wildboar in monster_upside_wildboarset:
                monster_wildboar.update(frame_time*10)
            for monster_ironboar in monster_upside_ironboarset:
                monster_ironboar.update(frame_time*10)
            for monster_mouse in monster_downside_mouseset:
                monster_mouse.update(frame_time*10)
            for monster_wildboar in monster_downside_wildboarset:
                monster_wildboar.update(frame_time*10)
            for monster_ironboar in monster_downside_ironboarset:
                monster_ironboar.update(frame_time*10)

        if tile.minimap_scroll>17500 :
            # stage3_class.get_hp(int(main_character.hp))
            game_framework.change_state(game_title)
        elif(main_character.hp==0):
            game_framework.change_state(game_title)

        delay(0.03)

def draw():
    clear_canvas()
    stage1bg.draw()
    tile.draw()
    minimap.draw()
    game_pause.draw()
    main_character.draw_minimap_character(tile)
    for monster_mouse in monster_upside_mouseset:
        monster_mouse.draw()
        monster_mouse.draw_bb()
    for monster_wildboar in monster_upside_wildboarset:
        monster_wildboar.draw()
        monster_wildboar.draw_bb()
    for monster_ironboar in monster_upside_ironboarset:
        monster_ironboar.draw()
        monster_ironboar.draw_bb()

    for monster_mouse in monster_downside_mouseset:
        monster_mouse.draw()
        monster_mouse.draw_bb()
    for monster_wildboar in monster_downside_wildboarset:
        monster_wildboar.draw()
        monster_wildboar.draw_bb()
    for monster_ironboar in monster_downside_ironboarset:
        monster_ironboar.draw()
        monster_ironboar.draw_bb()
    main_character.draw()
    main_character2.draw()
    main_character.draw_bb_body()
    main_character2.draw_bb_body()
    if(main_character.state==main_character.ATTACK):
        main_character.draw_bb_weapon()
    if(main_character2.state==main_character2.ATTACK):
        main_character2.draw_bb_weapon()
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
