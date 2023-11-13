import random
import sys

WIDTH = 8
HEIGTH = 8
def draw_board(board):
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGTH):
        print('%s|'% (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s'% (y+1))
    print(' +--------+')
    print('  12345678')

def get_new_board():
    #crea un board vacío
    board = []
    for i in range(WIDTH):
        board.append([' ']*HEIGTH)
    return board

def is_valid_move(board, tile, xstart, ystart):
    #Devuelve False si la move con las coordenadas x, y es invalida
    #si es válida devuelve una lista de los espacios que el jugador obtendría por la move
    if board[xstart][ystart] != ' ' or not is_on_board(xstart, ystart):
        return False

    if tile == 'X':
        other_tile = 'O'
    else:
        other_tile = 'X'

    tiles_to_flip = []

    for xdirection, ydirection in [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]:
        x, y = xstart, ystart
        x += xdirection #primer paso en la dirección
        y += ydirection #primer paso en la dirección

        while is_on_board(x, y) and board[x][y] == other_tile:
            x += xdirection
            y += ydirection
            if is_on_board(x, y) and board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tiles_to_flip.append([x, y])
    
    if len(tiles_to_flip) == 0:
        return False
    return tiles_to_flip

def is_on_board(x, y):
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGTH - 1

def get_board_with_valid_moves(board, tile):
    #devuelve un board con las moves posibles para el jugador
    board_copy = get_board_copy(board)

    for x, y in get_valid_moves(board_copy, tile):
        board_copy[x][y] = '.'
    return board_copy

def get_valid_moves(board, tile):
    valid_moves = []

    for x in range(WIDTH):
        for y in range(HEIGTH):
            if is_valid_move(board, tile, x, y) != False:
                valid_moves.append([x, y])
    return valid_moves

def get_score_of_board(board):
    #determina el score del juego en un diccionario con claves 'x' y 'y'
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGTH):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}

def enter_player_tile():
    #permite al jugador que tipo de tile será
    #devuelve una lista en donde el primer elemento es el jugador
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()
    
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    
def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def make_move(board, tile, xstart, ystart):
    #coloca la ficha en la tile elegida y convierte las fichas opuestas
    #Devuelve False si la move es invalida, True si es válida
    tiles_to_flip = is_valid_move(board, tile, xstart, ystart)
    
    if tiles_to_flip == False:
        return False
    
    board[xstart][ystart] = tile
    for x, y in tiles_to_flip:
        board[x][y] = tile
    return True

def get_board_copy(board):
    board_copy = get_new_board()

    for x in range(WIDTH):
        for y in range(HEIGTH):
                board_copy[x][y] = board[x][y]
    
    return board_copy

def is_on_corner(x, y):
    #devuelve True si la posición es una de las esquinas
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGTH - 1)

def get_player_move(board, player_tile):
    #devuelve [x, y] o 'hints' o 'quit'
    NUM1a8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, "quit" to end the game, or "hints" to toggle hints.')
        move = input().lower()
        if move == 'quit' or move == 'hints':
            return move
        
        if len(move) == 2 and move[0] in NUM1a8 and move[1] in NUM1a8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if is_valid_move(board, player_tile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Enter the column (1-8) and then the row (1-8).')
            print('For example, 81 will move on the top-right corner.')
    
    return [x, y]

def get_corner_best_move(board, computer_tile):
    #donde va a jugar la computadora y devolver la move como una lista [x, y]
    possible_moves = get_valid_moves(board, computer_tile)

    #ordena aleatoriamente el orden de las moves posibles
    random.shuffle(possible_moves)

    #siempre jugar en la esquina si es posible
    for x, y in possible_moves:
        if is_on_corner(x, y):
            return [x, y]
        
    #recorrer la lista de moves posibles y guardar la que da mayor score
    best_score = -1
    for x, y in possible_moves:
        board_copy = get_board_copy(board)
        make_move(board_copy, computer_tile, x, y)
        score = get_score_of_board(board_copy)[computer_tile]
        if score > best_score:
            best_move = [x, y]
            best_score = score
    return best_move

def get_worst_move(board, tile):
    possible_moves = get_valid_moves(board, tile)
    random.shuffle(possible_moves)

    worst_score = 64
    for x, y in possible_moves:
        board_copy = get_board_copy(board)
        make_move(board_copy, tile, x, y)
        score = get_score_of_board(board_copy)[tile]
        if score < worst_score:
            worst_move = [x, y]
            worst_score = score
    return worst_move

def get_random_move(board, tile):
    possible_moves = get_valid_moves(board, tile)
    return random.choice(possible_moves)

def is_on_side(x, y):
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGTH - 1

def get_corner_side_best_move(board, tile):
    possible_moves = get_valid_moves(board, tile)
    random.shuffle(possible_moves)

    #siempre jugar en la esquina si es posible
    for x, y in possible_moves:
        if is_on_corner(x, y):
            return [x, y]
    for x, y in possible_moves:
        if is_on_side(x, y):
            return [x, y]
    return get_corner_best_move(board, tile)

def print_score(board, player_tile, computer_tile):
    #imprime el score actual
    scores = get_score_of_board(board)
    print('You: %s points. Computer: %s points.' %(scores[player_tile], scores[computer_tile]))

def play_game(player_tile, computer_tile):
    show_hints = False
    turn = who_goes_first()
    # print('The ' + turn + ' will go first.')
    
    #clear the board
    board = get_new_board()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        player_valid_moves = get_valid_moves(board, player_tile)
        computer_valid_moves = get_valid_moves(board, computer_tile)

        if player_valid_moves == [] and computer_valid_moves == []:
            return board
        elif turn == 'player':
            if player_valid_moves != []:
                # if show_hints:
                #     valid_moves_board = get_board_with_valid_moves(board, player_tile)
                #     draw_board(valid_moves_board)
                # else:
                #     draw_board(board)
                # print_score(board, player_tile, computer_tile)

                move = get_corner_best_move(board, player_tile)
                # if move == 'quit':
                #     print('Thanks for playing!')
                #     sys.exit()
                # elif move == 'hints':
                #     show_hints = not show_hints
                #     continue
                # else:
                make_move(board, player_tile, move[0], move[1])
            turn = 'computer'
        elif turn == 'computer':
            if computer_valid_moves != []:
                # draw_board(board)
                # print_score(board, player_tile, computer_tile)

                # input('Press Enter to see the computer\'s move.')
                move = get_corner_side_best_move(board, computer_tile)
                make_move(board, computer_tile, move[0], move[1])
            turn = 'player'

#start game
NUM_GAMES = 250
x_wins = o_wins = ties = 0
print('Welcome to REVERSEGAM !')
player_tile, computer_tile = ['X', 'O']#enter_player_tile()

for i in range(NUM_GAMES):
    final_board = play_game(player_tile, computer_tile)

    # draw_board(final_board)
    scores = get_score_of_board(final_board)
    print('#%s: X scored %s points. O scored %s points.' % (i + 1, scores['X'], scores['O']))

    if scores[player_tile] > scores[computer_tile]:
        x_wins += 1
        # print('You beat the computer by %s points! Congratulations!' %(scores[player_tile] - scores[computer_tile]))
    elif scores[player_tile] < scores[computer_tile]:
        o_wins += 1
        # print('You lost. The computer beat you by %s points.' % (scores[computer_tile] - scores[player_tile]))
    else:
        ties += 1
        # print('The game was a tie!')
    
    # print('Do yo want to play again? (yes or no)')
    # if not input().lower().startswith('y'):
    #     break
print('X wins: %s (%s%%)' % (x_wins, round(x_wins / NUM_GAMES * 100, 1)))   
print('O wins: %s (%s%%)' % (o_wins, round(o_wins / NUM_GAMES * 100, 1)))   
print('Ties:   %s (%s%%)' % (ties, round(ties / NUM_GAMES * 100, 1)))   
        

