import pygame, sys

pygame.init()

win = pygame.display.set_mode((450, 550))
pygame.display.set_caption('TIC_TAC_TOE')

white = (255, 255, 255)
black = (0, 0, 0)

waiting = True
wait = 0
move = None
Box1, Box2, Box3, Box4, Box5, Box6, Box7, Box8, Box9 = None, None, None, None, None, None, None, None, None
box1, box2, box3, box4, box5, box6, box7, box8, box9 = '', '', '', '', '', '', '', '', ''

def main():
    global waiting
    k = 0
    i = 1
    inc = False
    while True:
        win.fill(white)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP and keys[pygame.K_1] or keys[pygame.K_2] or keys[pygame.K_3] or keys[pygame.K_4] or keys[pygame.K_5] or keys[pygame.K_6] or keys[pygame.K_7] or keys[pygame.K_8] or keys[pygame.K_9] :
                k += 1
                print(k)
                print(move)
        if k % 2 == 0:
            move = 'player1'
        elif k % 2 != 0:
            move = 'player2'
            
        draw_lines()
        gamePlay(move)
        if who_won():
            inc = True
        if inc is True:
            i += 1
            if i >= 100:
                redraw_board()
                inc = False
                i = 1

        pygame.display.update()

def draw_lines():
    pygame.draw.line(win, black, (0, 150), (450, 150))
    pygame.draw.line(win, black, (0, 300), (450, 300))
    pygame.draw.line(win, black, (150, 0), (150, 450))
    pygame.draw.line(win, black, (300, 0), (300, 450))

def box_1(x):
    text_surf = pygame.font.Font('freesansbold.ttf', 85)
    text_obj = text_surf.render(x, True, black)
    text_rect = text_obj.get_rect()
    text_rect.center = (75, 75)
    win.blit(text_obj, text_rect)

def box_2(x):
    text_surf = pygame.font.Font('freesansbold.ttf', 85)
    text_obj = text_surf.render(x, True, black)
    text_rect = text_obj.get_rect()
    text_rect.center = (225, 75)
    win.blit(text_obj, text_rect)

def box_3(x):
    text_surf = pygame.font.Font('freesansbold.ttf', 85)
    text_obj = text_surf.render(x, True, black)
    text_rect = text_obj.get_rect()
    text_rect.center = (375, 75)
    win.blit(text_obj, text_rect)

def box_4(x):
    text_surf = pygame.font.Font('freesansbold.ttf', 85)
    text_obj = text_surf.render(x, True, black)
    text_rect = text_obj.get_rect()
    text_rect.center = (75, 225)
    win.blit(text_obj, text_rect)

def box_5(x):
    text_surf = pygame.font.Font('freesansbold.ttf', 85)
    text_obj = text_surf.render(x, True, black)
    text_rect = text_obj.get_rect()
    text_rect.center = (225, 225)
    win.blit(text_obj, text_rect)

def box_6(x):
    text_surf = pygame.font.Font('freesansbold.ttf', 85)
    text_obj = text_surf.render(x, True, black)
    text_rect = text_obj.get_rect()
    text_rect.center = (375, 225)
    win.blit(text_obj, text_rect)

def box_7(x):
    text_surf = pygame.font.Font('freesansbold.ttf', 85)
    text_obj = text_surf.render(x, True, black)
    text_rect = text_obj.get_rect()
    text_rect.center = (75, 375)
    win.blit(text_obj, text_rect)

def box_8(x):
    text_surf = pygame.font.Font('freesansbold.ttf', 85)
    text_obj = text_surf.render(x, True, black)
    text_rect = text_obj.get_rect()
    text_rect.center = (225, 375)
    win.blit(text_obj, text_rect)

def box_9(x):
    text_surf = pygame.font.Font('freesansbold.ttf', 85)
    text_obj = text_surf.render(x, True, black)
    text_rect = text_obj.get_rect()
    text_rect.center = (375, 375)
    win.blit(text_obj, text_rect)

def gamePlay(moove):
    global Box1, Box2, Box3, Box4, Box5, Box6, Box7, Box8, Box9, box1, box2, box3, box4, box5, box6, box7, box8, box9, l, wait, waiting
    
    keys = pygame.key.get_pressed()
    disp = ''

    if waiting is True:
        disp = 'Plz Wait...'
        wait += 1
    if wait >= 50:
        waiting = False
        wait = 0
    
    if moove == 'player1' and waiting is False:
        disp = 'Player1'
        if keys[pygame.K_1] and Box1 is None:
            box1 = 'X'
            Box1 = True
            waiting = True
        if keys[pygame.K_2] and Box2 is None:
            box2 = 'X'
            Box2 = True
            waiting = True
        if keys[pygame.K_3] and Box3 is None:
            box3 = 'X'
            Box3 = True
            waiting = True
        if keys[pygame.K_4] and Box4 is None:
            box4 = 'X'
            Box4 = True
            waiting = True
        if keys[pygame.K_5] and Box5 is None:
            box5 = 'X'
            Box5 = True
            waiting = True
        if keys[pygame.K_6] and Box6 is None:
            box6 = 'X'
            Box6 = True
            waiting = True
        if keys[pygame.K_7] and Box7 is None:
            box7 = 'X'
            Box7 = True
            waiting = True
        if keys[pygame.K_8] and Box8 is None:
            box8 = 'X'
            Box8 = True
            waiting = True
        if keys[pygame.K_9] and Box9 is None:
            box9 = 'X'
            Box9 = True
            waiting = True

    if moove == 'player2' and waiting is False:
        disp = 'Player2'
        if keys[pygame.K_1] and Box1 is None:
            box1 = 'O'
            Box1 = True
            waiting = True
        if keys[pygame.K_2] and Box2 is None:
            box2 = 'O'
            Box2 = True
            waiting = True
        if keys[pygame.K_3] and Box3 is None:
            box3 = 'O'
            Box3 = True
            waiting = True
        if keys[pygame.K_4] and Box4 is None:
            box4 = 'O'
            Box4 = True
            waiting = True
        if keys[pygame.K_5] and Box5 is None:
            box5 = 'O'
            Box5 = True
            waiting = True
        if keys[pygame.K_6] and Box6 is None:
            box6 = 'O'
            Box6 = True
            waiting = True
        if keys[pygame.K_7] and Box7 is None:
            box7 = 'O'
            Box7 = True
            waiting = True
        if keys[pygame.K_8] and Box8 is None:
            box8 = 'O'
            Box8 = True
            waiting = True
        if keys[pygame.K_9] and Box9 is None:
            box9 = 'O'
            Box9 = True
            waiting = True

    if Box1 is True:
        box_1(box1)
    if Box2 is True:
        box_2(box2)
    if Box3 is True:
        box_3(box3)
    if Box4 is True:
        box_4(box4)
    if Box5 is True:
        box_5(box5)
    if Box6 is True:
        box_6(box6)
    if Box7 is True:
        box_7(box7)
    if Box8 is True:
        box_8(box8)
    if Box9 is True:
        box_9(box9)
    if who_won():
        disp = 'Game over' 
    text_surf = pygame.font.Font('freesansbold.ttf', 75)
    text_obj = text_surf.render(disp, True, black)
    text_rect = text_obj.get_rect()
    text_rect.center = (215, 510)
    win.blit(text_obj, text_rect)
        


def who_won():
    global Box1, Box2, Box3, Box4, Box5, Box6, Box7, Box8, Box9, box1, box2, box3, box4, box5, box6, box7, box8, box9

    if Box1 is True and Box2 is True and Box3 is True and box1 != '' and box2 != '' and box3 != '' and box1 == box2 and box2 == box3 and box1 == box3:
        return True
    if Box4 is True and Box5 is True and Box6 is True and box4 != '' and box5 != '' and box6 != '' and box4 == box5 and box5 == box6 and box4 == box6:
        return True
    if Box7 is True and Box8 is True and Box9 is True and box7 != '' and box8 != '' and box9 != '' and box7 == box8 and box8 == box9 and box7 == box9:
        return True
    if Box1 is True and Box4 is True and Box7 is True and box1 != '' and box4 != '' and box7 != '' and box1 == box4 and box4 == box7 and box1 == box7:
        return True
    if Box2 is True and Box5 is True and Box8 is True and box2 != '' and box5 != '' and box8 != '' and box2 == box5 and box5 == box8 and box2 == box8:
        return True
    if Box3 is True and Box6 is True and Box9 is True and box3 != '' and box6 != '' and box9 != '' and box3 == box6 and box6 == box9 and box3 == box9:
        return True
    if Box1 is True and Box5 is True and Box9 is True and box1 != '' and box5 != '' and box9 != '' and box1 == box5 and box5 == box9 and box1 == box9:
        return True
    if Box3 is True and Box5 is True and Box7 is True and box3 != '' and box5 != '' and box7 != '' and box3 == box5 and box5 == box7 and box3 == box7:
        return True
    return False

def redraw_board():
    global Box1, Box2, Box3, Box4, Box5, Box6, Box7, Box8, Box9, box1, box2, box3, box4, box5, box6, box7, box8, box9
    win.fill(white)
    Box1, Box2, Box3, Box4, Box5, Box6, Box7, Box8, Box9 = None, None, None, None, None, None, None, None, None
    box1, box2, box3, box4, box5, box6, box7, box8, box9 = '', '', '', '', '', '', '', '', ''

    draw_lines()
    gamePlay(move)

if __name__ == '__main__':
    main()





