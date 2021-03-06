import pygame

pygame.init() #초기화
#화면크기
screen_width = 480 #가로크기
screen_height = 600 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("Gyuddi game") #게임이름


# 배경이미지 불러오기
background = pygame.image.load("C:/Users/한규현/Desktop/기타/pythonworkspace/pygame_basic/background.png")


#케릭터 불러오기
character = pygame.image.load("C:/Users/한규현/Desktop/기타/pythonworkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2) #화면 중간에 위치
character_y_pos = screen_height-character_height #화면 가장 아래

#이동할 좌표
to_x = 0
to_y = 0

#이벤트 루프
running = True #게임이 진행중인가
while running:  
    for event in pygame.event.get(): #어떤 이벤트인가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생했는가?
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 2
            if event.key == pygame.K_RIGHT:
                to_x += 2
            if event.key == pygame.K_UP:
                to_y -= 2
            if event.key == pygame.K_DOWN:
                to_y += 2

        if event.type == pygame.KEYUP:          
             if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                to_x = 0
             if event.key == pygame.K_UP or  event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y
    #가로 경계값
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width 

    #세로경계값
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height 
                

    screen.blit(background,(0,0))  #배경 그리기

    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update() #게임화면 다시그리기       
 #게임종료
pygame.quit()