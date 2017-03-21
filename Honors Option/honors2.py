"""
    Honors Option 2
    Gets information about games from user
    Plays one round of mancala
        Prints out results from each move to a file
    Plays the user specified amount of rounds of mancala
        Prints out statistics of all games to a file
"""
import random
import statistics

def make_gameboard(pits,seeds):
    gameboard = []
    for i in range(pits):
        gameboard.append(seeds)
    gameboard.append(0)
    for i in range(pits):
        gameboard.append(seeds)
    gameboard.append(0)
    return gameboard

def int_to_letter(integer):
    if integer == 0:
        return 'A'
    elif integer == 1:
        return 'B'
    elif integer == 2:
        return 'C'
    elif integer == 3:
        return 'D'
    elif integer == 4:
        return 'E'
    elif integer == 5:
        return 'F'
    elif integer == 6:
        return 'G'
    elif integer == 7:
        return 'H'
    elif integer == 8:
        return 'I'
    elif integer == 9:
        return 'J'
    elif integer == 10:
        return 'K'
    elif integer == 11:
        return 'L'
    elif integer == 12:
        return 'M'

def print_board(board):

    fp = open('single_play.txt', 'a')
    letters = []
    for i in range(int(len(board)/2) - 1):
        letters.append(int_to_letter(i + (len(board)/2)))
    length_side_of_board = len(letters)

    #Prints the current board
    print("STRATEGY'S PITS".center(7 + 5*(length_side_of_board + 1)+2),file=fp)

    #prints the place
    print("{:7}".format(""), end = "", file = fp)
    for i in range(length_side_of_board):
        print("{:5}".format(letters.pop().center(5)), end = '',file = fp)

    #prints the seperators
    print("\n{:>7}".format("|"),end = '',  file = fp)
    for i in range(length_side_of_board):
        print("{:5}".format("----|"), end = '',file = fp)

    #prints the top of the board
    print("\n{:5}".format(""),end = '', file = fp)
    for i in range(1, length_side_of_board + 1):
        print("{:5}".format(board[len(board) - i - 1]), end = '',file = fp)

    #prints the middle of the board
    print("\n{:5}".format(board[-1]),' '*5*length_side_of_board,"{:2}".\
    format(board[int(len(board)/2 - 1)]), file = fp)

    #prints the bottom of the board
    print("{:5}".format(""),end = '', file = fp)
    for i in range(0, length_side_of_board):
        print("{:5}".format(board[i]), end = '',file = fp)

    #prints the seperators
    print("\n{:>7}".format("|"),end = '',  file = fp)
    for i in range(length_side_of_board):
        print("{:5}".format("----|"), end = '',file = fp)

    #prints the place
    print("\n{:7}".format(""), end = "", file = fp)
    for i in range(int(len(board)/2) - 1):
        print("{:5}".format(int_to_letter(i).center(5)), end = '',file = fp)
    print('',file = fp)
    print("AMAZING'S PITS".center(7 + 5*(length_side_of_board + 1)+2),file= fp)
    print('', file = fp)
    fp.close()

def print_move(board, movestats = [0,0,0,0], turn = '', previous_scores = [],\
    play_again = False, amazing_strategy = '', capture = False):
    """
    Prints results of the play to a file
    board: A list containing the values of each slot
    movestats: A list with the first item as the number moved and the second
                where it was moved from
    extramoves: A list containing strings describing an additional moves played
    turn: A string representing the current player
    previous_scores: A list with the first item as Random's previous score,
                    and the second item as Strategy's previous score
    """
    fp = open('single_play.txt', 'a')

    #Prints whose turn it was
    if not turn == '':
        print(turn.upper()+"'S TURN\n", file = fp)
    fp.close()
    print_board(board)
    fp = open('single_play.txt', 'a')

    print("Amazing's Score:", board[int(len(board)/2 - 1)], file = fp)
    print("Strategy's Score:",board[-1], file = fp)

    #Prints the first move
    if movestats  != [0,0,0,0] and movestats != []:
        print("Moved {} from {}".format(movestats[1],int_to_letter\
        (movestats[0])), file = fp)

    #Prints how the scores changed as a result of the moves
    if not previous_scores == []:
        print("Amazing's score increased by {}".format\
        (board[int(len(board)/2 - 1)] -\
        previous_scores[0]), file = fp)
        print("Strategy's score increased by {}".format(board[-1] -\
        previous_scores[1]), file = fp)
    if play_again == True:
        print(turn[0].upper() + turn[1:], "gets to play again", file = fp)
    if capture == True:
        print(turn[0].upper() + turn[1:], "captured", movestats[3],\
        "tiles from",int_to_letter(movestats[2])+'!',file = fp)
    if amazing_strategy != '':
        print(amazing_strategy, file = fp)
    print("\n" + "-"*20 + "\n", file = fp)
    fp.close()

def move_tiles(move, board):
    """
    Changes values in the board based on which spot was choosen
    move: the spot from which to move the seeds
    board: a list containing the current values of the board
    returns: the current board as a list, the moves played in this turn as
             a list
    """
    move_again = False
    capture = False
    #set the number of seeds to move
    number_of_tiles = board[move]
    #A counter to count the current position on the board
    i = 1
    #Sets the spot chosen to 0
    board[move] = 0
    #Keeps track of what the original spot was
    original_move = move

    while number_of_tiles > 0:
        board[move + i] += 1
        i += 1
        number_of_tiles -= 1

        #Checks to see if it is random's turn and there is another move
        if number_of_tiles == 0 and original_move < int(len(board)/2 -1)\
        and (move + i - 1) == int(len(board)/2 - 1):
            move_again = True
        #Checks to see if it is strategy's turn and there is another move
        elif number_of_tiles == 0 and original_move > int(len(board)/2 -1)\
        and (move + i - 1) == len(board) - 1:
            move_again = True

        #Checks to see if tiles need to be moved from the opposite
        #side of the board and moves them
        elif number_of_tiles == 0 and board[move + i - 1] == 1:
            if (original_move > int(len(board)/2 -1) and (move + i - 1) >\
            int(len(board)/2 -1)) or\
            (original_move < int(len(board)/2 -1) and (move + i - 1) < \
            int(len(board)/2 -1)):
                to_move = board[len(board) - 1 -(move + i)]
                board[move + i - 1] += to_move
                board[len(board) - 1 -(move + i)] = 0
                capture = True

        #Keeps the counter within values in the list
        if move + i > (len(board) - 1):
            move = 0
            i = 0

    #Returns the current board and any extra moves played
    return board, move_again, capture

def strategy_turn(board):
    """
    Makes a decision on the next piece for strategy to move based on
    the given strategy
    board: a list containing the current values of the board
    returns: the place of the piece to move
    4,5,6 out of 7
    """

    for place in range(int(len(board)/2),len(board) - 1):
        if board[place] == ((len(board) - 1) - place):
            return place
    for place in range(len(board) - 1):
        if board[len(board) - 2 -place] == 0:
            continue
        else:
            return (len(board) - 2-place)

def amazing_turn(board):
    """
    Makes a decision on the next piece for strategy to move based on
    an amazing strategy
    board: a list containing the current values of the board
    returns: the place of the piece to move
    """

    amazing_strategy = ''

    #Chooses strategy for getting another move
    for place in range(int(len(board)/2) - 1):
        if board[place] == ((len(board)/2 - 1) - place):
            amazing_strategy = "Chosen because it gains another move"
            return place, amazing_strategy

    #Chooses because it captures seeds from the other side
    for place in range(int(len(board)/2) - 1):
        if board[place] + place < int(len(board)/2) - 1:
            if board[place] == 0:
                continue
            if board[board[place] + place] == 0:
                amazing_strategy = "Chosen because it captures seeds"
                return place, amazing_strategy

    #Chooses strategy to hurt other player
    for place in range(int(len(board)/2) - 1): #0,1,2
        if board[place] == 0:
            continue
        if (place + board[place]) > int(len(board)/2):
            if board[(place + board[place])%(len(board) - 1)] == len(board)\
            - 1 - (place + board[place])%(len(board)-1):
                amazing_strategy = "Chosen because it hurts strategy's play"
                return place, amazing_strategy

    #Chooses strategy to help clear pits for stealing
    for place in range(int(len(board)/2) - 1):
        if board[int(len(board)/2) - 2 - place] == 0:
            continue
        else:
            amazing_strategy = "Chosen because it is closest to the pit"
            return (int(len(board)/2) - 2 - place), amazing_strategy

def end_of_game(board):
    """
    Moves pieces at the end of the game, then calls a function to print
    the board
    """
    bottom_total = 0
    for i in range(int(len(board)/2)):
        bottom_total += board[i]
    board[int(len(board)/2 - 1)] = bottom_total
    top_total = 0
    for i in range(int(len(board)/2 + 1), len(board)):
        top_total += board[i]
    board[-1] = top_total
    for place in range(len(board)):
        if place == len(board) - 1 or place == int(len(board)/2 - 1):
            pass
        else:
            board[place] = 0
    print_move(board)
    fp = open('single_play.txt', 'a')
    if board[int(len(board)/2 - 1)] > board[-1]:
        print("Amazing Won!", file = fp)
    elif board[int(len(board)/2 - 1)] < board[-1]:
        print("Strategy Won!", file = fp)
    else:
        print("It's a tie!", file = fp)
    fp.close()

def detect_end_of_game(board):
    #Detects end of game
    bottom_total = 0
    for i in range(int(len(board)/2 - 1)):
        bottom_total += board[i]
    top_total = 0
    for i in range(int(len(board)/2), len(board) - 1):
        top_total += board[i]
    if bottom_total == 0 or top_total == 0:
        return True
    return False

def single_play(gameboard):
    """
    Plays the first game, printing results to a file
    Plays one round outside of loop so that random's seed can be based on
    the user input, then loops until end of game is reached
    rand_move: the user created seed for random
    """

    #Sets the first player
    turn = 'amazing'

    #Sets move_stats to an empty list, prints the gameboard
    move_stats = []
    print_move(gameboard, [])

    #Loops until end of game is reached
    while True:
        move_stats = []
        extra_moves = True

        if (detect_end_of_game(board)):
            break

        #Plays amazing's turn
        if turn == 'amazing':
            while extra_moves == True:
                previous_score = [gameboard[int(len(gameboard)/2 - 1)],\
                gameboard[-1]]
                tile_move, amazing_strategy = amazing_turn(gameboard)
                move_stats.append(tile_move)
                move_stats.append(gameboard[tile_move])
                move_stats.append(len(gameboard) - 2 -(tile_move + gameboard[tile_move]))
                move_stats.append(gameboard[len(gameboard) - 2 -(tile_move + gameboard[tile_move])])
                gameboard, extra_moves, capture = \
                move_tiles(tile_move, gameboard)
                print_move(gameboard, move_stats, turn ,previous_score,\
                extra_moves, amazing_strategy, capture)
                move_stats = []
                if (detect_end_of_game(board)):
                    break
            turn = 'strategy'

        #Plays strategy's turn
        elif turn == 'strategy':
            while extra_moves == True:
                previous_score = [gameboard[int(len(gameboard)/2 - 1)],\
                gameboard[-1]]
                tile_move = strategy_turn(gameboard)
                move_stats.append(tile_move)
                move_stats.append(gameboard[tile_move])
                move_stats.append(len(gameboard) - 2 -(tile_move + gameboard[tile_move]))
                move_stats.append(gameboard[len(gameboard) - 2 -(tile_move + gameboard[tile_move])])
                gameboard, extra_moves, capture =\
                move_tiles(tile_move, gameboard)
                print_move(gameboard, move_stats, turn ,previous_score,\
                extra_moves,capture = capture)
                move_stats = []
                if (detect_end_of_game(board)):
                    break
            turn = 'amazing'
    end_of_game(gameboard)

def multiple_play(games, pits, seeds):
    """
    Plays the number of games specified by the user
    games: the user specified number of games to play
    """

    #Sets statistics
    strategy_won = 0
    amazing_won = 0
    game_stats_strategy = []
    game_stats_amazing = []

    #Plays the number of games specified
    for game_number in range(1, games+1):
        #Resets gameboard each game, randomly generates who starts
        gameboard = make_gameboard(pits, seeds)
        turn_num = random.randint(0,1)
        if turn_num == 0:
            turn = 'strategy'
        else:
            turn = 'amazing'

        while True:
            extra_moves = True

            #Detects end of game
            if(detect_end_of_game(gameboard)):
                break

            #plays amazing's turn
            if turn == 'amazing':
                while extra_moves == True:
                    tile_move, amazing_strategy = amazing_turn(gameboard)
                    gameboard, extra_moves, capture =\
                    move_tiles(tile_move, gameboard)
                    if(detect_end_of_game(gameboard)):
                        break
                turn = 'strategy'

            #plays the strategy's turn
            elif turn == 'strategy':
                while extra_moves == True:
                    tile_move = strategy_turn(gameboard)
                    gameboard, extra_moves, capture =\
                    move_tiles(tile_move, gameboard)
                    if(detect_end_of_game(gameboard)):
                        break
                turn = 'amazing'

        if gameboard[int(len(gameboard)/2 - 1)] > gameboard[-1]:
            amazing_won += 1
        else:
            strategy_won += 1
        game_stats_strategy.append(gameboard[-1])
        game_stats_amazing.append(gameboard[int(len(board)/2 - 1)])

    #After all games have been played, prints information to a file
    game_stats_amazing.sort()
    game_stats_strategy.sort()
    fp = open('multiple_play.txt', 'w')

    print("Total number of games:"  + str(amazing_won+strategy_won), file = fp)
    print("Amazing won " + str(amazing_won) + " games", file = fp)
    print("Strategy won " + str(strategy_won) + " games", file = fp)

    print("Amazing's average score: ", sum(game_stats_amazing)/\
    len(game_stats_amazing), file = fp)
    print("Strategy's average score: ", sum(game_stats_strategy)/\
    len(game_stats_strategy), file = fp)

    print("Amazing's median score: ", statistics.median(game_stats_amazing),\
    file = fp)
    print("Strategy's median score: ", statistics.median(game_stats_strategy),\
    file = fp)

    print("Amazing's highest score: ", max(game_stats_amazing), file = fp)
    print("Strategy's highest score: ", max(game_stats_strategy), file = fp)

    print("Amazing's lowest score: ", min(game_stats_amazing), file = fp)
    print("Strategy's lowest score: ", min(game_stats_strategy), file = fp)


open('single_play.txt', 'w').close()

#Gets information from user
random_seed = int(input("Input random seed: "))
number_of_pits = int(input("Input number of pits (2-6): "))
number_of_seeds = int(input("Input number of seeds (1-6): "))
games_to_play = int(input("Input number of games for multi-play: "))

random.seed(random_seed)
#Plays single play
board = make_gameboard(number_of_pits, number_of_seeds)
single_play(board)

#Plays multiple play
if not games_to_play == 0:
    multiple_play(games_to_play, number_of_pits, number_of_seeds)
