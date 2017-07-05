import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode([800, 600]
pygame.display.set_caption('Lazer Cat')
 
clock = pygame.time.Clock()
click_sound = pygame.mixer.Sound("laser5.ogg")
background_position = [0, 0]
background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
    screen.blit(background_image, background_position)
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    screen.blit(player_image, [x, y])
    pygame.display.flip() 
    clock.tick(60)
 
pygame.quit()