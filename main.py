import gladnessCRIT
import pygame

# inititalize pygame
pygame.init()

# creating a screen
screen = pygame.display.set_mode([800, 600])
# pygame.display.update()

pygame.display.set_caption("Tour de Gladnes")
# pygame.image.load('adrianagladness/downloads/cycling.png')


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Display screen color
    screen.fill((0,128,128))
# Draw a solid circle in the center of the screen
    pygame.draw.circle(screen, (255,255, 0), (700, 100), 90)

    pygame.display.flip()

    

pygame.quit()

