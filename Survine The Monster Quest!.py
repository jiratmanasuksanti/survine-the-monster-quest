import pygame
import random
import math
import sys
import pickle
pygame.init()
#################
Width = 900
Height = 700
screen = pygame.display.set_mode((Width,Height))
fullscreenx = Width/2
fullscreeny = Height/2
fullscreen_images = pygame.image.load("assets/images/start_menu/fullscreen_button.png")
click = False
while Click == False:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      click = True
      screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        click = True
  screen.blit(fullscreen_images,(fullscreenx,fullscreeny))
  pygame.display.update()
