import random

print('HI IM BRUH, LETS PLAY HANGMAN')
print(' ')
lstOfMovies = ['MOTHER INDIA', 'DHOOM', 'AZHARRUDDIN', 'MS DHONI THE UNTOLD STORY', 'CHETAK', 'CHENNAI VS CHINA',
               'MARY KOM', 'NO ENTRY', 'SINGH IS KINNG', 'PATIALA HOUSE',
               'BATLA HOUSE', 'JAB WE MET']


def DisplayMoviePuzzle(x):
    y = random.randint(0, (len(x) - 1))
    b = x[y]
    b = list(b)
    c = b
    c = list(c)
    vowels = ['A', 'E', 'I', 'O', 'U']

    for n in range(0, (len(b))):

        if b[n] in vowels:
            b[n] = b[n]
        elif b[n] == ' ':
            b[n] = '  /  '
            c[n] = '  /  '
        else:
            b[n] = '*'

    print(*b)
    i = 1

    while i:
        print('')
        guess = input('ENTER YOUR GUESS:')
        guess = guess.upper()
        appreciations = ['NICE ONE!', 'GREAT!']
        for m in range(0, len(b)):
            if guess == c[m]:
                b[m] = c[m]
            elif guess in vowels or guess in b[m]:
                print('THE LETTER YOU ENTERED IS ALREADY THERE OR NOT THERE IN THE MOVIE NAME:(')
                break

            else:
                continue
            h = random.randint(0, 1)
            if guess == c[m]:
                print(*appreciations[h])
                break
        print(*b)
        i += 1

        if b == c:
            print('CONGRATS! YOU CRACKED THE MOVIE NAME IN JUST ' + str(i - 1) + ' MOVES!')

            break


DisplayMoviePuzzle(lstOfMovies)
