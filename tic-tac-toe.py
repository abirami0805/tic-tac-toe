import time
def board(a,mark=""):
    print(a[1]+"|"+a[2]+"|"+a[3])
    print(a[4]+"|"+a[5]+"|"+a[6])
    print(a[7]+"|"+a[8]+"|"+a[9])
    result=win_check(a,mark)
    return result
    
def win_check(a,mark):
    if (( a[1] == a[2] == a[3] == mark ) or( a[4] == a[5] == a[6] == mark) or( a[7] == a[8] == a[9] == mark)
        or( a[1] == a[4] == a[7] ==mark) or( a[2] == a[5] == a[8] ==mark) or( a[3] == a[6] == a[9] == mark )
        or( a[1] == a[5] == a[9] ==mark) or( a[3] == a[5] == a[7] ==mark)) :
        win=1
        return win
    elif (a[1] == ' ' or a[2] == ' ' or a[3] == ' '
          or a[4] == ' ' or a[5] == ' ' or a[6] == ' '
          or a[7] == ' ' or a[8] == ' ' or a[9] == ' '):
        win=0
        return win  
    else:
        win=2
        return win
        
        
play='yes'
ch=['']
while play=='yes':    
  test =[' ']*10
  board(test)
  player1=input("choose 'x' or 'o' :")
  if player1 == 'x':
    player2 = 'o'
  else:
    player2 = 'x'
  print("PLAYER 1 : {}".format(player1))
  print("PLAYER 2 : {}".format(player2))
  alt=0
  win=0
  while win == 0:
   found=0
   if alt%2 == 0 :
      pos=int(input("enter the position (1-9) player 1:"))
      for x in ch:
        if pos == x:
          found = 1
      if found == 1:
        print("place occupied !")
        continue
      test[pos]=player1
      win=board(test,player1)
      alt=alt+1
      ch.append(pos)
   else:
      pos=int(input("enter the position (1-9) player 2:"))
      for x in ch:
        if pos == x:
          found = 1
      if found == 1:
        print("place occupied !")
        continue
      test[pos]=player2
      win=board(test,player2)
      alt=alt+1
      ch.append(pos)
  if win == 1 :
    print("yay you won")
  elif win == 2 :
    print("oops ... its a tie ")
  play=input("do you want to play again? (yes/no) :")
time.sleep(2)  
if play == 'no':
    print("see you later ....")
time.sleep(2)
