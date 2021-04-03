import pygame, sys, random
pygame.init()

win = pygame.display.set_mode((600, 600))

def render(text, x, y, size):
    text_obj = pygame.font.Font('freesansbold.ttf', size)
    text_surf = text_obj.render(text, True , (0, 0, 0))
    text_rect = text_surf.get_rect()
    text_rect.center = (x, y)
    win.blit(text_surf, text_rect)

def Lines():
    pygame.draw.line(win, (0, 0, 0), (200, 0), (200, 600))
    pygame.draw.line(win, (0, 0, 0), (400, 0), (400, 600))
    pygame.draw.line(win, (0, 0, 0), (0, 200), (600, 200))
    pygame.draw.line(win, (0, 0, 0), (0, 400), (600, 400))
def Choose():
    render('Press \'S\' to Start', 300, 250, 50)
    render('Else press \'B\'', 300, 400, 50)
def generate_num(k):
    k = random.randint(1, 9)

choosed = False
clicked = False
x = pygame.image.load('tic_tac_toe-x.png')
o = pygame.image.load('tic_tac_toe-o.png')
player_sign = None
clicked_pos = ()
box_list = []
rect_list = []
current_move = ''
box1, box2, box3, box4, box5, box6, box7, box8, box9 = '', '', '', '', '', '', '', '', ''
label_pos_list = [(10, 10), (210, 10), (410, 10), (10, 210), (210, 210), (410, 210), (10, 410), (210, 410), (410, 410)]
occupied_list = []
l = 0


while True:
    win.fill((255, 255, 255))
    box_label_list = [box1, box2, box3, box4, box5, box6, box7, box8, box9]
    pos = pygame.mouse.get_pos()
    if choosed is False:
        Choose()
    Lines()
    if clicked is True and current_move == 'player':
        box_x = clicked_pos[0]//200 + 1
        box_y = clicked_pos[1]//200 + 1
        box_tuple = (box_x, box_y)
        if box_tuple == (1, 1):
            occupied_list.append(1)
            box1 = current_move
            clicked = False
            current_move = 'bot'
        elif box_tuple == (2, 1):
            occupied_list.append(2)
            box2 = current_move
            clicked = False
            current_move = 'bot'
        elif box_tuple == (3, 1):
            occupied_list.append(3)
            box3 = current_move
            clicked = False
            current_move = 'bot'
        elif box_tuple == (1, 2):
            occupied_list.append(4)
            box4 = current_move
            clicked = False
            current_move = 'bot'
        elif box_tuple == (2, 2):
            occupied_list.append(5)
            box5 = current_move
            clicked = False
            current_move = 'bot'
        elif box_tuple == (3, 2):
            occupied_list.append(6)
            box6 = current_move
            clicked = False
            current_move = 'bot'
        elif box_tuple == (1, 3):
            occupied_list.append(7)
            box7 = current_move
            clicked = False
            current_move = 'bot'
        elif box_tuple == (2, 3):
            occupied_list.append(8)
            box8 = current_move
            clicked = False
            current_move = 'bot'
        elif box_tuple == (3, 3):
            occupied_list.append(9)
            box9 = current_move
            clicked = False
            current_move = 'bot'

    if current_move == 'bot':
        l = random.randint(1, 9)
        if l not in occupied_list:
            box_list.append(l)
            occupied_list.append(l)
            current_move = 'player'

    for num in box_list: #getting whether box is playersign or botsign
        if num == 1:
            box1 = 'bot'
        if num == 2:
            box2 = 'bot'
        if num == 3:
            box3 = 'bot'
        if num == 4:
            box4 = 'bot'
        if num == 5:
            box5 = 'bot'
        if num == 6:
            box6 = 'bot'
        if num == 7:
            box7 = 'bot'
        if num == 8:
            box8 = 'bot'
        if num == 9:
            box9 = 'bot'

    for x1 in range(9): #blitting image
        if box_label_list[x1] == 'bot':
            win.blit(bot_sign, label_pos_list[x1])
        if box_label_list[x1] == 'player':
            win.blit(player_sign, label_pos_list[x1])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if choosed is False:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    current_move = 'player'
                    player_sign = x
                    bot_sign = o
                    choosed = True
                elif event.key == pygame.K_b:
                    current_move = 'bot'
                    player_sign = o
                    bot_sign = x
                    choosed = True
                    
        if event.type == pygame.MOUSEBUTTONUP and choosed is True and current_move == 'player':
            clicked = True
            clicked_pos = pos
    
    print(l)                     
    pygame.display.update()
    
