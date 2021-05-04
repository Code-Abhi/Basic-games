def check_win():
    #horizontally
    if board[0]==ch and board[1]==ch and board[2]==ch:
        print("TIC TAC TOE PLAYER 1 HAS WON")
        exit()
    elif  board[0]==cy and board[1]==cy and board[2]==cy:
        print("TIC TAC TOE PLAYER 2 HAS WON")
        exit()
    elif  board[3]==ch and board[4]==ch and board[5]==ch:
        print("TIC TAC TOE PLAYER 1 HAS WON")
        exit()    
    elif  board[3]==cy and board[4]==cy and board[5]==cy:
        print("TIC TAC TOE PLAYER 2 HAS WON")
        exit()
    elif  board[6]==ch and board[7]==ch and board[8]==ch:
        print("TIC TAC TOE PLAYER 1 HAS WON")
        exit()
    elif  board[6]==cy and board[7]==cy and board[8]==cy:
        print("TIC TAC TOE PLAYER 2 HAS WON")
        exit() 
    #vertically
    elif  board[0]==ch and board[3]==ch and board[6]==ch:
        print("TIC TAC TOE PLAYER 1 HAS WON")
        exit()
    elif  board[0]==cy and board[3]==cy and board[6]==cy:
        print("TIC TAC TOE PLAYER 2 HAS WON")
        exit()    
    elif  board[1]==ch and board[4]==ch and board[7]==ch:
        print("TIC TAC TOE PLAYER 1 HAS WON")
        exit()
    elif  board[1]==cy and board[4]==cy and board[7]==cy:
        print("TIC TAC TOE PLAYER 2 HAS WON")
        exit()        
    elif  board[3]==ch and board[5]==ch and board[8]==ch:
        print("TIC TAC TOE PLAYER 1 HAS WON")
        exit() 
    elif  board[2]==cy and board[5]==cy and board[8]==cy:
        print("TIC TAC TOE PLAYER 2 HAS WON")
        exit()      
    #diagonally
    elif  board[0]==ch and board[4]==ch and board[8]==ch:
        print("TIC TAC TOE PLAYER 1 HAS WON")
        exit() 
    elif  board[0]==cy and board[4]==cy and board[8]==cy:
        print("TIC TAC TOE PLAYER 2 HAS WON")
        exit()       
    elif  board[2]==ch and board[4]==ch and board[6]==ch:
        print("TIC TAC TOE PLAYER 1 HAS WON")
        exit()    
    elif  board[2]==cy and board[4]==cy and board[6]==cy:
        print("TIC TAC TOE PLAYER 2 HAS WON") 
        exit()
    
#BOARD_________________________________________________________________________________________

board=[" "," "," ",
       " "," "," ",
       " "," "," " ]

def display_board():
    print(" | "+board[0]+" | "+board[1]+" | "+board[2]+" | ")
    print(" | "+board[3]+" | "+board[4]+" | "+board[5]+" | ")
    print(" | "+board[6]+" | "+board[7]+" | "+board[8]+" | ")        


                 
#GAME_________________________________________________________________________________________________

def playervsplayer():
    i=1
    while i<6:

        k=0
        while k==0:      
            position=int(input("player 1 enter your position from 1-9:  "))
            position=position-1
            if position<=8:
                if board[position]==ch or board[position]==cy:
                        print("space already occupied  ")
                        
                else:
                        k=1
                        board[position]=ch
                        check_win()
                        display_board()
            else: 
                print("INVALID CHARACTER") 
        if i==5:
            print("draw")
            exit()                   
        k=0
        while k==0:
            position2=int(input("player 2 enter your position from 1-9:  "))
            position2=position2-1
            if position2<=8:
                if board[position2]==ch or board[position2]==cy:
                        print("space already occupied  ")
                        k=0
                else:
                        k=1    
                        board[position2]=cy
                        check_win()
                        display_board()
            else:
                print("INVALID POSITION")
        i=i+1          


#player vs comp_____________________________________________________________________________________
import random
def playervscomp():
    i=1
    while i<6:

        k=0
        while k==0:      
            position=int(input("player 1 enter your position from 1-9:  "))
            position=position-1
            if position<=8:
                if board[position]==ch or board[position]==cy:
                        print("space already occupied  ")
                        
                else:
                        k=1
                        board[position]=ch
                        check_win()
                        display_board()
            else: 
                print("INVALID CHARACTER")
        if i==5:
            print("draw")
            exit()        
        k=0
        while k==0:
            position2= random.choice([0,1,2,3,4,5,6,7,8,])
            if board[position2]==ch or board[position2]==cy:
                        print("space already occupied  ")
                        
            else:
                    k=1
                    board[position2]=cy
                    check_win()
                    print(" ")
                    display_board()

#USER INPUT________________________________________________________________________________________
v=input("do you want to play 'single player'  or 'multiplayer'?     ").lower()
q=0
while q==0:
    ch=input("player1 choose your symbol, 'x' or 'o':  ").upper()
    if ch=="X":
        cy= "O"
        q=1
    elif ch=="O":
        cy="X"
        q=1
    else:
        print("invalid charecter") 
if v== "single player":
    playervscomp()
elif v== "multiplayer":
    playervsplayer()
else:
    print("INVALID choice, you may not play.")
    exit()
       