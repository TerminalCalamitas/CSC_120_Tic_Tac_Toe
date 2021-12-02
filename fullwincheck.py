#Global Variables

Row1 = ['-','-','-']
Row2 = ['-','-','-']
Row3 = ['-','-','-']
Board = [Row3,Row2,Row1]
Coloum = []
DiagonalL = []
DiagonalR = []

Xwin = ['X','X','X']
Owin = ['O','O','O']

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
  if intinput>9:
    print('Please choose a valid number.')
  elif intinput<1:
    print('Please choose a valid number.')
  elif intinput < 7:
    if intinput >3:
       if Row2[intinput-4] == 'X':
         print('Please choose an open space')
       else:Row2[intinput-4] = 'X' 
       turnnum=turnnum+1 
    else:
      if Row1[intinput-1] == 'X':
         print('Please choose an open space')
      else:
        Row1[intinput-1] = 'X'
        turnnum=turnnum+1
  else:
    if Row3[intinput-7] == 'X':
      print('Please choose an open space')
    else:
      Row3[intinput-7] = 'X'
      turnnum=turnnum+1

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
    while turnnum < 8:
      playerturn()
      printboard()
      winstate()

printboard()
boardplaystate()