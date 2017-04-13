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

def end_of_game_multiple(board):
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

    #Chooses strategy to help the next move
    for place in range(int(len(board)/2) - 1): #0,1,2
        if board[place] == 0:
            continue
        for next_place in range(place + 1, int(len(board)/2) - 1):
            if (board[next_place] == 0) and (board[place] == (next_place\
            - place)):
                amazing_strategy = "Chosen because it helps next move"
                return place, amazing_strategy

    #Chooses strategy to help clear pits for stealing
    for place in range(int(len(board)/2) - 1):
        if board[int(len(board)/2) - 2 - place] == 0:
            continue
        else:
            amazing_strategy = "Chosen because it is closest to the pit"
            return (int(len(board)/2) - 2 - place), amazing_strategy

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

def multiple_play(games, pits, seeds):
    """
    Plays the number of games specified by the user
    games: the user specified number of games to play
    """

    #Sets statistics
    strategy_won = 0
    amazing_won = 0
    tie = 0
    strategy_started = 0
    amazing_started = 0
    game_stats_strategy = []
    game_stats_amazing = []

    #Plays the number of games specified
    for game_number in range(1, games+1):
        #Resets gameboard each game, randomly generates who starts
        gameboard = make_gameboard(pits, seeds)
        turn_num = random.choice([0,1])
        if turn_num == 0:
            turn = 'strategy'
            strategy_started += 1
        else:
            turn = 'amazing'
            amazing_started += 1

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

        end_of_game_multiple(gameboard)
        if gameboard[int(len(gameboard)/2 - 1)] > gameboard[-1]:
            amazing_won += 1
        elif gameboard[int(len(gameboard)/2 - 1)] < gameboard[-1]:
            strategy_won += 1
        else:
            tie += 1

        game_stats_strategy.append(gameboard[-1])
        game_stats_amazing.append(gameboard[int(len(gameboard)/2 - 1)])

    #After all games have been played, prints information to a file
    game_stats_amazing.sort()
    game_stats_strategy.sort()
    fp = open('multiple_play.txt', 'a')
    print("Seeds: " + str(seeds) + " Pits: " + str(pits), file = fp)
    print("Amazing won " + str(amazing_won) + " games", file = fp)
    print("Strategy won " + str(strategy_won) + " games", file = fp)
    print("Tie on " + str(tie) + " games", file = fp)
    print("Amazing started: ", amazing_started, file = fp)
    print("Strategy started: ", strategy_started, file = fp)
    print("\n", file = fp)
    return amazing_won, strategy_won, tie

random.seed(50)
total_strategy_won = 0
total_amazing_won = 0
tie = 0
for number_of_pits in range(2,7):
    for number_of_seeds in range(1,7):
        amazing_won_game, strategy_won_game, tie_won = multiple_play(1000, number_of_pits, number_of_seeds)
        total_amazing_won += amazing_won_game
        total_strategy_won += strategy_won_game
        tie += tie_won

print(total_amazing_won, total_strategy_won, tie)
