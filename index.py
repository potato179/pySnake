import pygame   # 파이게임 불러오기
import sys  # 시스템 불러오기
from pygame.locals import QUIT, Rect, KEYDOWN, K_DOWN, K_UP, K_LEFT, K_RIGHT
from pygame import *    # 파이게임에 모든 요소 불러오기
import random   # 난수 불러오기
pygame.init()   # 파이게임 초기화
display = pygame.display.set_mode( 600,600 ) # 가로세로 600
fps = pygame.time.Clock()   # 시간 함수

food = []
snake = []
(height, width) = (50, 50)
score = 0
gameend = 0
level = 0
t = 0


