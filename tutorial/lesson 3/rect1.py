import pygame
from pygame.locals import *

SIZE = 500, 500
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

rect = Rect(50, 160, 80, 80)
r2 = Rect(200, 200, 100, 100)
print(rect)

print(f'x={rect.x}, y={rect.y}, w={rect.w}, h={rect.h}')
print(f'left={rect.left}, top={rect.top}, right={rect.right}, bottom={rect.bottom}')
print(f'center={rect.center}')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    pygame.draw.rect(screen, RED, r2)
    pygame.display.flip()

pygame.quit()