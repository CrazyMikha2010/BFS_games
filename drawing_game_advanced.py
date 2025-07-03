# Pygame microsoft paint with flood fill and distance to target using BFS

import pygame as pg
from collections import deque
import random
pg.init()
pg.font.init()

fps = 120
clock = pg.time.Clock()
w, h = 640, 710
active_size = 0
active_color = 'white'
scr = pg.display.set_mode((w, h))
pg.display.set_caption('Mezhibovskiy project')
my_font = pg.font.SysFont('Comic Sans MS', 30)
text_surface1 = my_font.render('Switch', False, (0, 0, 0))
text_surface2 = my_font.render(' mode', False, (0, 0, 0))
text_surface3 = my_font.render('Clear', False, (0, 0, 0))
painting = []
hover1 = False
hover2 = False
hover3 = False
hover4 = False
hover5 = False
jic1 = pg.Rect([250, 5, 120, 63])
jic2 = pg.Rect([380, 10, 80, 50])
jic3 = pg.Rect([160, 10, 80, 50])
jic4 = pg.Rect([10, 10, 140, 50])
jic5 = pg.Rect([460, 5, 60, 60])
jic6 = False
switch = 1
step = [40, 0]
steps = [40, 64, 128, 160]
grid_rects = []
painting_grid = []
painting_grid_gr = []
grid_bfs = [[0 for _ in range(w // step[0])] for __ in range(w // step[0])]
green_bfs = []
wh = pg.Rect([w - 60, 10, 50, 50])
bl = pg.Rect([w - 110, 10, 50, 50])
gr = pg.Rect([w - 160, 10, 50, 50])
active_color_grid = (0, 0, 0)
wave = False
wave2 = False
res = []
cols = {}
field = pg.display.set_mode((640, 640))
buck = pg.display.set_mode((640, 640))
scr.fill('white')
skibidi = False

def draw_menu_paint(size, color, hover1, hover2):
    if hover1:
        button_color1 = (150, 150, 150)
    else:
        button_color1 = (125, 125, 125)
    if hover2:
        button_color2 = (150, 150, 150)
    else:
        button_color2 = (125, 125, 125)
    if hover5:
        button_color5 = (150, 150, 150)
    else:
        button_color5 = (125, 125, 125)
    pg.draw.rect(scr, 'gray', [0, 0, w, 70])
    pg.draw.rect(scr, button_color1, [250, 5, 120, 63], border_radius=5)
    pg.draw.rect(scr, 'green', [250, 5, 120, 63], 1, border_radius=5)
    scr.blit(text_surface1, (260, 0))
    scr.blit(text_surface2, (260, 25))
    pg.draw.rect(scr, button_color2, [380, 10, 80, 50], border_radius=5)
    pg.draw.rect(scr, 'green', [380, 10, 80, 50], 1, border_radius=5)
    scr.blit(text_surface3, (383, 10))
    pg.draw.line(scr, 'black', (0, 70), (w, 70), 3)
    xl_brush = pg.draw.rect(scr, 'black', [10, 10, 50, 50])
    pg.draw.circle(scr, 'white', (35, 35), 20)
    l_brush = pg.draw.rect(scr, 'black', [70, 10, 50, 50])
    pg.draw.circle(scr, 'white', (95, 35), 15)
    m_brush = pg.draw.rect(scr, 'black', [130, 10, 50, 50])
    pg.draw.circle(scr, 'white', (155, 35), 10)
    s_brush = pg.draw.rect(scr, 'black', [190, 10, 50, 50])
    pg.draw.circle(scr, 'white', (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]
    if size == 20:
        pg.draw.rect(scr, 'green', [10, 10, 50, 50], 3)
    elif size == 15:
        pg.draw.rect(scr, 'green', [70, 10, 50, 50], 3)
    elif size == 10:
        pg.draw.rect(scr, 'green', [130, 10, 50, 50], 3)
    elif size == 5:
        pg.draw.rect(scr, 'green', [190, 10, 50, 50], 3)

    pg.draw.circle(scr, button_color5, (490, 35), 30)
    pg.draw.circle(scr, 'dark gray', (490, 35), 30, 3)
    if jic6 == True: 
        pg.draw.circle(scr, 'green', (490, 35), 30, 3)

    pg.draw.ellipse(scr, 'dark red', [475, 15, 30, 25])
    pg.draw.arc(scr, 'black', [475, 12, 30, 20], 10, 30, 2)
    pg.draw.polygon(scr, 'red', [(475, 25), (505, 25), (500, 55), (480, 55)])
    

    blue = pg.draw.rect(scr, (0, 0, 255), [w - 35, 10, 25, 25])
    red = pg.draw.rect(scr, (255, 0, 0), [w - 35, 35, 25, 25])
    green = pg.draw.rect(scr, (0, 255, 0), [w - 60, 10, 25, 25])
    yellow = pg.draw.rect(scr, (255, 255, 0), [w - 60, 35, 25, 25])
    teal = pg.draw.rect(scr, (0, 255, 255), [w - 85, 10, 25, 25])
    purple = pg.draw.rect(scr, (255, 0, 255), [w - 85, 35, 25, 25])
    white = pg.draw.rect(scr, (255, 255, 255), [w - 110, 10, 25, 25])
    black = pg.draw.rect(scr, (0, 0, 0), [w - 110, 35, 25, 25])
    if active_color == (0, 0, 255):
        pg.draw.line(scr, 'red', (w - 35, 10), (w - 10, 10), 3)
    elif active_color == (255, 0, 0):
        pg.draw.line(scr, 'red', (w - 35, 60), (w - 10, 60), 3)
    elif active_color == (0, 255, 0):
        pg.draw.line(scr, 'red', (w - 60, 10), (w - 35, 10), 3)
    elif active_color == (255, 255, 0):
        pg.draw.line(scr, 'red', (w - 60, 60), (w - 35, 60), 3)
    elif active_color == (0, 255, 255):
        pg.draw.line(scr, 'red', (w - 85, 10), (w - 60, 10), 3)
    elif active_color == (255, 0, 255):
        pg.draw.line(scr, 'red', (w - 85, 60), (w - 60, 60), 3)
    elif active_color == (255, 255, 255):
        pg.draw.line(scr, 'red', (w - 110, 10), (w - 85, 10), 3)
    elif active_color == (0, 0, 0):
        pg.draw.line(scr, 'red', (w - 110, 60), (w - 85, 60), 3)
    color_rect = [blue, red, green, yellow, teal, purple, white, black]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255), (0, 0, 0)]
    return brush_list, color_rect, rgb_list


def draw_menu_grid(step, hover1, hover2, hover3, active_color_grid):
    if hover1:
        button_color1 = (150, 150, 150)
    else:
        button_color1 = (125, 125, 125)
    if hover2:
        button_color2 = (150, 150, 150)
    else:
        button_color2 = (125, 125, 125)
    if hover3:
        button_color3 = (150, 150, 150)
    else:
        button_color3 = (125, 125, 125)
    if hover4:
        button_color4 = (150, 150, 150)
    else:
        button_color4 = (125, 125, 125)
    pg.draw.rect(scr, 'gray', [0, 0, w, 70])
    pg.draw.rect(scr, button_color1, [250, 5, 120, 63], border_radius=5)
    pg.draw.rect(scr, 'green', [250, 5, 120, 63], 1, border_radius=5)
    scr.blit(text_surface1, (260, 0))
    scr.blit(text_surface2, (260, 25))
    pg.draw.rect(scr, button_color2, [380, 10, 80, 50], border_radius=5)
    pg.draw.rect(scr, 'green', [380, 10, 80, 50], 1, border_radius=5)
    scr.blit(text_surface3, (383, 10))
    pg.draw.rect(scr, button_color3, [160, 10, 80, 50], border_radius=5)
    pg.draw.rect(scr, 'green', [160, 10, 80, 50], 1, border_radius=5)
    text_surface4 = my_font.render(f'{step[0]}', False, (0, 0, 0))
    scr.blit(text_surface4, (175, 10))
    pg.draw.rect(scr, 'white', [w - 60, 10, 50, 50])
    pg.draw.rect(scr, 'black', [w - 110, 10, 50, 50])
    pg.draw.rect(scr, 'green', [w - 160, 10, 50, 50])
    if active_color_grid == (0, 0, 0):
        pg.draw.line(scr, 'red', (w - 110, 10), (w - 60, 10), 3)
    elif active_color_grid == (255, 255, 255):
        pg.draw.line(scr, 'red', (w - 60, 10), (w - 10, 10), 3)
    elif active_color_grid == (0, 255, 0):
        pg.draw.line(scr, 'red', (w - 160, 10), (w - 110, 10), 3)
    pg.draw.rect(scr, button_color4, [10, 10, 140, 50], border_radius=5)
    pg.draw.rect(scr, 'green', [10, 10, 140, 50], 1, border_radius=5)
    text_surface5 = my_font.render(f'Run wave', False, (0, 0, 0))
    scr.blit(text_surface5, (15, 10))
    pg.draw.line(scr, 'black', (0, 70), (w, 70), 3)
    for i in range(0, w, step[0]):
        pg.draw.line(scr, 'black', (i, 70), (i, h), 3)
        pg.draw.line(scr, 'black', (0, i + 70), (w, i + 70), 3)
    if len(grid_rects) < (w // step[0]) ** 2:
        for x in range(0, w, step[0]):
            for y in range(70, h, step[0]):
                grid_rects.append([x, y, step[0], step[0]])


def draw_painting(paints, wave2):
    for i in range(len(paints)):
        pg.draw.circle(field, paints[i][0], (paints[i][1][0], paints[i][1][1]), paints[i][2])



def draw_painting_grid(painting_grid, painting_grid_gr):
    for i in range(len(painting_grid)):
        pg.draw.rect(scr, (50, 50, 50), painting_grid[i])
    try:
        tmp = pg.Rect(painting_grid_gr[0])
        pg.draw.rect(scr, (0, 255, 0), tmp)
        pg.draw.polygon(scr, (255, 0, 0), [[tmp[0] + tmp[2] // 4, tmp[1] + tmp[2] // 4], [tmp[0] + tmp[2] // 4, tmp[1] + tmp[2] // 2], [tmp[0] + tmp[2] // 2, tmp[1] + tmp[2] // 3]])
        pg.draw.line(scr, (0, 0, 0), (tmp[0] + tmp[2] // 4, tmp[1] + tmp[2] // 4), (tmp[0] + tmp[2] // 4, tmp[1] + tmp[2] - tmp[2] // 4), 3)
    except:
        pass
    if wave:
        a = [(235, 50, 50), (50, 235, 50), (50, 50, 235)]   
        tmp = random.choice(a)
        idx = random.randint(1, 2)
        for y in range(len(res)):
            for x in range(len(res[0])):
                if res[y][x] > 2:
                    if res[y][x] in cols:
                        col = cols[res[y][x]]
                    else:
                        cols[res[y][x]] = tmp
                        col = cols[res[y][x]]
                        if tmp[0] == 235:
                            if idx == 1:
                                tmp = (tmp[0], (tmp[1] + 15) % 255, (tmp[2] + 10) % 255)
                            else:
                                tmp = (tmp[0], (tmp[1] + 10) % 255, (tmp[2] + 15) % 255)
                        elif tmp[1] == 235:
                            if idx == 1:
                                tmp = ((tmp[0] + 15) % 255, tmp[1], (tmp[2] + 10) % 255)
                            else:
                                tmp = ((tmp[0] + 10) % 255, tmp[1], (tmp[2] + 15) % 255)
                        else:
                            if idx == 1:
                                tmp = ((tmp[0] + 15) % 255, (tmp[1] + 10) % 255, tmp[2])
                            else:
                                tmp = ((tmp[0] + 10) % 255, (tmp[1] + 15) % 255, tmp[2])
                    pg.draw.rect(scr, col, [x * step[0], y * step[0] + 70, step[0], step[0]])





def floodFill_grid(image, sr, sc, color=2):
    def neighbors(image, sr, sc, start):
        indices = [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]
        return [(sr, sc) for sr, sc in indices if isValid(image, sr, sc) and image[sr][sc] == start]


    def isValid(image, sr, sc):
        return sr >= 0 and sc >= 0 and sr < len(image) and sc < len(image[0])
        

    start = image[sr][sc]
    queue = deque([(sr, sc, color)])
    visited = set()
    while queue:
        sr, sc, col = queue.popleft()
        visited.add((sr, sc))
        image[sr][sc] = col
        for sr, sc in neighbors(image, sr, sc, start):
            if (sr, sc) not in visited:
                queue.append((sr, sc, col + 1))
    return image


def floodFill_image(x, y):
    def neighbors(x, y, active_color):
        indices = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [(x, y) for x, y in indices if isValid(x, y) and field.get_at((x, y)) == (255, 255, 255)]


    def isValid(x, y):
        return x >= 0 and y >= 0 and x < 640 and y < 640
        
    start = scr.get_at((x, y))
    queue = [(x, y)]
    visited = set()
    while queue:
        x, y = queue.pop()
        visited.add((x, y))
        field.set_at((x, y), active_color)
        painting.append(((active_color), [x, y], active_size))
        for x, y in neighbors(x, y, active_color):
            if (x, y) not in visited:
                queue.append((x, y))



running = True
while running:
    if switch == 2: scr.fill('white')
    # scr.fill('white')
    # scr.blit(field, (0, 70))
    mouse = pg.mouse.get_pos()
    left_click = pg.mouse.get_pressed()[0]
    if left_click and mouse[1] > 70 and switch == 1:
        #painting.append((active_color, mouse, active_size))
        pg.draw.circle(scr, active_color, mouse, active_size)
        if skibidi:
            try:
                pg.draw.line(scr, active_color, mouse, prev_mouse, active_size * 2)
            except:
                ...
        prev_mouse = mouse
        skibidi = True
    #if switch == 1: draw_painting(painting, wave2)
    if mouse[1] > 70 and switch == 1 and jic6 == False:
        # pg.draw.circle(scr, active_color, mouse, active_size)
        ...
    elif mouse[1] > 70 and switch == 1 and jic6 == True:
        x, y = mouse
        pg.draw.ellipse(scr, 'dark red', [475, 15, 30, 25])
        pg.draw.arc(scr, 'black', [475, 12, 30, 20], 10, 30, 2)
        pg.draw.polygon(scr, 'red', [(475, 25), (505, 25), (500, 55), (480, 55)])

        # pg.draw.ellipse(buck, 'dark red', [x, y, 30, 25])
        # pg.draw.arc(buck, 'black', [x, y - 3, 30, 20], 10, 30, 2)
        # pg.draw.polygon(buck, 'red', [(x, y + 10), (x + 30, y + 10), (x + 25, y + 40), (x + 5, y + 40)])
    if mouse[1] > 70 and switch == 2:
        for i in grid_rects:
            tmp = pg.Rect(i)
            if tmp.collidepoint(mouse):
                if active_color_grid == (0, 0, 0):
                    pg.draw.rect(scr, 'grey', tmp)
                elif active_color_grid == (0, 255, 0):
                    pg.draw.rect(scr, (178, 240, 177), tmp)
                elif active_color_grid == (255, 255, 255):
                    pg.draw.rect(scr, (240, 240, 240), tmp)
    if left_click and mouse[1] > 70 and switch == 2 and active_color_grid == (0, 0, 0):
        x, y = mouse[0], mouse[1] - 70
        grid_bfs[y // step[0]][x // step[0]] = 1
        for i in grid_rects:
            tmp = pg.Rect(i)
            if tmp.collidepoint(mouse):
                painting_grid.append(i)
    elif left_click and mouse[1] > 70 and switch == 2 and active_color_grid == (255, 255, 255):
        x, y = mouse[0], mouse[1] - 70
        grid_bfs[y // step[0]][x // step[0]] = 0
        for i in grid_rects:
            tmp = pg.Rect(i)
            if tmp.collidepoint(mouse):
                try:
                    painting_grid.remove(i)
                except ValueError:
                    pass
    elif left_click and mouse[1] > 70 and switch == 2 and active_color_grid == (0, 255, 0):
        x, y = mouse[0], mouse[1] - 70
        green_bfs = [y // step[0], x // step[0]]
        for i in grid_rects:
            tmp = pg.Rect(i)
            if tmp.collidepoint(mouse):
                painting_grid_gr = []
                painting_grid_gr.append(i)
    if switch == 2: draw_painting_grid(painting_grid, painting_grid_gr)
    if jic1.collidepoint(mouse):
        hover1 = True
    else:
        hover1 = False
    if jic2.collidepoint(mouse):
        hover2 = True
    else:
        hover2 = False
    if jic3.collidepoint(mouse):
        hover3 = True
    else:
        hover3 = False
    if jic4.collidepoint(mouse):
        hover4 = True
    else:
        hover4 = False 
    if jic5.collidepoint(mouse):
        hover5 = True
    else:
        hover5 = False 



    if switch == 1:
        brushes, colors, rgbs = draw_menu_paint(active_size, active_color, hover1, hover2)
    elif switch == 2:
        draw_menu_grid(step, hover1, hover2, hover3, active_color_grid)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if jic1.collidepoint(event.pos):
                if switch == 1:
                    switch = 2
                elif switch == 2:
                    switch = 1
                scr.fill('white')
            if jic2.collidepoint(event.pos):
                painting = []
                grid_rects = []
                painting_grid = []
                painting_grid_gr = []
                grid_bfs = [[0 for _ in range(w // step[0])] for __ in range(w // step[0])]
                green_bfs = [[0 for _ in range(w // step[0])] for __ in range(w // step[0])]
                wave = False
                res = []
                scr.fill('white')
            if jic3.collidepoint(event.pos) and switch == 2:
                step = [steps[(step[1] + 1) % len(steps)], (step[1] + 1) % len(steps)]
                painting = []
                grid_rects = []
                painting_grid = []
                painting_grid_gr = []
                grid_bfs = [[0 for _ in range(w // step[0])] for __ in range(w // step[0])]
                green_bfs = []
                wave = False
                res = []
            if jic4.collidepoint(event.pos) and switch == 2:
                try:
                    res = floodFill_grid(grid_bfs, green_bfs[0], green_bfs[1])
                    wave = True
                except:
                    pass
            if jic5.collidepoint(event.pos) and switch == 1:
                if jic6 == False:
                    jic6 = True
                else:
                    jic6 = False
            if wh.collidepoint(event.pos):
                active_color_grid = (255, 255, 255)
            if bl.collidepoint(event.pos):
                active_color_grid = (0, 0, 0)
            if gr.collidepoint(event.pos):
                active_color_grid = (0, 255, 0)
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
            if jic6 == True and event.pos[1] > 70:
                jic6 = False

                floodFill_image(x, y)
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]
        elif event.type == pg.MOUSEBUTTONUP:
            skibidi = False
    scr.blit(buck, (0, 0))
    
    pg.display.flip()
    clock.tick(fps)
pg.quit()
