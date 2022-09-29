print ("----Welcome to tic tac toe game-----")
import random
pos=[[1,2,3],[4,5,6],[7,8,9]]
player_one_turn=True
player_two_turn=False
player1_symbol="X"
player2_symbol="O"
#printing the board of the game
def print_board(position):
  print('{0:^2} | {1:^2} | {2:^2}'.format(position[0][0],position[0][1],position[0][2]))
  print('{0:^2} | {1:^2} | {2:^2}'.format(position[1][0],position[1][1],position[1][2]))
  print('{0:^2} | {1:^2} | {2:^2}'.format(position[2][0],position[2][1],position[2][2]))

print_board(pos)
players=["player_one","player_two"]
player_key=random.choice(players)
start=str(player_key)
#players choosing the position 
def who_play(number,symbol):  
  if number==1:
    pos[0][0]=symbol
  elif number==2:
    pos[0][1]=symbol
  elif number==3:
    pos[0][2]=symbol
  elif number==4:
    pos[1][0]=symbol
  elif number==5:
    pos[1][1]=symbol
  elif number==6:
    pos[1][2]=symbol
  elif number==7:
    pos[2][0]=symbol
  elif number==8:
    pos[2][1]=symbol
  elif number==9:
    pos[2][2]=symbol  
  print_board(pos) 
if start=="player_one": 
  player_one_turn==True 
  player_two_turn==False
elif start=="player_two":
  player_two_turn=False
  player_one_turn=True

#flip the columns into rows 
def flip(array):
  pos_vertical=[[array[0][0],array[1][0],array[2][0]],
  [array[0][1],array[1][1],array[2][1]],
  [array[0][2],array[1][2],array[2][2]]]
  return pos_vertical
# find diagonal array
def diagonal(array):
  pos_diagonal=[[array[0][0],array[1][1],array[2][2]],
                [array[0][2],array[1][1],array[2][0]]]
  return pos_diagonal
# test the array with the symbols 
def test_general(array,given_symbol):  
  count_winner=False
  for i in range(0,len(array)):  
    if given_symbol==array[i][:]:
      count_winner=True
      break  
  return(count_winner)     
# test the horizontal, vertical and diagonal and return final value  
def check_array(test_general,array,symbol):
  final_result=False
  horizontal_flag=test_general(array,symbol)  
  new_array=flip(array)
  vertical_flag=test_general(new_array,symbol)
  diagonal_array=diagonal(array) 
  diagonal_flag=test_general(diagonal_array,symbol)
  final_result= horizontal_flag or vertical_flag or diagonal_flag
  return(final_result)
#check for the winner  
player1_result=False
player2_result=False
symbol_O_ver=["O","O","O"]
symbol_X_ver=["X","X","X"]
continue_game=True
while continue_game==True:
  for i in range(1,10): 
    if player_one_turn==True:  # flipping between player1 and player two
      player_one=int(input(f"player 1 turn,your symbol is: {player1_symbol} , Enter position: "))
      who_play(player_one,player1_symbol) 
      player_one_turn= not player_one_turn
      player_two_turn= not player_two_turn
    else:
      player_two=int(input(f"player 2 turn,your symbol is: {player2_symbol} , Enter position: "))
      who_play(player_two,player2_symbol)
      player_two_turn=not player_two_turn
      player_one_turn=not player_one_turn
    #testing the symbols X and O in the game board at each entery 
    result_of_X=check_array(test_general,pos,symbol_X_ver)
    result_of_O=check_array(test_general,pos,symbol_O_ver)
    # set the symbol for the each player
    if player1_symbol=="X":
      player1_result=result_of_X
      player2_result=result_of_O
    else:
     player1_result=result_of_O
     player2_result=result_of_X 
  
    if player1_result==True:
      print("Player 1 has Won!\nGame Over!")
      break
    elif player2_result==True:
      print("Player 2 has Won!\nGame Over!")
      break
  if player1_result==player2_result==False:
      print("tie\nGame Over!")
  input_value=input("Do you want to play again? Enter Y or N:").lower()
  if input_value=="y":
    continue_game=True
  elif input_value=="n":
    continue_game=False
    print("Thank you")
    

      
  







  









