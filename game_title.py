from pico2d import *

import game_framework
import game_stage2


titlebg = None
firstsubject = None
middlesubject = None
lastsubject = None

firstsubjectx,firstsubjecty = -200,350
middlesubjectx,middlesubjecty = 550,900
lastsubjectx,lastsubjecty = 1600,350
basicstart,shadowstart = None,None
basichelp,shadowhelp=None,None
basicexit,shadowexit=None,None
explain = None #헬프 마우스 온 됫을때 띄우는 로고 아직 미완성

startmouseon,helpmouseon,exitmouseon=False,False,False
starty,helpy,exity=900,900,900

mousex,mousey=None,None

title_time = 0.0

def enter():
    global titlebg,firstsubject,middlesubject,lastsubject,basicstart,shadowstart,basichelp,shadowhelp,basicexit,shadowexit,explain
    titlebg = load_image('resource//titlebg.png')
    firstsubject = load_image('resource//name1.png')
    middlesubject = load_image('resource//name2.png')
    lastsubject = load_image('resource//name3.png')
    basicstart=load_image('resource//start1.png')
    shadowstart=load_image('resource//start2.png')
    basichelp=load_image('resource//help1.png')
    shadowhelp=load_image('resource//help2.png')
    basicexit=load_image('resource//exit1.png')
    shadowexit=load_image('resource//exit2.png')
    explain=load_image('resource//BG1.png')

def exit():
    global titlebg,firstsubject,middlesubject,lastsubject,basicstart,shadowstart,basichelp,shadowhelp,basicexit,shadowexit,explain
    del(titlebg)
    del(firstsubject)
    del(middlesubject)
    del(lastsubject)
    del(basicstart)
    del(shadowstart)
    del(basichelp)
    del(shadowhelp)
    del(basicexit)
    del(shadowexit)
    del(explain)

def handle_events():
    global mousex,mousey,startmouseon,helpmouseon,exitmouseon,starty,helpy,exity,title_time,firstsubjectx,middlesubjecty,lastsubjectx
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            if event.type == SDL_MOUSEMOTION:
                mousex,mousey=event.x, 900-event.y
                if(mousex>=1260 and mousex<=1500 and mousey>=starty and mousey<=starty+80):
                    startmouseon=True
                else:
                    startmouseon=False
                if(mousex>=1320 and mousex<=1500 and mousey>=helpy and mousey<=helpy+80):
                    helpmouseon=True
                else:
                    helpmouseon=False
                if(mousex>=1320 and mousex<=1500 and mousey>=exity and mousey<=exity+80):
                    exitmouseon=True
                else:
                    exitmouseon=False
            if event.type == SDL_MOUSEBUTTONDOWN and startmouseon==True:
                game_framework.change_state(game_stage2)
            elif event.type == SDL_MOUSEBUTTONDOWN and exitmouseon==True:
                game_framework.quit()
            elif event.type == SDL_MOUSEBUTTONDOWN and startmouseon==False and exitmouseon==False:
                title_time=3
                firstsubjectx=250
                middlesubjecty=350
                lastsubjectx=820
                exity=200
                helpy=400
                starty=600

def draw():
    clear_canvas()
    titlebg.draw_to_origin(0,0,1600,900)
    firstsubject.clip_draw_to_origin(0,0,200,200,firstsubjectx,firstsubjecty,200,200)
    middlesubject.clip_draw_to_origin(0,0,200,250,middlesubjectx,middlesubjecty,200,250)
    lastsubject.clip_draw_to_origin(0,0,200,200,lastsubjectx,lastsubjecty,200,200)
    if(startmouseon==True):
        shadowstart.clip_draw_to_origin(0,0,250,100,1200,starty,300,120)
    else:
        basicstart.clip_draw_to_origin(0,0,250,100,1200,starty,300,120)
    if(helpmouseon==True):
        shadowhelp.clip_draw_to_origin(0,0,250,100,1200,helpy,300,120)
        explain.clip_draw_to_origin(0,0,1600,900,250,300,800,300)
    else:
        basichelp.clip_draw_to_origin(0,0,250,100,1200,helpy,300,120)
    if(exitmouseon==True):
        shadowexit.clip_draw_to_origin(0,0,250,100,1200,exity,300,120)
    else:
        basicexit.clip_draw_to_origin(0,0,250,100,1200,exity,300,120)
    update_canvas()


def update():
    global title_time,firstsubjectx,middlesubjecty,lastsubjectx,starty,helpy,exity

    if(title_time<0.45):
        firstsubjectx=firstsubjectx+10
        # firstsubjectx+=firstsubjectx_speed_pps*frame_time
    elif(title_time>=0.45 and title_time<1.00):
        middlesubjecty=middlesubjecty-10
    elif(title_time>=1.00 and title_time<1.52):
        lastsubjectx=lastsubjectx-15
    elif(title_time>=1.52 and title_time<1.87):
        exity-=20
    elif(title_time>=1.87 and title_time<1.90):
        exity+=10
    elif(title_time>=1.90 and title_time<1.93):
        exity-=10
    elif(title_time>=1.93 and title_time<2.17):
        helpy-=20
    elif(title_time>=2.18 and title_time<2.21):
        helpy+=10
    elif(title_time>=2.21 and title_time<2.24):
        helpy-=10
    elif(title_time>=2.24 and title_time<2.44):
        starty-=15
    elif(title_time>=2.44 and title_time<2.47):
        starty+=10
    elif(title_time>=2.47 and title_time<2.50):
        starty-=10
    if(title_time<3):
        delay(0.01)
        title_time+=0.01

def pause():
    pass


def resume():

    pass


