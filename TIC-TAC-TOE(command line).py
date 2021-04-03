import random

print('hello mate!')
print('LETS PLAY TIC-TAC-TOE')
input()
print('')
x1a = 1
x2a = 2
x3a = 3
x4a = 4
x5a = 5
x6a = 6
x7a = 7
x8a = 8
x9a = 9
playerSign = ''
botSign = ''

x1 = ' '
x2 = ' '
x3 = ' '
x4 = ' '
x5 = ' '
x6 = ' '
x7 = ' '
x8 = ' '
x9 = ' '
print('Given below are the numberings for each box')
print(' ' + str(x1a) + ' | ' + str(x2a) + ' | ' + str(x3a))
print('---|---|---')
print(' ' + str(x4a) + ' | ' + str(x5a) + ' | ' + str(x6a))
print('---|---|---')
print(' ' + str(x7a) + ' | ' + str(x8a) + ' | ' + str(x9a))
playersMove = None
PlayerMove = None
botMove = None

k = random.randint(1, 9)
lstOfBoxes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
vals = int


def PlayerBotSigns():
    global playerSign, botSign, playersMove
    j = 1

    while j:

        playerSign = input('which letter do you want to use?(\'X\' or \'O\') ')
        playerSign = playerSign.upper()
        if playerSign == 'O':
            print('OK I WILL GO FIRST')
            botSign = 'X'
            playersMove = False

            break
        elif playerSign == 'X':
            print('OK U GO FIRST')
            botSign = 'O'
            playersMove = True

            break

        else:
            print('U CAN ONLY CHOOSE LETTERS \'X\' OR \'O\'')
            print('')

    j += 1


def GameBoard():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9

    print(' ' + str(x1) + ' | ' + str(x2) + ' | ' + str(x3))
    print('---|---|---')
    print(' ' + str(x4) + ' | ' + str(x5) + ' | ' + str(x6))
    print('---|---|---')
    print(' ' + str(x7) + ' | ' + str(x8) + ' | ' + str(x9))


def displayBotMove():
    global botSign, playerSign, x1, x2, x3, x4, x5, x6, x7, x8, x9, k, vals

    i = 1
    while i:
        k = random.randint(1, 9)
        if k == 1:
            vals = x1
        if k == 2:
            vals = x2
        if k == 3:
            vals = x3
        if k == 4:
            vals = x4
        if k == 5:
            vals = x5
        if k == 6:
            vals = x6
        if k == 7:
            vals = x7
        if k == 8:
            vals = x8
        if k == 9:
            vals = x9
        if vals == playerSign:
            k = random.randint(1, 9)
        elif vals != playerSign:
            if k in lstOfBoxes:
                if k == 1 and x1 != playerSign:
                    x1 = botSign
                    lstOfBoxes.remove(k)
                    break
                elif k == 2 and x2 != playerSign:
                    x2 = botSign
                    lstOfBoxes.remove(k)
                    break
                elif k == 3 and x3 != playerSign:
                    x3 = botSign
                    lstOfBoxes.remove(k)
                    break
                elif k == 4 and x4 != playerSign:
                    x4 = botSign
                    lstOfBoxes.remove(k)
                    break
                elif k == 5 and x5 != playerSign:
                    x5 = botSign
                    lstOfBoxes.remove(k)
                    break
                elif k == 6 and x6 != playerSign:
                    x6 = botSign
                    lstOfBoxes.remove(k)
                    break
                elif k == 7 and x7 != playerSign:
                    x7 = botSign
                    lstOfBoxes.remove(k)
                    break
                elif k == 8 and x8 != playerSign:
                    x8 = botSign
                    lstOfBoxes.remove(k)
                    break
                elif k == 9 and x9 != playerSign:
                    x9 = botSign
                    lstOfBoxes.remove(k)
                    break
        else:
            k = random.randint(1, 9)
    i += 1
    GameBoard()


def displayPlayerMove():
    global PlayerMove, playerSign, botSign, x1, x2, x3, x4, x5, x6, x7, x8, x9, k

    i = 1
    while i:

        PlayerMove = input('which box should your move be in? ')
        if PlayerMove == '1' or PlayerMove == '2' or PlayerMove == '3' or PlayerMove == '4' \
                or PlayerMove == '5' or PlayerMove == '6' or PlayerMove == '7' or PlayerMove == '8' \
                or PlayerMove == '9':
            break
        if PlayerMove != '1' or PlayerMove != '2' or PlayerMove != '3' or \
                PlayerMove != '4' or PlayerMove != '5' or PlayerMove != '6' or \
                PlayerMove != '7' or PlayerMove != '8' or PlayerMove != '9':
            print('Please Enter a Valid Box Number')
            print('')
            continue
        i += 1
    if PlayerMove == '1':
        x1 = playerSign
    if PlayerMove == '2':
        x2 = playerSign
    if PlayerMove == '3':
        x3 = playerSign
    if PlayerMove == '4':
        x4 = playerSign
    if PlayerMove == '5':
        x5 = playerSign
    if PlayerMove == '6':
        x6 = playerSign
    if PlayerMove == '7':
        x7 = playerSign
    if PlayerMove == '8':
        x8 = playerSign
    if PlayerMove == '9':
        x9 = playerSign


def AllOccupied():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, playerSign, botSign
    if x1 != ' ' and x2 != ' ' and x3 != ' ' and x4 != ' ' and x5 != ' ' and x6 != ' ' and x7 != ' ' and x8 != ' ' and \
            x9 != ' ':
        return True
    else:
        return False


def WhoWon():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, playerSign, botSign
    if x1 == x2 and x2 == x3 and x3 == x1 and x1!= ' ' and x2 != ' ' and x3 != ' ':
        if playerSign == x1:
            print('You win !!!')
        elif botSign == x1:
            print('I win!!!!!')
        return True
    elif x4 == x5 and x5 == x6 and x6 == x4 and x4!= ' ' and x5 != ' ' and x6 != ' ':
        if playerSign == x4:
            print('You win !!!')
        elif botSign == x4:
            print('I win!!!!!')
        return True
    elif x7 == x8 and x9 == x8 and x9 == x7 and x9!= ' ' and x8 != ' ' and x7 != ' ':
        if playerSign == x7:
            print('You win !!!')
        elif botSign == x7:
            print('I win!!!!!')
        return True
    elif x1 == x4 and x4 == x7 and x7 == x1 and x1!= ' ' and x4 != ' ' and x7 != ' ':
        if playerSign == x1:
            print('You win !!!')
        elif botSign == x1:
            print('I(Bot) win!!!!!')
        return True
    elif x2 == x5 and x5 == x8 and x8 == x2 and x2!= ' ' and x5 != ' ' and x8 != ' ':
        if playerSign == x2:
            print('You win !!!')
        elif botSign == x2:
            print('I win!!!!!')
        return True
    elif x3 == x6 and x6 == x9 and x9 == x3 and x3!= ' ' and x6 != ' ' and x9 != ' ':
        if playerSign == x3:
            print('You win !!!')
        elif botSign == x3:
            print('I win!!!!!')
        return True
    elif x1 == x5 and x5 == x9 and x9 == x1 and x1!= ' ' and x5 != ' ' and x9 != ' ':
        if playerSign == x1:
            print('You win !!!')
        elif botSign == x1:
            print('I win!!!!!')
        return True
    elif x3 == x5 and x5 == x7 and x7 == x3 and x3!= ' ' and x5 != ' ' and x7 != ' ':
        if playerSign == x3:
            print('You win !!!')
        elif botSign == x3:
            print('I win!!!!!')
        return True
    else:
      return False  


def insertLettersOnBoard():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, playerSign, botSign, playersMove, PlayerMove, lstOfBoxes, k
    AllOccupied()
    i = 1
    while i:
        random.shuffle(lstOfBoxes)
        if playersMove is True:
            displayPlayerMove()

            displayBotMove()

        elif playersMove is False:
            displayBotMove()

            displayPlayerMove()

        random.shuffle(lstOfBoxes)
        if WhoWon():
            break
    i += 1

if __name__ == '__main__':
    PlayerBotSigns()
    insertLettersOnBoard()
