#Global Variables

Row1 = ['-','-','-']
Row2 = ['-','-','-']
Row3 = ['-','-','-']
Board = [Row1,Row2,Row3]

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
  


#Plays game while not in win state
def boardplaystate():
  global turnnum
  while turnnum<8:
    printboard()
    playerturn()
    
boardplaystate()