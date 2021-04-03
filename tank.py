import pygame, sys, math
pygame.init()

win = pygame.display.set_mode((450, 550))
game_icon = pygame.image.load('gameicon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption('Tank Fight')
black = (0, 0, 0)
white = (255, 255, 255)

class Tank:
    def __init__(self, lives, ammo, x, y, img, name):
        self.name = name
        self.lives = lives
        self.ammo = ammo
        self.x = x
        self.y = y
        self.img = img
    def draw(self, win, angle):
        self.angle = angle
        img_copy = pygame.transform.rotate(self.img, self.angle)
        win.blit(img_copy, (int(self.x - img_copy.get_width() / 2), int(self.y - img_copy.get_height() / 2)))
        rect = pygame.Rect(self.x, self.y, 32, 32)
        self.rect = rect

class Ball:
    def __init__(self, x, y, img, shoot_angle):
        self.x = x
        self.y = y
        self.img = img
        self.shoot_angle = shoot_angle
    def draw_ball(self, win):
        win.blit(self.img, (self.x, self.y))
        rect = pygame.Rect(self.x, self.y, 16, 16)
        self.rect = rect

def render(text, size, centerx, centery):
    textsurf = pygame.font.Font('freesansbold.ttf', size)
    textobj = textsurf.render(text, True, black)
    textrect = textobj.get_rect()
    textrect.center = centerx, centery
    win.blit(textobj, textrect)

    
tank_img = pygame.image.load('tank.png')
ball1_img = pygame.image.load('circle.png')
ball2_img = pygame.image.load('circle(1).png')
red_heart = pygame.image.load('redheart.png').convert()
blue_heart = pygame.image.load('blueheart.png').convert()
blue_heart.set_colorkey((255, 255, 255))
red_heart.set_colorkey((255, 255, 255))

tank1 = Tank(5, 15, 20, 220, tank_img, 'Berry')
tank2 = Tank(5, 15, 400, 220, tank_img, 'Apple')
t1_lives_list = []
t2_lives_list = []

tank1_angle = 0
tank2_angle = 180

clock = pygame.time.Clock()

move_front = False
move_back = False
move_front1 = False
move_back1 = False

shoot1 = False
shoot_disabled = False
b1_list = []
b2_list = []
wall_list = [pygame.Rect(100, 50, 10, 100), pygame.Rect(100, 300, 10, 100), pygame.Rect(350, 50, 10, 100), pygame.Rect(350, 300, 10, 100)]

left_rect = pygame.Rect(-32, 0, 5, 450)
right_rect = pygame.Rect(482, 0, 1, 450)
up_rect = pygame.Rect(0, -32, 450, 5)
down_rect = pygame.Rect(0, 482, 450, 1)

angle_change = 0
angle1_change = 0

x_change = 0
y_change = 0
x1_change = 0
y1_change = 0

bx = 15
by = 500
b1x = 250
rx = 0
ry = 0
winner = ''

for i in range(tank1.lives):
    t1_lives_list.append(bx)
    bx += 35
for j in range(tank2.lives):
    t2_lives_list.append(b1x)
    b1x += 35

while True:
    win.fill((0, 216, 0))
    tank1.draw(win, tank1_angle)
    tank2.draw(win, tank2_angle)
    pygame.draw.rect(win, (0, 0, 0), (0, 450, 450, 5))
    render(tank1.name, 10, tank1.x, tank1.rect.top - 20)
    render(tank2.name, 10, tank2.x, tank2.rect.top - 20)
    render(tank1.name, 30, 90, 480)
    render(tank2.name, 30, 330, 480)
    
    if tank1_angle >= 325 and tank1_angle <= 360 or tank1_angle >= 0 and tank1_angle <= 45:
        tank1_facing = 'right'
    if tank1_angle >= 45 and tank1_angle <= 135:
        tank1_facing = 'up'
    if tank1_angle >= 135 and tank1_angle <= 225:
        tank1_facing = 'left'
    if tank1_angle >= 225 and tank1_angle <= 325:
        tank1_facing = 'down'

    for x in t1_lives_list:
        win.blit(blue_heart, (x, 500))
    for x1 in t2_lives_list:
        win.blit(red_heart, (x1, 500))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_front = True
            if event.key == pygame.K_s:
                move_back = True
            if event.key == pygame.K_d:
                angle_change = -4
            if event.key == pygame.K_a:
                angle_change = 4
            if not shoot_disabled:
                if event.key == pygame.K_e:
                    b1_list.append(Ball(tank1.rect.left , tank1.rect.top, ball1_img, tank1_angle))
                
            if event.key == pygame.K_UP:
                move_front1 = True
            if event.key == pygame.K_DOWN:
                move_back1 = True
            if event.key == pygame.K_RIGHT:
                angle1_change = -4
            if event.key == pygame.K_LEFT:
                angle1_change = 4
            if not shoot_disabled:
                if event.key == pygame.K_SPACE:
                    b2_list.append(Ball(tank2.rect.left , tank2.rect.top, ball2_img, tank2_angle))
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_front = False
                x_change = 0
                y_change = 0
            if event.key == pygame.K_s:
                move_back = False
                x_change = 0
                y_change = 0
            if event.key == pygame.K_d:
                angle_change = 0
            if event.key == pygame.K_a:
                angle_change = 0
                
            if event.key == pygame.K_UP:
                move_front1 = False
                x1_change = 0
                y1_change = 0
            if event.key == pygame.K_DOWN:
                move_back1 = False
                x1_change = 0
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                angle1_change = 0
            if event.key == pygame.K_LEFT:
                angle1_change = 0
            
    if move_front is True:
        x_change = int(5 * math.cos(math.radians(tank1_angle)))
        y_change = int(5 * math.sin(math.radians(tank1_angle)))

    if move_back is True:
        x_change = -1 * int(5 * math.cos(math.radians(tank1_angle)))
        y_change = -1 * int(5 * math.sin(math.radians(tank1_angle)))

    if move_front1 is True:
        x1_change = int(5 * math.cos(math.radians(tank2_angle)))
        y1_change = int(5 * math.sin(math.radians(tank2_angle)))

    if move_back1 is True:
        x1_change = -1 * int(5 * math.cos(math.radians(tank2_angle)))
        y1_change = -1 * int(5 * math.sin(math.radians(tank2_angle)))
        
    for ball in b1_list:
        ball.draw_ball(win)
        ball.x += int(8 * math.cos(math.radians(ball.shoot_angle)))
        ball.y -= int(8 * math.sin(math.radians(ball.shoot_angle)))
    for ball in b2_list:
        ball.draw_ball(win)
        ball.x += int(8 * math.cos(math.radians(ball.shoot_angle)))
        ball.y -= int(8 * math.sin(math.radians(ball.shoot_angle)))

    if len(b1_list) != 0: 
        for ball in b1_list:
            for ball1 in b2_list:
                if ball.rect.colliderect(ball1.rect):
                    b1_list.remove(ball)
                    b2_list.remove(ball1)
        for ball in b1_list:
            if not shoot_disabled:
                if ball.rect.colliderect(tank2.rect):
                    b1_list.remove(ball)
                    t2_lives_list.pop()
                
            if ball.x >= 450 or ball.y >= 450 or ball.x <= 0 or ball.y <= 0:
                b1_list.remove(ball)
    if len(b2_list) != 0:
        for ball in b2_list:
            if not shoot_disabled:
                if ball.rect.colliderect(tank1.rect):
                    b2_list.remove(ball)
                    t1_lives_list.pop()
            if ball.x >= 450 or ball.y >= 450 or ball.x <= 0 or ball.y <= 0:
                b2_list.remove(ball)
    for rect in wall_list:
        pygame.draw.rect(win, (0, 0, 0), rect)
        for ball in b1_list:
            if ball.rect.colliderect(rect):
                b1_list.remove(ball)
        for ball in b2_list:
            if ball.rect.colliderect(rect):
                b2_list.remove(ball)

    if tank1.rect.colliderect(left_rect):
        tank1.x = tank1.x + 450
    if tank1.rect.colliderect(right_rect):
        tank1.x = tank1.x - 450
    if tank1.rect.colliderect(up_rect):
        tank1.y = tank1.y + 450
    if tank1.rect.colliderect(down_rect):
        tank1.y = tank1.y - 450
    if tank2.rect.colliderect(left_rect):
        tank2.x = tank2.x + 450
    if tank2.rect.colliderect(right_rect):
        tank2.x = tank2.x - 450
    if tank2.rect.colliderect(up_rect):
        tank2.y = tank2.y + 450
    if tank2.rect.colliderect(down_rect):
        tank2.y = tank2.y - 450
    
    tank1.x += x_change
    tank1.y -= y_change
    tank1_angle += angle_change
    tank2.x += x1_change
    tank2.y -= y1_change
    tank2_angle += angle1_change
    
    if len(t1_lives_list) == 0:
        shoot_disabled = True
        winner = tank2.name
    if len(t2_lives_list) == 0:
        shoot_disabled = True
        winner = tank1.name
    if shoot_disabled:
        render(winner + ' Wins!', 35, 225, 275)
        render('Press R to Restart and Q to quit', 20, 225, 300)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            bx = 15
            b1x = 250
            t1_lives_list = []
            t2_lives_list = []
            for i in range(tank1.lives):
                t1_lives_list.append(bx)
                bx += 35
            for j in range(tank2.lives):
                t2_lives_list.append(b1x)
                b1x += 35
            tank1.x = 20
            tank1.y = 220
            tank2.x = 400
            tank2.y = 220
            shoot_disabled = False
            
    
    pygame.display.update()
    clock.tick(65)
