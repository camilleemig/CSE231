"""
    Honors Option 1
    Gets information about games from user
    Plays one round of mancala
        Prints out results from each move to a file
    Plays the user specified amount of rounds of mancala
        Prints out statistics of all games to a file
"""

import random
import statistics

open('single_play.txt', 'w').close()

def print_move(board, movestats = [0,0], extramoves = [], turn = '',\
    previous_scores = []):
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
        
    #Prints the current board
    print("{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}".format("",board[12], board[11],\
    board[10], board[9], board[8], board[7], ""), file = fp)
    print("{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}".format(board[13],"", "", "", "",\
    "", "", board[6]), file = fp)
    print("{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}\n".format("",board[0], board[1],\
    board[2], board[3], board[4], board[5], ""), file = fp)
    print("Random's Score:", board[6], file = fp)
    print("Strategy's Score:",board[13], file = fp)
    
    #Prints the first move
    if not movestats  == []:
        print("Moved {} from {}".format(movestats[1],movestats[0]), file = fp)
        
    #Prints the next moves, if there are any
    for item in extramoves:
        print(item, file = fp)
        
    #Prints how the scores changed as a result of the moves
    if not previous_scores == []:
        print("Random's score increased by {}".format(board[6] - previous_scores[0]), file = fp)
        print("Strategy's score increased by {}".format(board[13] -previous_scores[1]), file = fp)
    
    print("\n" + "-"*20 + "\n", file = fp)
    fp.close()


def move_tiles(move, board, moves):
    """
    Changes values in the board based on which spot was choosen
    move: the spot from which to move the seeds
    board: a list containing the current values of the board
    moves: a list of any previous moves that occurred this turn
    returns: the current board as a list, the moves played in this turn as
             a list
    """
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
        if number_of_tiles == 0 and move < 6 and (move + i - 1) == 6:
            turn = random_turn(board)
            move_str = "Moved " + str(board[turn]) +" from " + str(turn)
            moves.append(move_str)
            move_tiles(turn, board, moves)
        #Checks to see if it is strategy's turn and there is another move
        elif number_of_tiles == 0 and move > 6 and (move + i - 1) == 13:
            turn = strategy_turn(board)
            move_str = "Moved " + str(board[turn]) +" from " + str(turn)
            moves.append(move_str)            
            move_tiles(turn, board, moves)
            
        #Checks to see if tiles need to be moved from the opposite
        #side of the board and moves them
        elif number_of_tiles == 0 and board[move + i - 1] == 1:
            if (original_move > 6 and (move + i - 1) > 6) or\
            (original_move < 6 and (move + i - 1) < 6): 
                to_move = board[13-(move + i)]      
                board[move + i - 1] += board[13-(move + i)]
                board[13-(move + i)] = 0
                if not to_move == 0:
                    move_str = "Moved " + str(to_move) +" from "\
                    + str(13- (move + i))
                    moves.append(move_str)
        #Keeps the counter within values in the list            
        if move + i > 13:
            move = 0
            i = 0
            
    #Returns the current board and any extra moves played
    return board, moves
    
def strategy_turn(board):
    """
    Makes a decision on the next piece for strategy to move based on 
    the given strategy
    board: a list containing the current values of the board
    returns: the place of the piece to move
    """
    #Checks to see if there is only one valid move
    if board[7] == 0 and board[8] == 0 and board[9] == 0 and board[10] == 0\
    and board[11] == 0:
        return 12       
    elif board[7] == 0 and board[8] == 0 and board[9] == 0 and board[10] == 0\
    and board[12] == 0:
        return 11         
    elif board[7] == 0 and board[8] == 0 and board[9] == 0 and board[11] == 0\
    and board[12] == 0:
        return 10        
    elif board[7] == 0 and board[8] == 0 and board[10] == 0 and board[11] == 0\
    and board[12] == 0:
        return 9       
    elif board[7] == 0 and board[9] == 0 and board[10] == 0 and board[11] == 0\
    and board[12] == 0:
        return 8       
    elif board[8] == 0 and board[9] == 0 and board[10] == 0 and board[11] == 0\
    and board[12] == 0:
        return 7  
    #Otherwise, uses strategy to determine the spot to move from
    else:
        for place in range(7,13):
            if board[place] == (13-place):
                return place
        for place in range(6):
            if board[12-place] == 0:
                continue
            else:
                return (12-place)
            
def random_turn(board):
    """
    Makes a decision on the next piece for strategy to move based on 
    a random number generator
    board: a list containing the current values of the board
    returns: the place of the piece to move
    """
    #Loops for error checking
    while True:
        #Checks to see if there is only one valid move
        if board[0] == 0 and board[1] == 0 and board[2] == 0 and\
        board[3] == 0 and board[4] == 0:
            move = 5       
        elif board[0] == 0 and board[1] == 0 and board[2] == 0 and\
        board[3] == 0 and board[5] == 0:
            move = 4        
        elif board[0] == 0 and board[1] == 0 and board[2] == 0 and\
        board[4] == 0 and board[5] == 0:
            move = 3        
        elif board[0] == 0 and board[1] == 0 and board[3] == 0 and\
        board[4] == 0 and board[5] == 0:
            move = 2        
        elif board[0] == 0 and board[2] == 0 and board[3] == 0 and\
        board[4] == 0 and board[5] == 0:
            move = 1      
        elif board[1] == 0 and board[2] == 0 and board[3] == 0 and\
        board[4] == 0 and board[5] == 0:
            move = 0 
        else:
            #Ensures that the move will be a non-zero spot on random's side
            move = 13
            while move == 13 or board[move] == 0:  
                move = random.randint(0,5)
        if move == None:
            continue
        else:
            break
    return move
    
def get_first_turn():
    """
    Gets the first seed for random from the user
    returns: the place of the piece to move
    """
    while True:
        try:
            tile_to_move = int(input("Please input the seed to move"\
            + " (0-5 from left to right): "))
        except ValueError:
            print("That was not a number. Try again.")
            continue
        if tile_to_move > 5 or tile_to_move < 0:
            print("Integer out of range (0-5), please try again.")
            continue
        else:
            break
    return tile_to_move
    
def end_of_game(board):
    """
    Moves pieces at the end of the game, then calls a function to print
    the board
    """
    board[6] = board[6] + board[5] + board[4] + board[3] + board[2] +\
    board[1] + board[0]
    board[13] = board[13] + board[12] + board[11] + board[10] + board[9]\
    + board[8] + board[7]
    for place in range(len(board)):
        if place == 13 or place == 6:
            pass
        else:
            board[place] = 0
    print_move(board, [])

def single_play(rand_move):
    """
    Plays the first game, printing results to a file
    Plays one round outside of loop so that random's seed can be based on
    the user input, then loops until end of game is reached
    rand_move: the user created seed for random
    """
    
    #Sets the gameboard for the first game and the first player
    gameboard = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    turn = 'strategy'
    
    #Sets move_stats to an empty list, prints the gameboard
    move_stats = []
    print_move(gameboard, [])
    
    #Plays strategy's first round
    previous_score = [gameboard[6], gameboard[13]]
    tile_move = strategy_turn(gameboard)   
    move_stats.append(tile_move)
    move_stats.append(gameboard[tile_move])     
    gameboard, extramoves = move_tiles(tile_move, gameboard, [])
    print_move(gameboard, move_stats, extramoves, turn,previous_score)
    turn = 'random'
    
    #Plays random's first round
    previous_score = [gameboard[6], gameboard[13]]
    move_stats = []
    move_stats.append(rand_move)
    move_stats.append(gameboard[rand_move])     
    gameboard, extramoves = move_tiles(rand_move, gameboard, [])
    print_move(gameboard, move_stats, extramoves, turn,previous_score)
    turn = 'strategy'
            
    #Loops until end of game is reached
    while True:
        move_stats = []
        #Detects end of game
        if (gameboard[0] == 0 and gameboard[1] == 0 and gameboard[2] == 0 and\
        gameboard[3] == 0 and gameboard[4] == 0 and gameboard[5] == 0) or\
        (gameboard[7] == 0 and gameboard[8] == 0 and gameboard[9] == 0 and\
        gameboard[10] == 0 and gameboard[11] == 0 and gameboard[12] == 0):
            end_of_game(gameboard)
            break
        
        #Stores score at beginning of round
        previous_score = [gameboard[6], gameboard[13]]
        
        #Plays random's turn
        if turn == 'random':
            tile_move = random_turn(gameboard)
            move_stats.append(tile_move)
            move_stats.append(gameboard[tile_move]) 
            gameboard, extra_moves = move_tiles(tile_move, gameboard, [])
            print_move(gameboard, move_stats, extra_moves, turn,previous_score)
            turn = 'strategy'
            
        #Plays strategy's turn
        elif turn == 'strategy':
            tile_move = strategy_turn(gameboard)
            move_stats.append(tile_move)
            move_stats.append(gameboard[tile_move])
            gameboard, extra_moves = move_tiles(tile_move, gameboard, [])
            print_move(gameboard, move_stats, extra_moves, turn,previous_score)
            turn = 'random'


def multiple_play(games):
    """
    Plays the number of games specified by the user
    games: the user specified number of games to play
    """
    
    #Sets statistics
    strategy_won = 0
    random_won = 0
    game_stats_strategy = []  
    game_stats_random = []
    
    #Plays the number of games specified
    for game_number in range(1, games+1):
        #Resets gameboard each game, randomly generates who starts
        gameboard = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        turn_num = random.randint(0,1)
        if turn_num == 0:    
            turn = 'strategy'
        else:
            turn = 'random'
        
        #Plays first round with random seeded as the game number%6
        if turn == 'strategy':
            tile_move = strategy_turn(gameboard)        
            gameboard, extramoves = move_tiles(tile_move, gameboard, [])
            turn = 'random'
        
            move_stats = []   
            gameboard, extramoves = move_tiles(game_number%6, gameboard, [])
            turn = 'computer'
            
        else:
            move_stats = []   
            gameboard, extramoves = move_tiles(game_number%6, gameboard, [])
            turn = 'computer'
            
            tile_move = strategy_turn(gameboard)        
            gameboard, extramoves = move_tiles(tile_move, gameboard, [])
            turn = 'random'
                
        while True:
            move_stats = []
            #Checks if it is the end of the game
            if (gameboard[0] == 0 and gameboard[1] == 0 and gameboard[2] == 0\
            and gameboard[3] == 0 and gameboard[4] == 0 and gameboard[5] == 0)\
            or (gameboard[7] == 0 and gameboard[8] == 0 and gameboard[9] == 0\
            and gameboard[10] == 0 and gameboard[11] == 0\
            and gameboard[12] == 0):
                if gameboard[6] > gameboard[13]:
                    random_won += 1
                else:
                    strategy_won += 1
                game_stats_strategy.append(gameboard[13])
                game_stats_random.append(gameboard[6])
                break
            #plays random's turn
            if turn == 'random':
                tile_move = random_turn(gameboard)
                move_stats.append(tile_move)
                move_stats.append(gameboard[tile_move]) 
                gameboard, extra_moves = move_tiles(tile_move, gameboard, [])
                turn = 'computer'
            #plays the computer's turn
            elif turn == 'computer':
                tile_move = strategy_turn(gameboard)
                move_stats.append(tile_move)
                move_stats.append(gameboard[tile_move])
                gameboard, extra_moves = move_tiles(tile_move, gameboard, [])
                turn = 'random'
    #After all games have been played, prints information to a file
    game_stats_random.sort()
    game_stats_strategy.sort()
    fp = open('multiple_play.txt', 'w')
    
    print("Total number of games:"  + str(random_won+strategy_won), file = fp)
    print("Random won " + str(random_won) + " games", file = fp)
    print("Strategy won " + str(strategy_won) + " games", file = fp)

    print("Random's average score: ", sum(game_stats_random)/\
    len(game_stats_random), file = fp)
    print("Strategy's average score: ", sum(game_stats_strategy)/\
    len(game_stats_strategy), file = fp)
    
    print("Randoms's median score: ", statistics.median(game_stats_random),\
    file = fp)
    print("Strategy's median score: ", statistics.median(game_stats_strategy),\
    file = fp)
    
    print("Random's highest score: ", max(game_stats_random), file = fp)
    print("Strategy's highest score: ", max(game_stats_strategy), file = fp)
    
    print("Random's lowest score: ", min(game_stats_random), file = fp)
    print("Strategy's lowest score: ", min(game_stats_strategy), file = fp)


#Gets information from user
random_seed = get_first_turn()
games_to_play = int(input("Input number of games for multi-play: "))
#Plays single play
single_play(random_seed)
#Plays multiple play
multiple_play(games_to_play)