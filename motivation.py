import pygame, sys

pygame.init()

win = pygame.display.set_mode((1000, 650))


def main():
    while True:
        win.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        m1 = 'Bhai sahab U-14 aur U-16 State Khelna hai'
        m2 = 'U-16 ke liye sirf 7 mahine baaki hai bhai'
        m3 = 'pura jor laga ke khelna hai'
        m4 = 'your dream will come TRUE'
        m5 = 'BUT'
        m6 = 'KEEP WORKING HARD'
        m7 = 'KUMON!!!!!!'
        m8 = 'THIS IS YOUR ULTIMATE MOTIVATION!!!'
        m9 = 'AAG LAGA DO!!!'
        motivation(m1, 500, 50)
        motivation(m2, 500, 100)
        motivation(m3, 500, 150)
        motivation(m4, 500, 200)
        motivation(m5, 500, 250)
        motivation(m6, 500, 300)
        motivation(m7, 500, 350)
        motivation(m8, 500, 400)
        motivation(m9, 500, 450)
        pygame.display.update()


def motivation(m, x, y):
    
    text_obj = pygame.font.Font('freesansbold.ttf', 35)
    text_surf = text_obj.render(m, True , (0, 0, 0))
    text_rect = text_surf.get_rect()
    text_rect.center = (x, y)
    win.blit(text_surf, text_rect)

    
    
main()  
    
