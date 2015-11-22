import random
import json
from pico2d import *
import game_framework
import game_title
from stage1_class import *

stage1bg = None
main_character = None
tile = None
monster_mouseset = None
monster_wildboarset = None
monsters=None
current_time= get_time()

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
    global main_character,tile,stage1bg,monster_mouseset,monster_wildboarset,current_time,monsters
    main_character=Character()
    tile=Tile()
    stage1bg=Background()
    monster_mouseset = create_monster_mouseset()
    monster_wildboarset = create_monster_wildboarset()
    monsters=monster_mouseset+monster_wildboarset # wildboar도 행렬이면 됨
    current_time = get_time()

def exit():
    global main_character,tile,stage1bg,monster_mouseset,monster_wildboarset,monsters
    del(main_character)
    del(tile)
    del(stage1bg)
    del(monster_mouseset)
    del(monster_wildboarset)
    del(monsters)

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
                main_character.total_frames=0
            elif event.key == SDLK_x:
                main_character.state=2
                main_character.attack_frame=0
                main_character.total_frames=0
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
    global main_character,monster_mouseset,monster_wildboarset,current_time,frame_time
    frame_time = get_time() - current_time
    #frame_rate = 1.0/frame_time
    #print("Frame Rage : %f fps, Frame time : %f sec, "%(frame_rate,frame_time))
    current_time +=frame_time
    main_character.update(frame_time)
    for monster_mouse in monsters:
        if collide_body(main_character,monster_mouse) and monster_mouse.crush==False:
            main_character.hp-=1
            monster_mouse.crush=True
    for monster_wildboar in monster_wildboarset:
        if main_character.state==main_character.ATTACK and collide_weapon(main_character,monster_wildboar):
            monster_wildboar.state=monster_wildboar.HIT
            monster_wildboar.total_frames=0.0
            monster_wildboar.crush=True
        elif collide_body(main_character,monster_wildboar) and monster_wildboar.crush==False:
            main_character.hp-=1
            monster_wildboar.crush=True
    tile.update(frame_time)
    stage1bg.update(frame_time)
    for monster_mouse in monsters:
        monster_mouse.update(frame_time)
    for monster_wildboar in monsters:
        monster_wildboar.update(frame_time)
    if(main_character.hp==0):
        game_framework.change_state(game_title)
    delay(0.03)

def draw():
    clear_canvas()
    stage1bg.draw()
    tile.draw()
    for monster_mouse in monsters:
        monster_mouse.draw()
        monster_mouse.draw_bb()
    for monster_wildboar in monsters:
        monster_wildboar.draw()
        monster_wildboar.draw_bb()
    main_character.draw()
    main_character.draw_bb_body()
    if(main_character.state==main_character.ATTACK):
        main_character.draw_bb_weapon()

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