import pygame 
import constants
from character import Character

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")

#Create clock for maintaining frame rate 
clock = pygame.time.Clock()

#Define palyer movement variables 
moving_left = False 
moving_right = False
moving_up = False 
moving_down = False 

#Scaling Helper Function to scale image 
def scale_img(image, scale): 
  w = image.get_width()
  h = image.get_height()
  return pygame.transform.scale(image, (w* scale, h * scale))

#Loading player
player_image = pygame.image.load('assets/images/characters/elf/idle/0.png').convert_alpha()
player_image = scale_img(player_image, constants.SCALE)

# Create Player 
player = Character(100,100, player_image)

#Main game loop 
run = True
while run:

  #Control frame rate 
  clock.tick(constants.FPS)

  screen.fill(constants.BG)

  #Calculate player movement 
  dx = 0 # How much left vs right 
  dy = 0 # How much up and down 
  if moving_right == True: 
    dx = constants.SPEED
  if moving_left == True: 
    dx = -constants.SPEED
  if moving_up == True: 
    dy = -constants.SPEED
  if moving_down == True: 
    dy = constants.SPEED

  #move player 
  player.move(dx, dy)

  #Draw player on screen 
  player.draw(screen)

  #Event handler 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    #Take keyboard presses to move player 
    if event.type == pygame.KEYDOWN: 
      if event.key == pygame.K_a: 
        moving_left = True 
      if event.key == pygame.K_d: 
        moving_right = True 
      if event.key == pygame.K_w: 
        moving_up = True 
      if event.key == pygame.K_s: 
        moving_down = True 
    #Keyboard button releases 
    if event.type == pygame.KEYUP: 
      if event.key == pygame.K_a: 
        moving_left = False
      if event.key == pygame.K_d: 
        moving_right = False 
      if event.key == pygame.K_w: 
        moving_up = False 
      if event.key == pygame.K_s: 
        moving_down = False 

  pygame.display.update()

pygame.quit()