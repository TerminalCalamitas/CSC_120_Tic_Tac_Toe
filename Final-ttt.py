#Global Variables

import random 

Row1 = ['-','-','-']
Row2 = ['-','-','-']
Row3 = ['-','-','-']
Board = [Row3,Row2,Row1]
Coloum = []
DiagonalL = []
DiagonalR = []

Xwin = ['X','X','X']
Owin = ['O','O','O']

occupied = False
win = False
turnnum = 0

#Prints current board state
def printboard():
  for rows in range(len(Board)):
        print(Board[rows])


#Promted player input for human turn
def playerturn():
  global turnnum
  plrinput = input('\"X\" input position (1-9): ')
  intinput = int(plrinput)
  #Sets input to board space
  Freespace(intinput)

#Checks for free space
def Freespace(index):
  rownum = 0
  if index > 6:
    rownum = 7
    row = Row3
  elif index < 4:
    rownum = 4
    row = Row2
  else:
    rownum = 1
    row = Row1

  if row[index-rownum] != '-':
    return True


#Checks game for win state
def winstate():
  coloum = 0
  global win
  global DiagonalL
  global DiagonalR
  #Checks for horizontal wins
  DiagonalR = [Row3[2],Row2[1], Row1[0]]
  DiagonalL = [Row3[0], Row2[1], Row1[2]]
  for row in Board:
    if row == Xwin:
      win = True
      print('X wins!')
    elif row == Owin:
      win = True
      print('O wins!')
  #Checks for vertical wins
  while coloum<3:
    Coloum.append(Row1[coloum])
    Coloum.append(Row2[coloum])
    Coloum.append(Row3[coloum])
    if Coloum == Xwin:
      win = True
      print('X wins!')
    elif Coloum == Owin:
      win = True
      print('O wins!')
    Coloum.clear()
    coloum = coloum + 1

  #Checks for diagonal wins

  if DiagonalL == Xwin:
    win = True
    print('X wins!')
  elif DiagonalR == Owin:
    win = True
    print('O wins!')
  elif DiagonalR == Xwin:
    win = True
    print('X wins!')
  elif DiagonalR == Owin:
    win = True
    print('O wins!')


#Plays game while not in win state
def boardplaystate():
  global turnnum
  global win
  while win == False:
    if turnnum < 8:
      playerturn()
      printboard()
      Ply2Turn(Board, letter)
      printboard()
      winstate()



# Jalen's Code =========================================================================

#def Freespace(board, move):
 # return Board[move] == '-'

#G
def AImove(board, letter, move):
  board[move] = letter

# Does a valid move from the lsit on the past board
#returns None if there are no valid moves
def RandomMove(board, mlist):
  pMoves = []
  for i in mlist:
    if row in mlist:
     if Freespace(board, row):
      pMoves.append(row)

#determines the AI's Letter either it being X or O based of player 1
# Determines where the computer can move on the board
def Ply2Turn(board, letter):
  letter == 'O'
  for row in range(0,9):
    copy = printboard()
    if FreeSpace(copy, row):
      AImove(copy, letter, row)
      if winstate(copy, letter):
        return row
   
  #Blocking Player 1 moves
  for row in range(0,9):
    copy = printboard(board)
    if FreeSpace(copy, row):
      AImove(copy, playerturn, row)
      if winstate(copy, playerturn):
        return row
      
  #AI player corner moves
  Cmove = RandomMove(board, [0, 2, 6, 8])
  if Cmove != None:
    return Cmove
      
  #AI player takes middle square if the position is free on the board
  if FreeSpace(board, 4):
    return 4
  
  #AI player side moves
  return RandomMove(board, [1, 3, 5, 7])






printboard()
boardplaystate()