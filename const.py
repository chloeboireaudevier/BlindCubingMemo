#Background color
global BACKGROUND 
BACKGROUND = (223,220,204)

#Colors
global BLACK
BLACK = (0,0,0)

global GREEN 
GREEN = (16,250,54)
global ORANGE
ORANGE = (250,150,15)
global RED 
RED = (250,16,16)
global BLUE 
BLUE = (16,63,250)
global YELLOW 
YELLOW = (241,250,16)
global WHITE 
WHITE = (255,255,255)

colors = [GREEN,ORANGE,RED,BLUE,YELLOW,WHITE]

edges = {
    (WHITE,BLUE):'AQ',
    (WHITE,ORANGE):'DE',
    (WHITE,GREEN):'CI',
    (WHITE,RED):'BM',
    (YELLOW,ORANGE):'XG',
    (YELLOW,GREEN):'UK',
    (YELLOW,RED):'VO',
    (YELLOW,BLUE):'WS',
    (ORANGE,BLUE):'HR',
    (ORANGE,GREEN):'FL',
    (GREEN,RED):'JP',
    (RED,BLUE):'NT'
}

edges_list = list(edges.items())

corners = {
    (WHITE,ORANGE,GREEN):'DFI',
    (WHITE,ORANGE,BLUE):'AER',
    (WHITE,GREEN,RED):'CJM',
    (WHITE,RED,BLUE):'BNQ',
    (YELLOW,GREEN,ORANGE):'ULG',
    (YELLOW,GREEN,RED):'VKP',
    (YELLOW,RED,BLUE):'WOT',
    (YELLOW,ORANGE,BLUE):'XHS'
}

corners_list = list(corners.items())

#Window size
global width,height
width, height = 500,300
