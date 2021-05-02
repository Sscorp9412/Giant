import pygame
from .Functions import *
pygame.init()

def Computer(screen,screen_w,screen_h):
  clock = pygame.time.Clock()
  # Player_1 movement variables
  Player_1 = {'X_pos': 0,'Y_pos': int(screen_h / 5), 'Y_change': 0}
  # Player_2 movement variables
  Player_2 = {'X_pos': int(screen_w - 10),'Y_pos': 3*int(screen_h / 5), 'Y_change': 0}
  # Ball movement variables
  Ball={'X_pos':int((screen_w/2)-12),'Y_pos':int((screen_h/2)-10),'X_change':4,'Y_change':2}
  # Score variables
  Score={'Player1':0,'Player2':0}

  play = True
  while play:
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,0,0),(0,0),20)
    Score_board(screen,Score['Player1'],Score['Player2'])
    ## Events/Actions(Keyboard controls)
    for action in pygame.event.get():
      if action.type == pygame.MOUSEBUTTONDOWN:
        play = False
      if action.type == pygame.KEYDOWN:
        if action.key == pygame.K_UP:
          Player_2['Y_change'] = -4
        if action.key == pygame.K_DOWN:
          Player_2['Y_change'] = 4
      if action.type == pygame.KEYUP:
        if action.key == pygame.K_UP or action.key == pygame.K_DOWN:
          Player_2['Y_change'] = 0
    ## Player_computer Algorithm
    # Player_1 movement controls 
    Player_1['Y_pos'] += Player_1['Y_change']
    if Player_1['Y_pos'] >= 980:
      Player_1['Y_pos'] = 980
    if Player_1['Y_pos'] <= 200:
      Player_1['Y_pos'] = 200
    #########################################
    #player_2 movement controls
    Player_2['Y_pos'] += Player_2['Y_change']
    if Player_2['Y_pos'] >= 980:
      Player_2['Y_pos'] = 980
    if Player_2['Y_pos'] <= 200:
      Player_2['Y_pos'] = 200
    # Ball movement Controls
    ## Ball & surrounding interaction
    Ball['X_pos'] += Ball['X_change']
    Ball['Y_pos'] += Ball['Y_change']
    if Ball['Y_pos'] >= 1060:
      Ball['Y_change'] = (-1)*(Ball['Y_change'])
    if Ball['Y_pos'] <=220:
      Ball['Y_change'] = (-1)*(Ball['Y_change'])
    ## Ball & Computer interaction system
    if -20 <= (int(Ball['Y_pos']) - int(Player_1['Y_pos'])) <= 120:
      Ball['X_change'] = (-1)*(Ball['X_change'])
    else:
      Score['Player2'] += 1
    ## Ball & Player interaction system
    if Ball['X_pos'] == 1900:
      if -20 < (int(Ball['Y_pos']) - int(Player_2['Y_pos'])) < 120:
        Ball['X_change'] = (-1)*(Ball['X_change'])
        Ball['X_change'] +=1
        Ball['Y_change'] += Player_1['Y_change']
      else:
        Score['Player1'] += 1
    # Ball reloading after going out of screen
    if 0 > Ball['X_pos'] or Ball['X_pos'] > 1920:
      Ball = {'X_pos': 500 ,'Y_pos': 500 ,'X_change': 4 ,'Y_change': 2}
    # Screen show items
    Player(screen,Player_1['X_pos'],Player_1['Y_pos'])
    Player(screen,Player_2['X_pos'],Player_2['Y_pos'])
    Ball_img(screen,Ball['X_pos'],Ball['Y_pos'])
    pygame.display.update()
    clock.tick(100)
pygame.quit()