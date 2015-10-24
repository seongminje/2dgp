from pico2d import *

import game_framework
import stage1

name = "title"
titlebase = None
name1 = None
name2 = None
name3 = None
title_time = 0.0
name1x,name1y = -200,350
name2x,name2y = 550,900
name3x,name3y = 1600,350
start1,start2 = None,None
help1,help2=None,None
explain = None #헬프 마우스 온 됫을때 띄우는 로고 아직 미완성
finish1,finish2=None,None
start,help,finish=False,False,False
starty,helpy,finishy=900,900,900
mousex,mousey=None,None

def enter():
    global titlebase,name1,name2,name3,start1,start2,help1,help2,finish1,finish2,explain
    titlebase = load_image('resource//titlebase.png')
    name1 = load_image('resource//name1.png')
    name2 = load_image('resource//name2.png')
    name3 = load_image('resource//name3.png')
    start1=load_image('resource//gamestart1.png')
    start2=load_image('resource//gamestart2.png')
    help1=load_image('resource//help1.png')
    help2=load_image('resource//help2.png')
    finish1=load_image('resource//exit1.png')
    finish2=load_image('resource//exit2.png')
    explain=load_image('resource//BG1.png')

def exit():
    global titlebase,name1,name2,name3,start1,start2,help1,help2,finish1,finish2,explain
    del(titlebase)
    del(name1)
    del(name2)
    del(name3)
    del(start1)
    del(start2)
    del(help1)
    del(help2)
    del(finish1)
    del(finish2)
    del(explain)

def handle_events():
    global mousex,mousey,start,help,finish,starty,helpy,finishy,title_time,name1x,name2y,name3x
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
                    start=True
                else:
                    start=False
                if(mousex>=1320 and mousex<=1500 and mousey>=helpy and mousey<=helpy+80):
                    help=True
                else:
                    help=False
                if(mousex>=1320 and mousex<=1500 and mousey>=finishy and mousey<=finishy+80):
                    finish=True
                else:
                    finish=False
            if event.type == SDL_MOUSEBUTTONDOWN and start==True:
                game_framework.change_state(stage1)
            elif event.type == SDL_MOUSEBUTTONDOWN and finish==True:
                game_framework.quit()
            elif event.type == SDL_MOUSEBUTTONDOWN and start==False and finish==False:
                title_time=3
                name1x=250
                name2y=350
                name3x=820
                finishy=200
                helpy=400
                starty=600

def draw():
    clear_canvas()
    titlebase.draw_to_origin(0,0,1600,900)
    name1.clip_draw_to_origin(0,0,200,200,name1x,name1y,200,200)
    name2.clip_draw_to_origin(0,0,200,250,name2x,name2y,200,250)
    name3.clip_draw_to_origin(0,0,200,200,name3x,name3y,200,200)
    if(start==True):
        start2.clip_draw_to_origin(0,0,250,100,1200,starty,300,120)
    else:
        start1.clip_draw_to_origin(0,0,250,100,1200,starty,300,120)
    if(help==True):
        help2.clip_draw_to_origin(0,0,250,100,1200,helpy,300,120)
        explain.clip_draw_to_origin(0,0,1600,900,250,300,800,300)
    else:
        help1.clip_draw_to_origin(0,0,250,100,1200,helpy,300,120)
    if(finish==True):
        finish2.clip_draw_to_origin(0,0,250,100,1200,finishy,300,120)
    else:
        finish1.clip_draw_to_origin(0,0,250,100,1200,finishy,300,120)
    update_canvas()


def update():
    global title_time,name1x,name2y,name3x,starty,helpy,finishy

    if(title_time<3):
        delay(0.01)
        title_time+=0.01
    if(title_time<0.45):
        name1x=name1x+10
    elif(title_time>=0.45 and title_time<1.00):
        name2y=name2y-10
    elif(title_time>=1.00 and title_time<1.52):
        name3x=name3x-15
    elif(title_time>=1.52 and title_time<1.87):
        finishy-=20
    elif(title_time>=1.87 and title_time<1.90):
        finishy+=10
    elif(title_time>=1.90 and title_time<1.93):
        finishy-=10
    elif(title_time>=1.93 and title_time<2.18):
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

    # elif(title_time):



def pause():
    pass


def resume():

    pass






