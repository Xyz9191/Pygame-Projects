import pygame, sys, random
pygame.init()

win = pygame.display.set_mode((500, 500))
white = (255, 255, 255)
black = (0, 0, 0)
blue = (94, 244, 255)
lightPink = (255, 100, 200)
yellow = (255, 240, 60)

class PlayerShip:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw_ship(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, white, (self.x + 16, self.y - 25, 15, 25))

class EnemyShip:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def draw_enemy(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

class Bullet:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw_bullet(self, win):
        pygame.draw.rect(win, white, (self.x, self.y, self.width, self.height))

def render(text, size, centerx, centery):
    textsurf = pygame.font.Font('freesansbold.ttf', size)
    textobj = textsurf.render(text, True, white)
    textrect = textobj.get_rect()
    textrect.center = centerx, centery
    win.blit(textobj, textrect)

def wave(wave_num):
    render('Wave ' + str(wave_num), 30, 250, 250)

px, py, pwidth, pheight = 220, 285, 45, 10
bx, by, bwidth, bheight = 0, 0, 5, 10

brect = pygame.Rect(bx, by, bwidth, bheight)
prect = pygame.Rect(px, py, pwidth, pheight)
ps = PlayerShip(blue, *prect)
bs = Bullet(*brect)

velx = 0
vely = 0

wave_num = 1
wave_length = 5
enemy_list = []
enemy_list2 = []
enemy_list3 = []

Bool = True
shoot = False
list_filled = False
gameover = False
i = 0
x = 0
k = 0
incr = 1
score = 0
clock = pygame.time.Clock()
kinc = True

while True:
    win.fill(black)
    ps.draw_ship(win)
    render('Score : ' + str(score), 20, 39, 30)
    
    if Bool is True:
        wave(wave_num)
        i += 0.1
        if i >= 10:
            Bool = False
            i = 0
    if shoot is True:
        bs.draw_bullet(win)
        bs.y -= 15
        
        
        if bs.y <= -10:
            shoot = False

    if list_filled is False:
        for x in range(wave_length):
            ex = random.randint(0, 450)
            ey, ewidth, eheight = -5, 30, 10
            e_rect = pygame.Rect(ex, ey, ewidth, eheight)
            es = EnemyShip(yellow, *e_rect)
            enemy_list.append(es)
            x += 1
            if len(enemy_list) >= wave_length:
                list_filled = True
                kinc = True

    if k >= 10:
        if Bool is False:
            enemy_list2.append(enemy_list[0])
            enemy_list.pop(0)
            k = 0
            if len(enemy_list) == 0:
                kinc = False
            
    for enemy in enemy_list2:
        enemy.draw_enemy(win)
        enemy.y += incr
        if enemy.y >= 500:
            gameover = True

    for enemy in enemy_list2:
        b_rect = pygame.Rect(bs.x, bs.y, bs.width, bs.height)
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        if enemy_rect.colliderect(b_rect):
            enemy_list2.remove(enemy)
            score += 1
            shoot = False
        if len(enemy_list2) == 0:
            wave_length += 5
            if incr != 2:
                incr += 1
            else:
                incr += 0
            wave_num += 1
            Bool = True
            list_filled = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                vely = -5
            if event.key == pygame.K_DOWN:
                vely = 5
            if event.key == pygame.K_LEFT:
                velx = -5
            if event.key == pygame.K_RIGHT:
                velx = 5
            if shoot is False:
                if event.key == pygame.K_SPACE:
                    bs.x = ps.x + 22
                    bs.y = ps.y - 35
                    shoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                vely = 0
            if event.key == pygame.K_DOWN:
                vely = 0
            if event.key == pygame.K_LEFT:
                velx = 0
            if event.key == pygame.K_RIGHT:
                velx = 0
    ps.x += velx
    ps.y += vely

    if gameover is True:
        wave_num = 1
        wave_length = 5
        enemy_list = []
        enemy_list2 = []
        enemy_list3 = []
        i = 0
        x = 0
        k = 0
        incr = 1
        score = 0
        Bool = True
        shoot = False
        list_filled = False
        kinc = False
        gameover = False
    
    if kinc is True:
        k += 0.2
    else:
        k = 0
    if ps.x <= 0 :
        velx = 0
    if 500 - ps.x <= 45:
        velx = 0
    clock.tick(60)
    pygame.display.update()
