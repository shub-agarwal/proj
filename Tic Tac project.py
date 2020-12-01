def welcome(board):
    list1=range(1,10)
    print('"Hello User!" Welcome to tic tac toe \n')
    print('{0:^4} | {1:^4} | {2:^4}'.format(board[0],board[1],board[2]))
    print('{0:^4} | {1:^4} | {2:^4}'.format(board[3],board[4],board[5]))
    print('{0:^4} | {1:^4} | {2:^4} \n'.format(board[6],board[7],board[8]))
    
    while True:
        user=input('Enter y to continue: ')
        
        if user == 'y':
            print("welcome to the game users,\n")
            print('Please select a number from your screen, you will be given a chance each \n')
            print('{0:^4} | {1:^4} | {2:^4}'.format(list1[0],list1[1],list1[2]))
            print('{0:^4} | {1:^4} | {2:^4}'.format(list1[3],list1[4],list1[5]))
            print('{0:^4} | {1:^4} | {2:^4}'.format(list1[6],list1[7],list1[8]))
            break
        
        else:
            print('enter the value y')
   
def display(board):
    print('\n' *25)
    
    print(' Tic Tac Toe \n')
    print('{0:^4} | {1:^4} | {2:^4}'.format(board[1],board[2],board[3]))
    print('{0:^4} | {1:^4} | {2:^4}'.format(board[4],board[5],board[6]))
    print('{0:^4} | {1:^4} | {2:^4}'.format(board[7],board[8],board[9]))

def marker_usr():
    
    while True:
        marker=input('Player1, select you marker "X" or "O": ').upper()
        
        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')
        
def space_check(board,position):
    
    if board[position] == '':
        return True
    else:
        return False
    
def user_input():
    
    choice=''
    acc_values=range(0,10)
    out_of_range=True
    while choice.isdigit() == False or out_of_range == True or not space_check(board,int(choice)):
         
        choice=input('Enter your position(1-9): ')
        
        if choice.isdigit() == False:
            print('Please enter numeric values (1-9) !!')
            
        if choice.isdigit() == True:
            if int(choice) in acc_values:
                out_of_range=False
            else:
                print('please enter values in range (1-9) ')
                  
                
    return int(choice)

def place_maker(board,position,player):
    board[position]=player
def win(board,marked):
    
    return ((board[1] == marked and board[2] == marked and board[3] == marked) or
            (board[4]== marked and board[5]== marked and board[6]== marked) or
            (board[7]== marked and board[8]== marked and board[9]== marked) or
            (board[1]== marked and board[4]== marked and board[7]== marked) or
            (board[2]== marked and board[5]== marked and board[8]== marked) or
            (board[3]== marked and board[6]== marked and board[9] == marked) or
            (board[1] == marked and board[5] == marked and board[9] == marked) or
            (board[3] == marked and board[5] == marked and board[7] == marked))   

from random import randint

def choose_first():
    if randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'

def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
board = ['']*10
welcome(board)
(player1,player2)=marker_usr()
turn=choose_first()
print(turn+'will go first')

while True:
    ##player1
    if turn == 'player1':
        position=user_input()
        place_maker(board,position,player1)
        display(board)
        
        if win(board,player1) == True:
            print("player1,You won !!")
            break
        else:
            if full_board(board):
                print('The game is draw')
                break
            else:
                turn='player2'
        
    ##player2
    else:
            position=user_input()
            place_maker(board,position,player2)
            display(board)
            
            if win(board,player2) == True:
                print("player2,You won !!")
                break
                
            else:
                if full_board(board):
                    print('The game is draw')
                    break
                else:
                    turn='player1'
            
