import random
import json
from pico2d import *
import game_framework
import game_title
from class_data import *

stage1bg = None
main_character = None
tile = None
monster_mouseset = None
monster_wildboar = None
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

def enter():
    global main_character,tile,stage1bg,monster_mouseset,monster_wildboar,current_time
    main_character=Character()
    tile=Tile()
    stage1bg=Background()
    monster_mouseset = create_monster_mouseset()
    monster_wildboar = Monster_wildboar()
    current_time = get_time()

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
    global monster_mouseset,main_character,monster_wildboar,current_time,frame_time
    frame_time = get_time() - current_time
    #frame_rate = 1.0/frame_time
    #print("Frame Rage : %f fps, Frame time : %f sec, "%(frame_rate,frame_time))
    current_time +=frame_time

    main_character.update(frame_time)
    for monster_mouse in monster_mouseset:
        if main_character.x in range(monster_mouse.x, monster_mouse.x+80) and main_character.y-65 in range(monster_mouse.y-30, monster_mouse.y+50) and monster_mouse.crush==False:
            main_character.hp-=1
            monster_mouse.crush=True
    if main_character.state==main_character.ATTACK and main_character.x+90 in range(monster_wildboar.x-20,monster_wildboar.x+40):
        monster_wildboar.state=monster_wildboar.HIT
        monster_wildboar.total_frames=0.0
        monster_wildboar.crush=True
    elif main_character.x in range(monster_wildboar.x-30,monster_wildboar.x+20) and monster_wildboar.crush==False:
        main_character.hp-=1
        monster_wildboar.crush=True
    tile.update(frame_time)
    stage1bg.update(frame_time)
    for monster_mouse in monster_mouseset:
        monster_mouse.update(frame_time)
    monster_wildboar.update(frame_time)
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