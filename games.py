import pygame
#from menu.py import walkRight, walkLeft, idle

pygame.init()
wight_window = 1000
height_window = 563
play_window = pygame.display.set_mode((wight_window, height_window))

pygame.display.set_caption('Golems_Rush')

walkRight = [pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_00.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_01.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_02.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_03.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_04.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_05.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_06.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_07.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_08.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_09.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_010.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_011.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_012.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_013.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_014.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_015.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_016.png'),
             pygame.image.load('sprites\Golem_Braun\walkRight\Walking_Right_017.png')]
walkLeft = [pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_00.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_01.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_02.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_03.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_04.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_05.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_06.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_07.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_08.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_09.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_010.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_011.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_012.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_013.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_014.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_015.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_016.png'),
            pygame.image.load('sprites\Golem_Braun\walkLeft\Walking_Left_017.png')]
idle = pygame.image.load('sprites\Golem_Braun\idle\Idle_0.png')

bg = pygame.image.load('R:\Projects_Python\Golems_Rush\_Night_copy.jpg')
bg_down = pygame.image.load('R:\Projects_Python\Golems_Rush\Bg_down.jpg')
soundJump = pygame.mixer.Sound('Jump.wav')

clock = pygame.time.Clock()

x = 0
y = 600 - 167 - 73
wight = 250
height = 167
speed = 6

isJump = False
jumpCount = 10

left = False
right = True
animCount = 0


def drawWindow():
    global animCount

    play_window.blit(bg, (0, 0))
    #play_window.blit(bg_down, (0, height_window - 83))
    #play_window.blit(bg_down, (500, height_window - 83))

    if animCount + 1 >= 119:
        animCount = 0

    if left:
        play_window.blit(walkLeft[animCount // 17], (x, y))
        animCount += 1
    elif right:
        play_window.blit(walkRight[animCount // 17], (x, y))
        animCount += 1
    else:
        play_window.blit(idle, (x, y))

    pygame.display.update()


run = True
while run:
    clock.tick(200)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1000 - wight - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0

    if not isJump:
        if keys[pygame.K_UP]:
            soundJump.play()
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:

                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()

pygame.quit()
