#Global Variables

Row1 = ['-','-','-']
Row2 = ['-','-','-']
Row3 = ['-','-','-']
Board = [Row3,Row2,Row1]
Coloum = []

Xwin = ['X','X','X']
Ywin = ['X','X','X']

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
    turnnum = turnnum+1
    if intinput >3:
       Row2[intinput-4] = 'X'  
    else:
      Row1[intinput-1] = 'X'
  else:
    turnnum=turnnum+1
    Row3[intinput - 7] = 'X'

#Checks game for win state
def winstate():
  coloum = 0
  global win
  for row in Board:
    if row == Xwin:
      win = True
      print('X wins!')
    elif row == Ywin:
      win = True
      print('Y wins!')
  while coloum<3:
    Coloum.append(Row1[coloum])
    Coloum.append(Row2[coloum])
    Coloum.append(Row3[coloum])
    if Coloum == Xwin:
      win = True
      print('X wins!')
    elif Coloum == Ywin:
      win = True
      print('Y wins!')
    Coloum.clear()
    coloum = coloum + 1
#Plays game while not in win state
def boardplaystate():
  global turnnum
  global win
  while win == False:
    playerturn()
    printboard()
    winstate()

printboard()
boardplaystate()