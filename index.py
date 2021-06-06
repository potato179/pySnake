################################ 모듈 호출 및 정의 ################################
import pygame # 파이게임 불러오기
import sys # 시스템 불러오기
from pygame.locals import QUIT, Rect, KEYDOWN, K_DOWN, K_UP, K_LEFT, K_RIGHT # 게임 종료 , 직각 , 키 눌렸을때, 화살표 - 아래, 위, 왼쪽, 오른쪽
from pygame import *  # 파이게임에 모든 요소 불러오기
import random # 난수 불러오기

################################ 기본 구성 ################################
pygame.init() # 파이게임 초기화
display = pygame.display.set_mode((600, 600)) # 가로세로 600
timer = pygame.time.Clock()   # 시간 함수

food = [] # 음식 저장
snake = [] # 뱀 몸 저장
(height, width) = (20, 20) # 가로 세로 길이 

################################ 음식 생성 함수 ################################
def createFood():
    while True:
        location = (random.randint(0, width-1), random.randint(0, height-1)) # 난수 생성(가로: 0부터 19까지 난수 생성, 세로: 0부터 19까지 난수 생성)
        if location in food or location in snake: # 해당 위치에 뱀 또는 음식이 있는지 판단
            continue
        food.append(location) # 음식 리스트에 해당 위치 추가
        break

################################ 음식 배치 함수 ################################
def locateFood(location):
    delete = food.index(location) 
    del food[delete] # 해당 위치에 음식이 존재할 경우 삭제
    createFood()

################################ GUI 관련 함수 ################################
def draw(endmessage):
    display.fill((0, 0, 0)) # 단색으로 배경 채우기

    for i in food:
        pygame.draw.ellipse(display, (255, 255, 255), Rect(i[0]*30, i[1]*30, 30, 30)) # 음식(원 모양) 그리기

    for i in snake:
        pygame.draw.rect(display, (50, 100, 50), Rect(i[0]*30, i[1]*30, 30, 30)) # 뱀(사각형 모양) 그리기
    
    if endmessage != None:
        display.blit(endmessage, (100, 300)) # 해당 좌표에 종료 메시지 띄우기
    
    pygame.display.update() # 실행 코드 업데이트

################################ 주 실행 코드 ################################
key = K_UP # 최초 실행 했을 때 위로 올라가게 동작 정하기
endmessage = None # 게임 종료 메시지
gameend = False # 게임 종류 여부
score = 0 # 점수
myfont = pygame.font.SysFont("malgungothic", 30)

snake.append((int(width/2), int(height/2))) # 화면 중앙 부터 뱀 꼬리 만들기

for i in range(10):
    createFood() # 음식 생성 함수 호출

while True:
    # 이벤트가 발생했을 때 동작 코드
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            sys.exit() # 게임이 종료되었을 때 pygame과 시스템 종료하기
        elif i.type == KEYDOWN:
            key = i.key
    
    if not gameend:
        if key == K_LEFT:
            body = (snake[0][0]-1, snake[0][1]) # x측에 1을 빼서 한 칸 왼쪽으로 이동
        elif key == K_RIGHT:
            body = (snake[0][0]+1, snake[0][1]) # x측에 1을 더해서 한 칸 오른쪽으로 이동
        elif key == K_UP:
            body = (snake[0][0], snake[0][1]-1) # y측에 1을 빼서 한 칸 위쪽으로 이동
        elif key == K_DOWN:
            body = (snake[0][0], snake[0][1]+1) # y측에 1을 더해서 한 칸 아래쪽으로 이동

        if body in snake or body[0] < 0 or body[0] >= height or body[1] < 0 or body[1] >= width:
            endmessage = myfont.render("게임이 종료되었습니다. 점수: "+ str(score) + "점", True, (255, 255, 0)) # 게임 종료 메시지 설정
            gameend = True # 게임 종류 여부 참으로 전환
        
        snake.insert(0, body)
        if body in food:
            locateFood(body)
            score += 1
        else:
            snake.pop()
    
    draw(endmessage)
    timer.tick(5)