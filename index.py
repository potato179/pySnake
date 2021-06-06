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
level = 0 # 레벨 저장
Calculation = 0 # 계산 저장
(height, width) = (20, 20) # 가로 세로 길이

################################ 음식 생성 함수 ################################
def createFood():   # 음식생성 함수 선언
    while True: # 계속 반복하기
        location = (random.randint(0, width-1), random.randint(0, height-1)) # 난수 생성(가로: 0부터 19까지 난수 생성, 세로: 0부터 19까지 난수 생성)
        if location in food or location in snake: # 해당 위치에 뱀 또는 음식이 있는지 판단
            continue    # 반복문 다시 실행
        food.append(location) # 음식 리스트에 해당 위치 추가
        break   # 반복문 종료

################################ 음식 배치 함수 ################################
def locateFood(location):   # 음식위치 함수 선언
    delete = food.index(location)   # 음식이 위치 칮기
    del food[delete] # 해당 위치에 음식이 존재할 경우 삭제
    createFood()    # 음식생성 함수 호출

################################ GUI 관련 함수 ################################
def draw(scoreboard,endmessage):    # 그리기 함수 선언
    display.fill((0, 0, 0)) # 단색으로 배경 채우기

    for i in food:  # 음식 리스트 만큼 실행하기
        pygame.draw.ellipse(display, (255, 255, 255), Rect(i[0]*30, i[1]*30, 30, 30)) # 음식(원 모양) 그리기

    for i in snake: # 뱀 리스트 만큼 실행하기
        pygame.draw.rect(display, (50, 100, 50), Rect(i[0]*30, i[1]*30, 30, 30)) # 뱀(사각형 모양) 그리기
    
    if endmessage != None:  # 종료메시지가 없다면
        display.blit(endmessage, (100, 300)) # 해당 좌표에 종료 메시지 띄우기

    if scoreboard != None:  # 점수판이 없다면
        display.blit(scoreboard, (10,10))  # 해당 좌표에 종료 메시지 띄우기
    
    pygame.display.update() # 실행 코드 업데이트

################################ 주 실행 코드 ################################
key = K_UP # 최초 실행 했을 때 위로 올라가게 동작 정하기
endmessage = None # 게임 종료 메시지
gameend = False # 게임 종류 여부
score = 0 # 점수
myfont = pygame.font.SysFont("malgungothic", 30)    # 글꼴 설정

snake.append((int(width/2), int(height/2))) # 화면 중앙 부터 뱀 꼬리 만들기

for i in range(10): # 10번 반복하기
    createFood() # 음식 생성 함수 호출

while True: # 계속 반복하기
    # 이벤트가 발생했을 때 동작 코드
    for i in pygame.event.get(): # 이벤트가 발생했을때
        if i.type == QUIT:  # 그 이벤트가 종료러면
            pygame.quit()   # 종료함수
            sys.exit() # 게임이 종료되었을 때 pygame과 시스템 종료하기
        elif i.type == KEYDOWN: # 아니면 키가 눌렸는가
            key = i.key # key 함수에 해당키 저장
    
    if not gameend: # 게임종료가 False라면
        if key == K_LEFT:   # 만약에 왼쪽키가 눌렸으면
            body = (snake[0][0]-1, snake[0][1]) # x측에 1을 빼서 한 칸 왼쪽으로 이동
        elif key == K_RIGHT:    # 만약에 오른쪽키가 눌렸으면
            body = (snake[0][0]+1, snake[0][1]) # x측에 1을 더해서 한 칸 오른쪽으로 이동
        elif key == K_UP:   # 만약에 위쪽키가 눌렸으면
            body = (snake[0][0], snake[0][1]-1) # y측에 1을 빼서 한 칸 위쪽으로 이동
        elif key == K_DOWN: # 만약에 아래쪽키가 눌렸으면
            body = (snake[0][0], snake[0][1]+1) # y측에 1을 더해서 한 칸 아래쪽으로 이동

        if body in snake or body[0] < 0 or body[0] >= height or body[1] < 0 or body[1] >= width:    # 만약에 뱀이 자신의 몸이나 벽에 나았으면
            endmessage = myfont.render("게임이 종료되었습니다. 점수: "+ str(score) + "점", True, (255, 255, 0)) # 게임 종료 메시지 설정
            gameend = True # 게임 종류 여부 참으로 전환
        scoreboard = myfont.render("점수 : "+str(score),"점",True,(255,255,255))   # 점수 메시지 설정
        snake.insert(0, body)   # 뱀에 몸 추가하기
        if body in food:    # 뱀에 음식에 닿으면
            locateFood(body)    # 음식위치에 몸 추가하기
            score += 1  # 점수에 1 더하기
        else:   # 아니면
            snake.pop() # 뱀의 꼬리 삭제하기

    if score / 10 == 1+Calculation: # 점수가 10 단위마다
        level += 1  # 레벨에 1 더하기
        Calculation +=1 # 계산에 1 더하기


    draw(scoreboard,endmessage) # 그리기 함수 호출
    timer.tick(5+level) # 초당 5프레임