import pygame
import os
###########################################################################
#기본 초기화!
pygame.init() #초기화
#화면크기
screen_width = 640 #가로크기
screen_height = 480 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀
pygame.display.set_caption("Gyuddi Pang") #게임이름

#FPS
clock = pygame.time.Clock()
############################################################################

# 1. 사용자 게임 초기화(배경,케릭터,폰트,좌표,속도 등 설정)
# current_path = os.path.dirname(__file__) #현재파일 위치 반환
image_path =os.path.dirname(__file__) #image 폴더 위치반환

#배경만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

stage =  pygame. image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

character = pygame. image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height - stage_height

#케릭터 이동방향
character_to_x = 0
#이동속도
character_speed = 5

#무기만들기
weapon =pygame. image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러발 발사 가능
weapons = []

#무기 이동속도
weapon_speed = 10



#공 만들기(4개 크기에 따라 따로처리)
ball_images = [
    pygame. image.load(os.path.join(image_path, "balloon1.png")),
    pygame. image.load(os.path.join(image_path, "balloon2.png")),
    pygame. image.load(os.path.join(image_path, "balloon3.png")),
    pygame. image.load(os.path.join(image_path, "balloon4.png"))
    ]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9]

#공들
balls = []
# 최초 발생하는 큰 공
balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0,
    "to_x": 3,
    "to_y": -6,
    "init_spd_y":ball_speed_y[0]  #y최초속도
})

running = True #게임이 진행중인가
while running:
    dt = clock.tick(100) #게임의 초당 프레임

    # 2. 이벤트 처리(키보드 마우스 등)
    for event in pygame.event.get(): #어떤 이벤트인가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생했는가?
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed            
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0




    #3. 게임케릭터 위치
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width 

    #무기 위치조절
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    weapons = [[w[0],w[1]] for w in weapons if w[1] > 0 ]

    #공 위치 정리
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_heigt = ball_size[1]


        #가로벽에 닿았을 때 공 위치 변경
        if ball_pos_x <= 0 or ball_pos_x > screen_width-ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1


        #세로벽
        if ball_pos_y >= screen_height - stage_height - ball_heigt:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5


        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
    #4.충돌처리

    #5.화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height - stage_height))
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))

    screen.blit(character,(character_x_pos,character_y_pos))


    pygame.display.update() #게임화면 다시그리기
pygame.quit()