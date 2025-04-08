import pygame
import math

def Draw_Branch(screen, x, y, angle, length, depth):
    if depth == 0:
        return
    x_end = x + length * math.cos(angle)
    y_end = y - length * math.sin(angle)
    pygame.draw.line(screen, (0, 255, 0), (x, y), (x_end, y_end), depth)
    Draw_Branch(screen, x_end, y_end, angle - math.pi / 6, length * 0.7, depth - 1)
    Draw_Branch(screen, x_end, y_end, angle + math.pi / 6, length * 0.7, depth - 1)


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))
    Draw_Branch(screen, 400, 550, math.pi / 2, 100, 6)
    pygame.display.flip()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            