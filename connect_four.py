import numpy as np
import random

#Plays one full game of connect-4 between two players and returns the win,loss or draw in list form

def play_once(player1,player2):
    
#Initialize connect-4 board as matrix
    board = np.array(list("*******"*6)).reshape(6,7)
   
    counter = 1
    while board_empty(board): 
       
        if counter%2 == 0:
            selected_player = player1
            player = "1"
        else:
            selected_player = player2
            player = "2"
        
        #Choice of movement relative to player's binary "genes"       
        choice = choice_maker(selected_player)
        
        while not is_valid(board,choice):
            choice = choice_maker(selected_player)
        
        board,level = update_board(board,choice,player)
        
        if is_win(board,[level,choice],player):
            if player == "1":
                return [1,0]
            if player == "2":
                return [0,1]      
        
        counter += 1 
    return [0,0]  
    
#Maps binary candidates to probabilities of playing choice and returns integer representing column to be played
def choice_maker(player):
    
    low_list = []
    high_list = []
    
    for i in range(7):
        if player[i] == str(1):
            high_list = high_list+[i]
        else:
            low_list = low_list+[i]
            
    r = random.randrange(1,101)
    
    if len(high_list) == 0:
        r = 24
    if len(low_list) == 0:
        r = 26
        
    if r>=25:
        pos = random.randrange(len(high_list))
        return high_list[pos]
    else:
        pos = random.randrange(len(low_list))
        return low_list[pos]
    
#Checks if board is completely full by scanning top row
def board_empty(current_board):
    for i in range(7):
        if current_board[0][i] == "*":
            return True
    return False
        
#Checks if given move is valid             
def is_valid(current_board,choice):
    if current_board[0][choice] == "*":
        return True
    return False

#Returns a board updated with the latest move and the level at which the update was made
def update_board(current_board,choice,player):
    levels = [5,4,3,2,1,0]
    for l in levels:
        if current_board[l][choice] == "*":
            current_board[l][choice] = player
            return current_board,l 

#Returns True if winning position.  
def is_win(current_board,current_move,current_player):
    
    #horizontal
    counter = 0
    for column in current_board[current_move[0]]:
        if column == current_player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True
    
    #vertical
    counter = 0
    for level in range(6):
        if current_board[level][current_move[1]] == current_player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True
    
    #diagonal to the right - down
    counter = 0
    diff = min(current_move[0],current_move[1])
    y,x = current_move[0]-diff,current_move[1]-diff
    while y<6 and x<7:
        if current_board[y][x] == current_player:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            return True
        y += 1
        x += 1
        
    #diagonal to the left - up
    counter = 0
    y,x = current_move[0],current_move[1]
    while y>0 and x<6:
        y = y-1
        x = x+1
    while y<=5 and x>=0:
        if current_board[y][x] == current_player:
            counter = counter+1
        else:
            counter = 0
        if counter == 4:
            return True
        y = y+1
        x = x-1
        
    return False
    

"""    
#Manual board controls to check features 
#     r  c
board[0][0] = "*"
board[1][0] = "*"
board[2][0] = "*"
board[3][0] = "*"
board[4][0] = "*"
board[5][0] = "*"

board[0][1] = "*"
board[1][1] = "*"
board[2][1] = "*"
board[3][1] = "*"
board[4][1] = "*"
board[5][1] = "*"

board[0][2] = "*"
board[1][2] = "*"
board[2][2] = "*"
board[3][2] = "*"
board[4][2] = "*"
board[5][2] = "*"

board[0][3] = "*"
board[1][3] = "*"
board[2][3] = "*"
board[3][3] = "*"
board[4][3] = "*"
board[5][3] = "*"

board[0][4] = "*"
board[1][4] = "*"
board[2][4] = "*"
board[3][4] = "*"
board[4][4] = "*"
board[5][4] = "*"

board[0][5] = "*"
board[1][5] = "*"
board[2][5] = "*"
board[3][5] = "*"
board[4][5] = "*"
board[5][5] = "*"

board[0][6] = "*"
board[1][6] = "*"
board[2][6] = "*"
board[3][6] = "*"
board[4][6] = "*"
board[5][6] = "*"

"""