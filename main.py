import math

import pygame as pg
pg.init()
clock = pg.time.Clock()

pg.display.set_caption("Multigame")
screen = pg.display.set_mode((pg.display.get_desktop_sizes()[0][0]-100,pg.display.get_desktop_sizes()[0][1]-100),pg.SCALED)
pg.display.toggle_fullscreen()

i = 0
running = 1

while(running):
    r = round(255*math.cos((i+45)*3.14/180))
    v = round(255*math.cos((i+115)*3.14/180/3))
    b = round(255*math.cos(i*3.14/180/5))
    if(r<0):
        r = -r
    if(v<0):
        v = -v
    if(b<0):
        b = -b
        
    screen.fill(pg.Color(r, v, b))
    
    i += 1
    
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            running = False
        if (event.type == pg.KEYDOWN):
            if (event.key == pg.K_ESCAPE):
                running = False
            if (event.key == pg.K_f):
                pg.display.toggle_fullscreen()
    
    pg.display.flip()
    clock.tick(60)
    
pg.quit()