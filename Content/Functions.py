import pygame
import random

sizeX = 10
sizeY = 100
white = (255,255,255)

def Score_board(screen,X1,X2,X3):
  font = pygame.font.Font("./Content/Adlanta.ttf",100)
  Stat = "Level_1"
  if 15 <X3 <= 30:
    Stat = "Level_2"
  if 30 <X3:
    Stat = "Level_3"
  score = font.render(str(X1)+" : "+str(X2)+" _:- "+Stat,True,(255,255,255))
  score_pos = score.get_rect(midbottom = [960,170])
  screen.blit(score,(score_pos))
  pygame.draw.line(screen,white,(0,195),(1920,195),5)
  pygame.draw.line(screen,white,(960,210),(960,1070),5)

def Player(screen,posX,posY):
  screen.fill(white,[posX,posY,sizeX,sizeY])

def Ball_img(screen,posX,posY):
  pygame.draw.circle(screen,white,(posX,posY),20)

def Comp_limit(x,z):
  y = 0
  for i in range(z):
    y += x
    if y > z:
      break
  return (y-x)

def Random(x,y):
  p = random.randint(x,y)
  return p