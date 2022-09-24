import random

class CDominoes:
    def __init__(self):
        self.dominoes = [
            [0,0],
            [1,0], [1,1],
            [2,0], [2,1], [2,2],
            [3,0], [3,1], [3,2], [3,3],
            [4,0], [4,1], [4,2], [4,3], [4,4],
            [5,0], [5,1], [5,2], [5,3], [5,4], [5,5],
            [6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [6,6]
        ]

class CRandom:
    def __init__(self, dominoes):
        self.picked = []
        count = 0
        while count < 10:
            choice = random.choice(dominoes)
            self.picked.append(choice)
            dominoes.remove(choice)
            count = count + 1

class CPlayer:
    def __init__(self, id, pieces):
        self.id = id
        self.pieces = pieces

class CTable:
    def __init__(self, player, snake):
        count = 1
        print('Player: ', player.id)
        print('Snake: ', snake)
        for piece in player.pieces:
            print(count, ': ', piece)
            count = count + 1

pieces = CDominoes()

firstPick = CRandom(pieces.dominoes)
secondPick = CRandom(pieces.dominoes)

player1 = CPlayer('1', firstPick.picked)
player2 = CPlayer('2', secondPick.picked)

startingPiece = random.choice(pieces.dominoes)
pieces.dominoes.remove(startingPiece)
snake = [startingPiece]
head = startingPiece[0]
tail = startingPiece[1]

activePlayer = random.choice([player1, player2])

print('Player ', activePlayer.id, ' goes first')

isWinner = False

while not isWinner:
    canPlay = False
    nextPlayer = False

    while not canPlay:
        for piece in activePlayer.pieces:
            if piece[0] == head or piece[0] == tail or piece[1] == head or piece[1] == tail:
                canPlay = True

        if not canPlay:
            if len(pieces.dominoes) == 0:
                CTable(activePlayer, snake)
                print('You cannot play a piece and there are no more pieces to draw.')
                nextPlayer = True
                canPlay = True

            else:
                CTable(activePlayer, snake)
                print('You cannot play a piece and need to draw.  Please choose a piece to draw: ')
                count = 1

                for piece in pieces.dominoes:
                    print(count, ': [ , ]')
                    count = count + 1

                validPlay = False
                play = ''

                while not validPlay:
                    play = input('Which piece would you like to draw?')
                    if int(play) > 0 and int(play) < (len(pieces.dominoes) + 1):
                        validPlay = True
                    else:
                        print('Please make a valid choice.')

                chosenPiece = pieces.dominoes[int(play)-1]
                print('Chosen Piece: ', chosenPiece)
                activePlayer.pieces.append(chosenPiece)
                pieces.dominoes.remove(chosenPiece)

    if canPlay and not nextPlayer:
        validChoice = False

        while not validChoice:
            CTable(activePlayer, snake)
            validPlay = False
            play = ''

            while not validPlay:
                play = input('Which piece would you like to play?')
                if int(play) > 0 and int(play) < (len(activePlayer.pieces) + 1):
                    validPlay = True
                else:
                    print('Please make a valid choice.')

            chosenPiece = activePlayer.pieces[int(play)-1]
            print('Chosen Piece: ', chosenPiece)

            if (chosenPiece[0] == tail and chosenPiece[0] == head) or (chosenPiece[1] == tail and chosenPiece[1] == head) or (chosenPiece[0] == head and chosenPiece[1] == tail) or (chosenPiece[1] == head and chosenPiece[0] == tail):
                validEnd = False
                while not validEnd:
                    print('This piece can be played on either the head or the tail of the snake.')
                    print('1. Head')
                    print('2. Tail')
                    end = input('Where would you like to play this piece?')
                    if int(end) == 1 or int(end) == 2:
                        validEnd = True
                    else:
                        print('Please make a valid choice.')
                if int(end) == 1:
                    if chosenPiece[0] == head:
                        snake.insert(0, [chosenPiece[1], chosenPiece[0]])
                        head = chosenPiece[1]
                        validChoice = True
                        activePlayer.pieces.remove(chosenPiece)
                    else:
                        snake.insert(0, [chosenPiece[0], chosenPiece[1]])
                        head = chosenPiece[0]
                        validChoice = True
                        activePlayer.pieces.remove(chosenPiece)
                else:
                    if chosenPiece[0] == tail:
                        snake.append([chosenPiece[0], chosenPiece[1]])
                        tail = chosenPiece[1]
                        validChoice = True
                        activePlayer.pieces.remove(chosenPiece)
                    else:
                        snake.append([chosenPiece[1], chosenPiece[0]])
                        tail = chosenPiece[0]
                        validChoice = True
                        activePlayer.pieces.remove(chosenPiece)

            elif chosenPiece[0] == head:
                snake.insert(0, [chosenPiece[1], chosenPiece[0]])
                head = chosenPiece[1]
                validChoice = True
                activePlayer.pieces.remove(chosenPiece)

            elif chosenPiece[1] == head:
                snake.insert(0, [chosenPiece[0], chosenPiece[1]])
                head = chosenPiece[0]
                validChoice = True
                activePlayer.pieces.remove(chosenPiece)

            elif chosenPiece[0] == tail:
                snake.append([chosenPiece[0], chosenPiece[1]])
                tail = chosenPiece[1]
                validChoice = True
                activePlayer.pieces.remove(chosenPiece)

            elif chosenPiece[1] == tail:
                snake.append([chosenPiece[1], chosenPiece[0]])
                tail = chosenPiece[0]
                validChoice = True
                activePlayer.pieces.remove(chosenPiece)

            else:
                print('Invalid piece.  Please make another choice.')

    if len(activePlayer.pieces) == 0:
        print('Congratulations player ', activePlayer.id, '.  You win!')
        if activePlayer.id == '1':
            print('Player 2 has these remaining pieces: ')
            count = 1
            for piece in player2.pieces:
                print(count, ': ', piece)
                count = count + 1
        else:
            print('Player 1 has these remaining pieces: ')
            count = 1
            for piece in player1.pieces:
                print(count, ': ', piece)
                count = count + 1
        print('Final Snake: ', snake)
        isWinner = True
    else:
        if int(activePlayer.id) == 1:
            activePlayer = player2
        else:
            activePlayer = player1

    print('-------------------------------------------------------------------------------------------')