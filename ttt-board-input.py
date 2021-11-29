
Row1 = ['-','-','-']
Row2 = ['-','-','-']
Row3 = ['-','-','-']
Board = [Row1,Row2,Row3]

def printboard():
  for rows in range(len(Board)):
        print(Board[rows])

def playerturn():
    plrinput = input('input position (1-9)')
    intinput = int(plrinput)
    if intinput<7:
      if intinput<4:
        Row1[intinput-1] = 'X'
      else:
        Row2[intinput-4] = 'X'
    else:
      Row3[intinput - 7] = 'X'
    

playerturn()
printboard()