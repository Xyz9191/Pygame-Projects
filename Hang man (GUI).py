import pygame, sys, random
pygame.init()

win = pygame.display.set_mode((600, 600))

class Letter:
    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = x
        self.y = y
        text_obj = pygame.font.Font('freesansbold.ttf', 35)
        text_surf = text_obj.render(self.letter, True , (0, 0, 0), (144, 244, 255))
        text_rect = text_surf.get_rect()
        self.text_obj = text_obj
        self.text_surf = text_surf
        self.text_rect = text_rect
    def draw(self):
        self.text_rect.center = (self.x, self.y)
        win.blit(self.text_surf, self.text_rect)

class Word:
    def __init__(self, word):
        self.word = word
        found_list = []
        letter_list = []
        self.found_list = found_list
        self.letter_list = letter_list
        Word.define_letter(self)
        
    def define_letter(self):
        inc = 0
        for letter in self.word:
            self.found_list.append('not found')
            self.letter_list.append(pygame.Rect(150 + (inc*40), 200, 25, 40))
            inc += 1
    def draw(self):
        vowel_list = ['A', 'E', 'I', 'O', 'U']
        for x in range(0, len(self.word)):
            if self.found_list[x] == 'not found' and self.word[x] not in vowel_list:
                pygame.draw.rect(win, (0, 0, 0), self.letter_list[x], 3)
            elif self.found_list[x] == 'found' or self.word[x] in vowel_list:
                render(self.word[x], self.letter_list[x].x + 5, self.letter_list[x].y + 19, 35)

def render(text, x, y, size):
    text_obj = pygame.font.Font('freesansbold.ttf', size)
    text_surf = text_obj.render(text, True , (0, 0, 0))
    text_rect = text_surf.get_rect()
    text_rect.center = (x, y)
    win.blit(text_surf, text_rect)

lst = list('abcdefghijklmnopqrstuvwxyz'.upper())
words_lst = ['MATHS', 'PHYSICS', 'CHEMISTRY', 'BIOLOGY']
num = random.randint(0, 3)
word = Word(words_lst[num])
letters_list = []
hangman1 = pygame.image.load('hangman1.png')
hangman2 = pygame.image.load('hangman2.png')
hangman3 = pygame.image.load('hangman3.png')
hangman4 = pygame.image.load('hangman4.png')
hangman5 = pygame.image.load('hangman5.png')
hangman6 = pygame.image.load('hangman6.png')
hangman7 = pygame.image.load('hangman7.png')
error_list = ['1']
x = 0
y = 0
k = 25
error = 1
clicked = False
letter_clicked = False
won = False
lost = False
clicked_letter = ''
word_list = list(word.word)
text = 'click on your guess'

for letter in lst:
        letters_list.append(Letter(letter, ((40 * y) + k), int(x/13)*60 + 40))
        if y == 13:
            y = -1
        x += 1
        y += 1

while True:
    win.fill((10, 255, 10))
    pos = pygame.mouse.get_pos()
    word.draw()
    render(text, 300, 560, 35)
    for num in error_list:
        if num == '1':
            win.blit(hangman1, (200, 320))
        if num == '2':
            win.blit(hangman2, (175, 415))
        if num == '3':
            win.blit(hangman3, (140, 385))
        if num == '4':
            win.blit(hangman4, (140, 385))
        if num == '5':
            win.blit(hangman5, (140, 385))
        if num == '6':
            win.blit(hangman6, (140, 385))
        if num == '7':
            win.blit(hangman7, (140, 385))
            lost = True
    
    for letters in letters_list:
        letters.draw()
        if letters.text_rect.collidepoint(pos):
            pygame.draw.rect(win, (0, 0, 0), letters.text_rect, 3)
        if clicked is True and letter_clicked is False:
            if letters.text_rect.collidepoint(clicked_pos):
                letter_clicked = True
                clicked_letter = letters.letter
                clicked = False
    for x in range(0, len(word.word)):
        if clicked_letter == word.word[x]:
            word.found_list[x] = 'found'
            text = 'Great!'
            timer = True
        for letter in letters_list:
            if clicked_letter == letter.letter:
                letters_list.remove(letter)
                letter_clicked = False
            if clicked_letter not in word_list and letter_clicked is True and clicked_letter != '':
                error += 1
                error_list.append(str(error))
                letter_clicked = False
                text = 'Wrong guess:('
            
    if 'not found' not in word.found_list:
        won = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            clicked_pos = pygame.mouse.get_pos()
            clicked = True
    pygame.display.update()

