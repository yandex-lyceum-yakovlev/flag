import pygame

pygame.init()

size = width, height = 300, 300
screen = pygame.display.set_mode(size)


def draw_flag():
    gray = pygame.Color("#777777")
    white = pygame.Color("#ffffff")
    pygame.draw.rect(screen, gray, [(20, 20), (5, 280)], 0)
    pygame.draw.rect(screen, white, [(25, 20), (200, 80)], 0)


draw_flag()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
