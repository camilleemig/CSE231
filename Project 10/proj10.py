###########################################################
    #  Computer Project #10
    #
    #  Algorithm
    #   Set up game
    #   Loop getting commands until game is won or quit
    #       seperate commands
    #       check to see if the command is valid
    #   print win screen, or quit
    ###########################################################
import cards       # this is required

YAY_BANNER = """
__   __             __        ___                       _ _ _
\ \ / /_ _ _   _    \ \      / (_)_ __  _ __   ___ _ __| | | |
 \ V / _` | | | |    \ \ /\ / /| | '_ \| '_ \ / _ \ '__| | | |
  | | (_| | |_| |_    \ V  V / | | | | | | | |  __/ |  |_|_|_|
  |_|\__,_|\__, ( )    \_/\_/  |_|_| |_|_| |_|\___|_|  (_|_|_)
           |___/|/

"""

RULES = """
    *------------------------------------------------------*
    *-------------* Thumb and Pouch Solitaire *------------*
    *------------------------------------------------------*
    Foundation: Columns are numbered 1, 2, ..., 4; built
                up by rank and by suit from Ace to King.
                You can't move any card from foundation,
                you can just put in.

    Tableau:    Columns are numbered 1, 2, 3, ..., 7; built
                down by rank only, but cards can't be laid on
                one another if they are from the same suit.
                You can move one or more faced-up cards from
                one tableau to another. An empty spot can be
                filled with any card(s) from any tableau or
                the top card from the waste.

     To win, all cards must be in the Foundation.
"""

MENU = """
Game commands:
    TF x y     Move card from Tableau column x to Foundation y.
    TT x y n   Move pile of length n >= 1 from Tableau column x
                to Tableau column y.
    WF x       Move the top card from the waste to Foundation x
    WT x       Move the top card from the waste to Tableau column x
    SW         Draw one card from Stock to Waste
    R          Restart the game with a re-shuffle.
    H          Display this menu of choices
    Q          Quit the game
"""
def setup_game():
    """
        The game setup function, it has 4 foundation piles, 7 tableau piles,
        1 stock and 1 waste pile. All of them are currently empty. This
        function populates the tableau and the stock pile from a standard
        card deck.

        7 Tableau: There will be one card in the first pile, two cards in the
        second, three in the third, and so on. The top card in each pile is
        dealt face up, all others are face down. Total 28 cards.

        Stock: All the cards left on the deck (52 - 28 = 24 cards) will go
        into the stock pile.

        Waste: Initially, the top card from the stock will be moved into the
        waste for play. Therefore, the waste will have 1 card and the stock
        will be left with 23 cards at the initial set-up.

        This function will return a tuple: (foundation, tableau, stock, waste)
    """
    # you must use this deck for the entire game.
    # the stock works best as a 'deck' so initialize it as a 'deck'
    stock = cards.Deck()
    stock.shuffle()
    # the game piles are here, you must use these.
    foundation = [[], [], [], []]           # list of 4 lists
    tableau = [[], [], [], [], [], [], []]  # list of 7 lists
    waste = []                              # one list
    for i in range(0,7):
        for n in range(i,7):
            if i == n:
                current_card = stock.deal()
                current_card.__face_up = True
                tableau[n].append(current_card)
            else:
                current_card = stock.deal()
                current_card.flip_card()
                tableau[n].append(current_card)
    waste.append(stock.deal())
    return foundation, tableau, stock, waste

def display_game(foundation, tableau, stock, waste):
    """
        Displays the formatted game with three sections
        foundation: a list of four lists of cards, only displays top card
        tableau: a list of seven lists of cards, displays every card
        stock: a list of cards that have not yet been flipped over, only
                displays the number of cards
        waste: a list of cards that have been flipped, displays all cards
        returns: None
    """
    #Prints Foundations
    print("="*19 , "FOUNDATIONS", "="*19)
    for i in range(1, 5):
        print('f'+ str(i), end = "   ")
    print()
    for i in range(len(foundation)):
        if foundation[i] == []:
            print("[  ]", end = " ")
        else:
            print("["+foundation[i][-1].__str__()+"]", end = " ")
    print()

    #Prints Tableau Header
    print("="*19 , "TABLEAU", "="*19)
    max_len = 0
    for i in range(1, 8):
        print(("t"+ str(i)).center(3), end = "  ")
    print()

    #Finds the maximum length of the tableau lists
    for i in range(len(tableau)):
        if len(tableau[i]) > max_len:
            max_len = len(tableau[i])

    #Prints the cards (or blank spaces if there is no card in that spot)
    for i in range(max_len): #Loop for the index into the lists
        for n in range(len(tableau)): #Loop for the list number
            try:
                print(tableau[n][i].__str__().center(3), end = "  ")
            except:
                print("   ", end = "  ")
        print()
    print()

    #Prints stock and waste section
    print("="*19 , "STOCK/WASTE", "="*19)
    print("Stock #(", stock.__len__() ,") -->", waste)

def valid_fnd_move(src_card, dest_card):
    """
        Checks to see if the move to the foundation is valid (ace if the list
            is empty, otherwise if the suit is the same and the rank is one
            higher than the last card on the list)
        src_card: card to move
        dest_card: card to place src_card on
        returns: True or raises RuntimeError
    """
    #Checks to see if the suits are the same and that src_card's rank is one
    #higher than dest_card's rank
    if (dest_card.suit() == src_card.suit()) and\
    (src_card.rank() == dest_card.rank() + 1):
        return True
    else:
        #Raises RuntimeError if the move is not valid
        raise RuntimeError("Error: invalid move due to mismatched cards")

def valid_tab_move(src_card, dest_card):
    """
        Checks to see if the move to the foundation is valid
            the card to move must be face up, the suits must be different, and
            the rank of the card to place onto must be one less than the\
            rank of the card to move
        src_card: card to move
        dest_card: card to place src_card on
        returns: True or raises RuntimeError
    """
    #Checks to see if card is face up, returns RuntimeError if it is not
    if src_card.is_face_up():
        #if dest_card is nothing, then any card can be placed
        if dest_card == []:
            return True
        #otherwise, if the suits are not the same and the rank of src_card
        #is one lower than the rank of dest_card, raises RuntimeError if false
        if (not (dest_card.suit() == src_card.suit())) and\
        (src_card.rank() == dest_card.rank() - 1):
            return True
        else:
            raise RuntimeError("Error: invalid move due to mismatched cards")
    else:
        raise RuntimeError("Error: insufficient number of cards to move")

def tableau_to_foundation(tab, fnd):
    """
        Moves a card from the tableau to the foundation, then flips the
            top card on the tableau list, if necessary
        tab: list of the cards from which to move the top card
        fnd: list of cards to place the card onto
        returns: None
    """
    #If the tableau is empty and the card is an ace, place it
    if (fnd == []) and (tab[-1].rank() == 1):
        fnd.append(tab.pop())
        if not tab[-1].is_face_up():
            tab[-1].flip_card()
    #Otherwise, if the foundation is empty but it is not an ace, raise an error
    elif fnd == []:
        raise RuntimeError("Error: invalid move due to mismatched cards")
    #Otherwise, if the tableau list is not empty, check if it is a valid move
    elif not tab == []:
        if (valid_fnd_move(tab[-1],fnd[-1])) == True:
            #If it is valid, then place the card and flip the next one
            fnd.append(tab.pop())
            if not (tab == []):
                if not tab[-1].is_face_up():
                    tab[-1].flip_card()
    else:
        #Raises error if it can not complete the move
        raise RuntimeError("Error: insufficient number of cards to move")

def tableau_to_tableau(tab1, tab2, n):
    """
        Moves a card from the tableau to the tableau, then flips the
            top card on the tableau list, if necessary
        tab1: list of the cards from which to move n amount of cards
        tab2: list of cards to place the cards onto
        n: the number of cards to move
        returns: None
    """
    #List to place cards into for moving them
    transfer_list = []

    #If it is only moving one card
    if n == 1:
        #If the list to move to is empty, move the card and flip the next card
        if (tab2 == []):
            tab2.append(tab1.pop(-1))
            if not tab1 == [] and not tab1[-1].is_face_up():
                tab1[-1].flip_card()
        #If they are both not empty, see if it is a valid move, then
        #move the card if it is
        elif not tab1 == []:
            if (valid_tab_move(tab1[-1],tab2[-1])):
                tab2.append(tab1.pop(-1))
                if not tab1 == [] and not tab1[-1].is_face_up():
                    tab1[-1].flip_card()

    #If it is moving more than one card
    else:
        #If the list to move to is empty and there are enough cards to move in
        #the list to move from
        if tab2 == [] and len(tab1) >= n:
            #Check if it is a valid move, if it is, move the cards to a
            #placeholder list and then to the list to move to to preserve
            #the order of the cards
            if (valid_tab_move(tab1[-n],[])):
                for i in range(n):
                    if tab1[-1].is_face_up:
                        transfer_list.append(tab1.pop())
                    else:
                        break
                if len(transfer_list) == n:
                    for i in range(n):
                        tab2.append(transfer_list.pop())
                    if not tab1[-1].is_face_up():
                        tab1[-1].flip_card()
        #If the list to move to is not empty and there are enough cards
        elif len(tab1) >= n:
            #If it is a valid move, then try to move the cards
            if (valid_tab_move(tab1[-n],tab2[-1])):
                for i in range(n):
                    if tab1[-1].is_face_up():
                        transfer_list.append(tab1.pop())
                    else:
                        raise RuntimeError\
                        ("Error: insufficient number of cards to move")
                #If the proper amount of cards was appended to the transfer_list
                #then move all of the cards to tab2 and flip the last card in
                #tab1
                if len(transfer_list) == n:
                    for i in range(n):
                        tab2.append(transfer_list.pop())
                    if not tab1 == []:
                        if not tab1[-1].is_face_up():
                            tab1[-1].flip_card()
        #If there aren't enough cards to move, then raise a RuntimeError
        else:
            raise RuntimeError("Error: insufficient number of cards to move")

def waste_to_foundation(waste, fnd, stock):
    """
        Moves a card from the waste to the foundation
        waste: list of the cards from which to move one card
        fnd: list of cards to place the cards onto
        stock: not necessary or used, leftover from previous version
        returns: None
    """
    #If the foundation is empty and the card is an ace, move it
    if (fnd == []) and (waste[-1].rank() == 1):
        fnd.append(waste.pop())
    #If the foundation is not empty and the waste is not empty, check if it is
    #a valid move and move the card if it is
    elif (not fnd == []) and (not waste == []):
        if (valid_fnd_move(waste[-1],fnd[-1])):
            fnd.append(waste.pop())
    #Raise proper errors
    elif waste == []:
        raise RuntimeError("Error: insufficient number of cards to move")
    else:
        raise RuntimeError("Error: invalid move due to mismatched cards")

def waste_to_tableau(waste, tab, stock):
    """
        Moves a card from the waste to the tableau
        waste: list of the cards from which to move one card
        tab: list of cards to place the cards onto
        stock: not necessary or used, leftover from previous version
        returns: None
    """
    #If the tableau is empty, any card can be moved to it, so move the card
    if tab == []:
        tab.append(waste.pop(-1))
    #If it is a valid move, then move the card
    elif(valid_tab_move(waste[-1], tab[-1])):
        tab.append(waste.pop(-1))

def stock_to_waste(stock, waste):
    """
        Moves a card from the stock to the waste, or raises RuntimeError
        stock: list of the cards from which to move one card
        waste: list of cards to place the cards onto
        returns: None
    """
    #If the stock isn't empty, move a card, if it is, raise an error
    if not stock.is_empty():
        waste.append(stock.deal())
    else:
        raise RuntimeError("Error: insufficient number of cards to move")

def is_winner(foundation):
    """
        Checks to see if there are 13 cards in each foundation list and
            that the top card is a King
        foundation: list of four lists of cards
        returns: True or False
    """
    #If the length of each list is 13 and the top card on each list is a King
    if len(foundation[0]) == 13 and len(foundation[1]) == 13\
    and len(foundation[2]) == 13 and len(foundation[3]) == 13:
        if foundation[0][12].rank() == 13 and foundation[1][12].rank() == 13\
        and foundation[2][12].rank() == 13 and foundation[3][12].rank() == 13:
            return True
    else:
        return False

#Sets up the game
print(RULES)
fnd, tab, stock, waste = setup_game()
display_game(fnd, tab, stock, waste)
print(MENU)
command = input("prompt :> ")

#Loops until the quit command is given
while command.strip().lower() != 'q':
    try:
        commands = command.lower().split()
        #If there are no commands
        if commands == []:
            raise RuntimeError("Error: no command entered")
        #If command is tableau to foundation
        if commands[0] == "tf":
            if len(commands) == 3:
                x = int(commands[1].strip()) - 1
                y = int(commands[2].strip()) - 1
                if x < 0 or x > 6 or y < 0 or y > 3:
                    raise RuntimeError("Error: arguments must be numbers in range")
                tableau_to_foundation(tab[x], fnd[y])
            else:
                raise RuntimeError("Error: wrong number of arguments")
        #If command is tableau to tableau
        elif commands[0] == "tt":
            if len(commands) == 4:
                x = int(commands[1].strip()) - 1
                y = int(commands[2].strip()) - 1
                n = int(commands[3].strip())
                if x < 0 or x > 6 or y < 0 or y > 6 or n < 1:
                    raise RuntimeError("Error: arguments must be numbers in range")
                tableau_to_tableau(tab[x], tab[y], n)
            else:
                raise RuntimeError("Error: wrong number of arguments")
        #If command is waste to foundation
        elif commands[0] == "wf":
            if len(commands) == 2:
                x = int(commands[1].strip()) - 1
                if x < 0 or x > 3:
                    raise RuntimeError("Error: arguments must be numbers in range")
                waste_to_foundation(waste, fnd[x], stock)
            else:
                raise RuntimeError("Error: wrong number of arguments")
        #If command is waste to tableau
        elif commands[0] == "wt":
            if len(commands) == 2:
                x = int(commands[1].strip()) - 1
                if x < 0 or x > 6:
                    raise RuntimeError("Error: arguments must be numbers in range")
                waste_to_tableau(waste,tab[x],stock)
            else:
                raise RuntimeError("Error: wrong number of arguments")
        #If command is stock to waste
        elif commands[0] == "sw":
            if len(commands) == 1:
                stock_to_waste(stock, waste)
            else:
                raise RuntimeError("Error: wrong number of arguments")
        #If command is reset
        elif commands[0] == "r":
            if len(commands) == 1:
                fnd, tab, stock, waste = setup_game()
            else:
                raise RuntimeError("Error: wrong number of arguments")
        #If command is help
        elif commands[0] == "h":
            if len(commands) == 1:
                print(MENU)
            else:
                raise RuntimeError("Error: wrong number of arguments")
        #If it was not a recognized command
        else:
            raise RuntimeError(command + " is not a valid command")
        display_game(fnd, tab, stock, waste)
    #Handle all errors for the program
    except RuntimeError as error_message:  # any RuntimeError you raise lands here
        print("{:s}\nTry again.".format(str(error_message)))
    #Break if player won the game
    if(is_winner(fnd)):
        break
    #Set up for next move
    print()
    command = input("prompt :> ")

if (is_winner(fnd)):
    print(YAY_BANNER)

# Questions

# Q1: 7

# Q2: 4

# Q3: 1

# Q4: 7
