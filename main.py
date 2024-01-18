import pygame
from random import randint as r

time = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 400))
icon = pygame.image.load('images/icon.png')

player = pygame.image.load('images/1.png')
walk_left = [
    pygame.image.load('images/left/1.png'),
    pygame.image.load('images/left/2.png'),
    pygame.image.load('images/left/3.png'),
    pygame.image.load('images/left/4.png')
]
walk_right = [
    pygame.image.load('images/right/1.png'),
    pygame.image.load('images/right/2.png'),
    pygame.image.load('images/right/3.png'),
    pygame.image.load('images/right/4.png')
]
player_x = 120
player_y = 200
player_speed = 10
player_anim_count = 0
is_jump = False
jump_count = 12
player_life = 3
last_shot_time = pygame.time.get_ticks()
fire_rate = 2000

sceletons = [
    pygame.image.load('images/sceletons/1.png'),
    pygame.image.load('images/sceletons/2.png'),
    pygame.image.load('images/sceletons/3.png'),
    pygame.image.load('images/sceletons/4.png'),
    pygame.image.load('images/sceletons/5.png'),
    pygame.image.load('images/sceletons/6.png'),
    pygame.image.load('images/sceletons/7.png'),
    pygame.image.load('images/sceletons/8.png'),
    pygame.image.load('images/sceletons/9.png'),
    pygame.image.load('images/sceletons/10.png'),
    pygame.image.load('images/sceletons/11.png'),
    pygame.image.load('images/sceletons/12.png'),
    pygame.image.load('images/sceletons/13.png'),
    pygame.image.load('images/sceletons/14.png'),
    pygame.image.load('images/sceletons/15.png'),
    pygame.image.load('images/sceletons/16.png'),
    pygame.image.load('images/sceletons/17.png'),
    pygame.image.load('images/sceletons/18.png'),
]
sceletons_anim_count = 0
sceletons_list = []
sceletons_rect_x = 801
sceletons_speed = 4

fire = [
    pygame.image.load('images/arrow/1.png'),
    pygame.image.load('images/arrow/2.png'),
    pygame.image.load('images/arrow/3.png'),
    pygame.image.load('images/arrow/4.png'),
    pygame.image.load('images/arrow/5.png'),
    pygame.image.load('images/arrow/6.png'),
    pygame.image.load('images/arrow/7.png'),
    pygame.image.load('images/arrow/8.png'),
]
fire_list = []
fire_anim_count = 0
fire_speed = 12

money = [
    pygame.image.load('images/money/1.png'),
    pygame.image.load('images/money/2.png'),
    pygame.image.load('images/money/3.png'),
    pygame.image.load('images/money/4.png'),
    pygame.image.load('images/money/5.png'),
    pygame.image.load('images/money/6.png')
]
money_list = []
money_anim_count = 0
money_speed = 10
money_count = 30
points = 0

bg = pygame.image.load('images/bg.jpg')
bg_x = 0
bg_lose = pygame.image.load('images/bg_lose.png')
labal_font = pygame.font.Font('font/Old-Soviet.otf', 40)
labal_victory = labal_font.render('Вы выйграли!', False, (193, 196, 199))
labal_lose = labal_font.render('Вы проиграли', False, (193, 196, 199))
labal_restart = labal_font.render('Нажмите R чтобы начать занаво', False, (193, 196, 199))
hearts = [
    pygame.image.load('images/heart/1.png'),
    pygame.image.load('images/heart/1.png'),
    pygame.image.load('images/heart/1.png'),
    pygame.image.load('images/heart/1.png'),
    pygame.image.load('images/heart/1.png'),
    pygame.image.load('images/heart/2.png'),
    pygame.image.load('images/heart/3.png'),
    pygame.image.load('images/heart/2.png'),
    pygame.image.load('images/heart/3.png'),

]
heart_anim_count = 0

pygame.display.set_icon(icon)

game_over = False
intro_screen = True

running = True
paused = False
while running:
    while intro_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                intro_screen = False
                pygame.quit()

        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 36)
        play_text = font.render('Играть', True, (255, 255, 255))
        play_rect = play_text.get_rect(center=(400, 200))
        screen.blit(play_text, play_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                intro_screen = False
    labal_life = labal_font.render(str(player_life), False, (193, 196, 199))
    labal_points = labal_font.render(str(points) + '(30)', False, (193, 196, 199))

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 800, 0))
    screen.blit(bg, (bg_x - 800, 0))
    screen.blit(labal_life, (80, 10))
    screen.blit(hearts[heart_anim_count], (10, 10))
    screen.blit(labal_points, (600, 10))

    if player_life <= 0:
        screen.blit(bg_lose, (0, 0))
        screen.blit(labal_lose, (200, 200))
        screen.blit(labal_restart, (0, 300))

        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                player_life = 3
                player_x = 120
                player_y = 200
                points = 0
                game_over = False
                break

    player_rect = player.get_rect(topleft=(player_x, player_y))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and player_x > 50:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
        player_x -= player_speed
        bg_x += player_speed - 2
        if bg_x == 800:
            bg_x = 0
    elif keys[pygame.K_d] and player_x < 720:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
        player_x += player_speed
        bg_x -= player_speed - 2
        if bg_x == -800:
            bg_x = 0
    else:
        screen.blit(player, (player_x, player_y))

    if keys[pygame.K_e]:
        current_time = pygame.time.get_ticks()

        if current_time - last_shot_time >= fire_rate:
            fire_list.append(fire[fire_anim_count].get_rect(topleft=(player_x + 80, player_y + 60)))
            last_shot_time = current_time
    if fire_list:
        for (i, fire_idx) in enumerate(fire_list):
            screen.blit(fire[fire_anim_count], fire_idx)
            fire_idx.x += fire_speed

            if sceletons_list:
                for (i2, sceleton_idx) in enumerate(sceletons_list):
                    if fire_idx.colliderect(sceleton_idx):
                        fire_list.pop(i)
                        sceletons_list.pop(i2)

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -12:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 2
        else:
            is_jump = False
            jump_count = 12

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    if sceletons_anim_count == 17:
        sceletons_anim_count = 0
    else:
        sceletons_anim_count += 1

    if heart_anim_count == 8:
        heart_anim_count = 0
    else:
        heart_anim_count += 1
    if fire_anim_count == 7:
        fire_anim_count = 0
    else:
        fire_anim_count += 1
    if money_anim_count == 5:
        money_anim_count = 0
    else:
        money_anim_count += 1

    check = r(0, 60)
    if check == 2 and sceletons_rect_x > 0:  # Check that skeletons are spawned on the right side
        sceletons_list.append(sceletons[sceletons_anim_count].get_rect(topleft=(sceletons_rect_x, 200)))
        sceletons_rect_x -= 4

    if sceletons_list:
        for i in sceletons_list:
            screen.blit(sceletons[sceletons_anim_count], i)
            i.x -= sceletons_speed
            if player_rect.colliderect(i):
                player_life -= 1
                player_x = 100
                sceletons_list.pop(0)

    check_money = r(10, 750)
    check_time = r(0, 100)
    if money_count > 0:
        if check_time == 5:
            money_list.append(money[money_anim_count].get_rect(topleft=(check_money, 0)))
            money_count -= 1
    if money_list:
        for (i, money_idx) in enumerate(money_list):
            screen.blit(money[money_anim_count], money_idx)
            if money_idx.y <= 230:
                money_idx.y += money_speed
            if money_idx.colliderect(player_rect):
                money_list.pop(i)
                points += 1

    pygame.display.update()
    victory_condition = 30

    if points >= victory_condition:
        screen.fill((0, 0, 0))  # Fill the screen with a black background
        screen.blit(labal_victory, (200, 200))
        screen.blit(labal_restart, (0, 300))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                player_life = 3
                player_x = 120
                player_y = 200
                points = 0
                game_over = False
                break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        player_life = 3
        player_x = 120
        player_y = 200
        points = 0
        game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    time.tick(15)
