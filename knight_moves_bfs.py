# Pygame of a chessboard showing how many moves it takes knight to get to each square using BFS

from collections import deque
import pygame as pg

pg.init()
pg.font.init()
pg.display.set_caption('Mezhibovskiy project')
clock = pg.time.Clock()
fps = 60
w, h = 640, 640
scr = pg.display.set_mode((w, h))
my_font = pg.font.SysFont('Comic Sans MS', 50)
knight = pg.image.load("knight.png").convert_alpha()
knight = pg.transform.scale(knight, (80, 80))
x, y = 0, 0

def knight_bfs(image, sr, sc, color=0):
    def neighbors(image, sr, sc, start):
        indices = [
            (sr - 1, sc - 2),
            (sr - 1, sc + 2),
            (sr + 1, sc - 2),
            (sr + 1, sc + 2),
            (sr - 2, sc - 1),
            (sr - 2, sc + 1),
            (sr + 2, sc - 1),
            (sr + 2, sc + 1)
        ]
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


def draw_grid(image):
    color_grid = {0: (102, 255, 255), 1: (0, 204, 204), 2: (102, 178, 255), 3: (0, 102, 204), 4: (102, 102, 255), 5: (0, 0, 204), 6: (153, 0, 0)}
    for sc in range(8):
        for sr in range(8):
            sq = image[sr][sc]
            tmp_text = my_font.render(f'{sq}',False, (0, 0, 0))
            pg.draw.rect(scr, color_grid[sq], (sr * 80, sc * 80, 80, 80))
            if sq != 0: scr.blit(tmp_text, (sr * 80 + 22, sc * 80 + 5))
    for sc in range(8):
        for sr in range(8):
            pg.draw.line(scr, 'black', (sc * 80, 0), (sc * 80, 640), 3)
            pg.draw.line(scr, 'black', (0, sr * 80), (640, sr * 80), 3)
            


running = True
drag = False
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            drag = True
    
    scr.fill('white')
    left_click = pg.mouse.get_pressed()[0]
    board = [[0 for _ in range(8)] for __ in range(8)]
    if left_click:
        x, y = pg.mouse.get_pos()
        x, y = x // 80, y // 80

    tmp = knight_bfs(board, x, y)
    draw_grid(tmp)
    scr.blit(knight, (x * 80, y * 80))

    pg.display.update()
    clock.tick(60)
pg.quit()
