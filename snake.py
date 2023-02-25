import pygame
from pygame.locals import *
import random

WINDOW_SIZE = ((800, 600))
PIXEL_SIZE = 10
score = 0


background = pygame.image.load(r"C:\Users\guial\OneDrive\Imagens\Saved Pictures\background.png")
background = pygame.transform.scale(background, WINDOW_SIZE)

def colision(pos1, pos2):
    return pos1 == pos2


def off_limits(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True 


def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE))
pygame.display.set_caption('snake')

snake_colors = [[0, 255, 0], [255, 0, 0], [0, 0, 255]]  

#snake_color = [0,0,0]

snake_pos = [(250, 50),(250, 60),(250, 60)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))

#snake_surface.fill(snake_color)

snake_surface.fill(snake_colors[0]) 

snake_direction = K_LEFT

apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_surface.fill((255, 0, 0))
apple_pos = random_on_grid()

fps = 15

font = pygame.font.Font(None, 36)

color_index = 0 # índice da cor atual

while True:
    pygame.time.Clock().tick(fps)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    
    screen.blit(background, (0, 0))
    

    screen.blit(apple_surface, apple_pos)

    if colision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, 0))
        apple_pos = random_on_grid() 
        fps = fps + 3
        score += 10 
        color_index = (color_index + 1) % len(snake_colors) # mudar a cor para a próxima na lista


    if score >= 40:
        background = pygame.image.load(r"C:\Users\guial\OneDrive\Imagens\Saved Pictures\desert.jpg")
        background = pygame.transform.scale(background, WINDOW_SIZE)
    if score >= 60:
        background = pygame.image.load(r"C:\Users\guial\OneDrive\Imagens\Saved Pictures\back4.jpg")
        background = pygame.transform.scale(background, WINDOW_SIZE)

    snake_surface.fill(snake_colors[color_index]) # atualizar a cor da cobra

    for pos in snake_pos:
        screen.blit(snake_surface, pos)

    for i in range(len(snake_pos) - 1, 0, -1):
        if colision(snake_pos[0], snake_pos[i]):
            pygame.quit()
            quit()
        snake_pos[i] = snake_pos[i-1]


    if off_limits(snake_pos[0]):
        pygame.quit()
        quit()


    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] -  PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE,  snake_pos[0][1])

    
    score_text = font.render("Pontuação: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, [10, 10])

    pygame.display.update()
