# Pygame microsoft paint with flood fill using BFS

import pygame as pg
from collections import deque

pg.init()
pg.font.init()
clock = pg.time.Clock()
FPS = 120
w1, h1 = 800, 500
scr = pg.display.set_mode((w1, h1))
scr.fill('light grey')
w2, h2 = 750, 500
canvas = pg.surface.Surface((w2, h2))
canvas.fill('white')
size = 10
color = (0, 0, 0)
black = pg.Rect([0, 0, 50, 50])
white = pg.Rect([0, 50, 50, 50])
red = pg.Rect([0, 100, 50, 50])
green = pg.Rect([0, 150, 50, 50])
blue = pg.Rect([0, 200, 50, 50])
font = pg.font.SysFont('Comic Sans MS', 15)
check = 0

draw = False
running = True
def draw_menu(surface):
    pg.draw.rect(surface, 'black', (0, 0, 50, 50))
    pg.draw.rect(surface, 'white', (0, 50, 50, 50))
    pg.draw.rect(surface, 'red', (0, 100, 50, 50))
    pg.draw.rect(surface, 'green', (0, 150, 50, 50))
    pg.draw.rect(surface, 'blue', (0, 200, 50, 50))
    text1 = font.render('Press F', False, (0, 0, 0))
    text2 = font.render('to fill', False, (0, 0, 0))
    surface.blit(text1, (0, 450))
    surface.blit(text2, (5, 470))
    text3 = font.render('Press C', False, (0, 0, 0))
    text4 = font.render('to clear', False, (0, 0, 0))
    surface.blit(text3, (0, 400))
    surface.blit(text4, (0, 420))

def fill(surface, x, y, color):
    x -= 50
    def neighbors(x, y):
        moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [(x, y) for x, y in moves if isValid(x, y) and surface.get_at((x, y)) == start]


    def isValid(x, y):
        return x >= 0 and y >= 0 and x < w2 and y < h2
        
    start = surface.get_at((x, y))
    queue = [(x, y)]
    visited = set()
    while queue:
        x, y = queue.pop()
        visited.add((x, y))
        surface.set_at((x, y), color)
        for x, y in neighbors(x, y):
            if (x, y) not in visited:
                queue.append((x, y))


while running:
    x, y = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if x > 50:
                draw = True
            else:
                if black.collidepoint(event.pos):
                    color = 'black'
                elif white.collidepoint(event.pos):
                    color = 'white'
                elif red.collidepoint(event.pos):
                    color = 'red'
                elif green.collidepoint(event.pos):
                    color = 'green'
                elif blue.collidepoint(event.pos):
                    color = 'blue'
        elif event.type == pg.MOUSEBUTTONUP:
            draw = False
            check = 0
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                canvas.fill('white')
            elif event.key == pg.K_f:
                fill(canvas, x, y, color)



    if draw:
        x -= 50
        pg.draw.circle(canvas, color, [x, y], size)
        try:
            if check != 0:
                pg.draw.line(canvas, color, prev_coords, [x, y], size * 2)
        except:
            ...
        prev_coords = [x, y]
        check = 1


    draw_menu(scr)
    scr.blit(canvas, (50, 0))

    pg.display.flip()
    clock.tick(FPS)
pg.quit()
