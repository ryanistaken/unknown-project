import pygame

pygame.init()

screen = pygame.display.set_mode((468, 501))

hiding_in_the_darknessIMG = pygame.image.load('hiding_in_the_darkness.png')

pygame.display.set_caption('Your Soul Can\'t Be Saved')
icon = pygame.image.load('watchingyou.ico')
pygame.display.set_icon(icon)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    screen.blit(hiding_in_the_darknessIMG, (0, 0))

    pygame.display.update()
