import pygame

#초기화 (반드시 필요)
pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#배경 이미지 불러오기
background = pygame.image.load("/Users/joseongbeom/Desktop/프로그래밍/pygame_basic/background.png")

#화면 타이틀 설정
pygame.display.set_caption("Bombom Game")

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님
    
    screen.fill((0,0,255))
    #screen.blit(background, (0,0))

    pygame.display.update()


pygame.quit()