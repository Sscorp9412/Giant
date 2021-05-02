import pygame
from Content.player import *
from Content.Vs_comp import *
pygame.init()
pygame.display.set_caption("Game_Version2.0.3")

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width,screen_height),pygame.FULLSCREEN)
clock = pygame.time.Clock()

font = pygame.font.Font("./Content/Adlanta.ttf",90)
font2 = pygame.font.Font("./Content/Adlanta.ttf",70)
font_color=(255,255,255)

def Menu_List():
  screen.blit(Move_1,Move1_pos)
  screen.blit(Move_2,Move2_pos)
  screen.blit(Move_3,Move3_pos)
  screen.blit(Move_4,Move4_pos)

def Cursor(select):
  if select == 1:
    cursor_l = Move1_pos.center
  if select == 2:
    cursor_l = Move2_pos.center
  if select == 3:
    cursor_l = Move3_pos.center
  if select == 4:
    cursor_l = Move4_pos.center
  font = pygame.font.Font("./Content/Adlanta.ttf",150)
  Move = font.render(">            <",True,(255,255,255))
  Cursor_rect = Move.get_rect(center = cursor_l)
  screen.blit(Move,Cursor_rect)

def allowed():
  X,Y = pygame.mouse.get_pos()
  Yb = Move4_pos.bottom
  Xr = Move2_pos.right
  Xl = Move2_pos.left
  Yt = Move1_pos.top
  if 619<X<1301 and Yt<Y<Yb:
    return True
  else:
    return False

def selection_mode():
  X,Y = pygame.mouse.get_pos()
  ## SELECTION FIELD WITH MOUSE ##
  Y1 = Move1_pos.top
  Y2 = Move2_pos.top
  Y3 = Move3_pos.top
  Y4 = Move4_pos.top
  Y5 = Move4_pos.bottom
  if 619 < X < 1301 and Y1 <= Y < Y2:
    Z =1
  if 619 < X < 1301 and Y2 <= Y < Y3:
    Z =2
  if 619 < X < 1301 and Y3 <= Y < Y4:
    Z =3
  if 619 < X < 1301 and Y4 <= Y <= Y5:
    Z =4
  return Z

Menu_select = 1
selection_num = 1
Run = True
while Run:
  if selection_num == 1:
    Move_1=font.render("Vs Player",True,font_color)
  if selection_num == 2:
    Move_2=font.render("Vs Computer",True,font_color)
  if selection_num == 3:
    Move_3=font.render("SETTING",True,font_color)
  if selection_num == 4:
    Move_4=font.render("EXIT",True,font_color)
  #######################################
  if selection_num != 1:
    Move_1=font2.render("Vs Player",True,font_color)
  if selection_num != 2:
    Move_2=font2.render("Vs Computer",True,font_color)
  if selection_num != 3:
    Move_3=font2.render("SETTING",True,font_color)
  if selection_num != 4:
    Move_4=font2.render("EXIT",True,font_color)
  #######################################
  Move1_pos = Move_1.get_rect(midtop = [960,540])
  Move2_pos = Move_2.get_rect(midtop = Move1_pos.midbottom)
  Move3_pos = Move_3.get_rect(midtop = Move2_pos.midbottom)
  Move4_pos = Move_4.get_rect(midtop = Move3_pos.midbottom)
  screen.fill((0,0,0))
  Menu_List()
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == pygame.BUTTON_LEFT:
        if allowed():
          Menu_select = selection_num
    if event.type == pygame.MOUSEMOTION:
      if allowed():
        selection_num = selection_mode()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
        Menu_select = selection_num
      if event.key == pygame.K_UP:
        if selection_num > 1:
          selection_num -= 1
      if event.key == pygame.K_DOWN :
        if selection_num < 4:
          selection_num += 1
  Cursor(selection_num)
  ### Menu Section 
  if Menu_select == 1:
    Play(screen,screen_width,screen_height)
    Run = False
  if Menu_select == 2:
    Computer(screen,screen_width,screen_height)
    Run = False
  if Menu_select == 4:
    Run = False
  pygame.display.update()
  clock.tick()
pygame.quit()
