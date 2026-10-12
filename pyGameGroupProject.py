#CSCE 1010
#Names: Ethan Trombley, Kallen Schulz, Dabin Choi

#This file is just for fun

import pygame


screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Rock Paper Scissors")
fps = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 60))

    pygame.display.flip()
    fps.tick(30)