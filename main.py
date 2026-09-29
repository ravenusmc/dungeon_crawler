import pygame 

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")

#Main game loop 
run = True
while run:

  #Event handler 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False 

pygame.quit()