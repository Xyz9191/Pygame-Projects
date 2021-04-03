import pygame, sys, math 
pygame.init()

win = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Make your Army Win!')

class Team:
    def __init__(self, x, y, name, military):
        self.military = military
        rect = []
        self.rect = rect
        self.name = name
        self.x = x
        self.y = y
        lst = []
        self.lst = lst
        for i in range(5):
            self.military = pygame.image.load(military)
            self.military.set_colorkey((255, 255, 255))
            self.lst.append(self.military)
            self.rect.append(pygame.Rect(self.x, self.y, 18, 34))
            self.y += 65
    def draw(self, win, rx, ry):
        render(self.name, rx, ry, 25)
        x = 0
        for img in self.lst:
            
            win.blit(img, (self.rect[x].x, self.rect[x].y))
            if x < len(self.lst):
                x += 1 
            elif x == len(self.lst):
                x = 0

def Game_over(who_won, t1, t2):
    t1.rect = []
    t1.lst = []
    t2.rect = []
    t2.lst = []
    t1.name = ''
    t2.name = ''
    
    if who_won == 'team1':
        render(team1_name + ' Wins', 300, 250, 35)
    if who_won == 'team2':
        render(team2_name + 'Wins', 300, 250, 35)
    render('press \'R\' to restart', 300, 300, 20)
    
            
def render(text, x, y, size):
    text_obj = pygame.font.Font('freesansbold.ttf', size)
    text_surf = text_obj.render(text, True , (0, 0, 0))
    text_rect = text_surf.get_rect()
    text_rect.center = (x, y)
    win.blit(text_surf, text_rect)

team1_name = 'Blue Team'
team2_name = 'Red Team' 
t1 = Team(30, 95, team1_name, 'military.png')
t2 = Team(540, 95, team2_name, 'military1.png')
clicked = False
clicked_pos = ()
rect_clicked = False
shoot = False
current_move = 'team1'
clock = pygame.time.Clock()
shoot_pos = ()
who_won = None
game_over = False

while True:
    win.fill((10, 255, 10))
    t1.draw(win, 65, 20)
    t2.draw(win, 515, 20)

    pos = pygame.mouse.get_pos()
    for rect in t1.rect:
        if rect.collidepoint(pos):
            pygame.draw.rect(win, (0, 0, 0), (rect.x, rect.y, rect.width, rect.height), 2)
        if clicked is True and current_move == 'team1':
            if rect.collidepoint(clicked_pos):
                selected_rect = rect
                rect_clicked = True
                if shoot is True:
                    rect.x = shoot_pos[0]
                    rect.y = shoot_pos[1] - 17
                    shoot = False
                    rect_clicked = False
                    clicked = False
                    current_move = 'team2'
                    
    for rect in t2.rect:
        if rect.collidepoint(pos):
            pygame.draw.rect(win, (0, 0, 0), (rect.x, rect.y, rect.width, rect.height), 2)
        if clicked is True and current_move == 'team2':
            if rect.collidepoint(clicked_pos):
                selected_rect = rect
                rect_clicked = True
                
                if shoot is True:
                    rect.x = shoot_pos[0]
                    rect.y = shoot_pos[1] - 17
                    shoot = False
                    rect_clicked = False
                    clicked = False
                    current_move = 'team1'

    if rect_clicked is True:
        xcomp = pos[0] - selected_rect.right
        ycomp = pos[1] - selected_rect.top + 17
        linelength = math.sqrt(xcomp**2 + ycomp**2)
        if linelength <= 150:
            pygame.draw.line(win, (0, 0, 0), (selected_rect.x + 10, selected_rect.y + 17), (pos))

    for rect1 in t1.rect:
        for rect2 in t2.rect:
            if rect2.colliderect(rect1):
                if current_move == 'team1':
                    t1.rect.remove(rect1)
                    t1.lst.remove(t1.lst[0])
                elif current_move == 'team2':
                    t2.rect.remove(rect2)
                    t2.lst.remove(t2.lst[0])
    if len(t1.rect) == 0:
        who_won = 'team2'
        game_over = True
    if len(t2.rect) == 0:
        who_won = 'team1'
        game_over = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if rect_clicked is False and event.type == pygame.MOUSEBUTTONUP:
            clicked_pos = pygame.mouse.get_pos()
            if clicked is False:
                clicked = True
            elif clicked is True:
                clicked = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if rect_clicked is True:
                    if linelength <= 150:
                        shoot_pos = pygame.mouse.get_pos()
                        shoot = True
    if game_over:
        Game_over(who_won, t1, t2)
                        
    clock.tick(60)
    pygame.display.update()







    
