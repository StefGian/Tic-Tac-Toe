#create a dictionary with keys and their values to use as a board
board = {
  "7": " ", "8": " ", "9": " ",
  "4": " ", "5": " ", "6": " ",
  "1": " ", "2": " ", "3": " "
}

boardKeys = []

#append the selected key to the list
for key in boardKeys:
  boardKeys.append(key)

#print board after every move
def printBoard (board):
  print (board["7"] + "  | " + board["8"] + "  | " + board["9"])
  print ("---+----+---")
  print (board["4"] + "  | " + board["5"] + "  | " + board["6"])
  print ("---+----+---")
  print (board["1"] + "  | " + board["2"] + "  | " + board["3"])

#main function

def game():
  turn = "X"
  count = 0

  for i in range(10):
    printBoard(board)
    print("It's your turn " + turn + ". Move to which place?")

    move = input()

    if board[move] == " ":
      board[move] = turn
      count += 1

    else:
      print("That place is already filled. Move to which place?")

    #Check if player X or O has won for every 5 moves
    if count >= 5:
      if board["7"] == board["8"] == board["9"] != " ":
        printBoard(board)
        print("\n Game Over \n")
        print("The player " + turn + " won!!")
        break
      elif board["4"] == board["5"] == board["6"] != " ":
        printBoard(board)
        print("\n Game Over \n")
        print("The player " + turn + " won!!")
        break
      elif board["1"] == board["2"] == board["3"] != " ":
        printBoard(board)
        print("\n Game Over \n")
        print("The player " + turn + " won!!")
        break
      elif board["1"] == board["4"] == board["7"] != " ":
        printBoard(board)
        print("\n Game Over \n")
        print("The player " + turn + " won!!")
        break
      elif board["2"] == board["5"] == board["8"] != " ":
        printBoard(board)
        print("\n Game Over \n")
        print("The player " + turn + " won!!")
        break
      elif board["3"] == board["6"] == board["9"] != " ":
        printBoard(board)
        print("\n Game Over \n")
        print("The player " + turn + " won!!")
        break
      elif board["7"] == board["5"] == board["3"] != " ":
        printBoard(board)
        print("\n Game Over \n")
        print("The player " + turn + " won!!")
        break
      elif board["1"] == board["5"] == board["9"] != " ":
        printBoard(board)
        print("\n Game Over \n")
        print("The player " + turn + " won!!")
        break

    #If neither X or O win and the board is full, it will be a tie
    if count == 9:
      print("\n Game Over \n")
      print("It's a tie!")

    #change player after each move
    if turn == "X":
      turn = "O"
    else:
      turn = "X"

      #ask if they want to play again
      replay = input("Would you like to play again? (y/n")
      if replay == "y" or replay == "Y":
        for key in boardKeys:
          board[key] = " "

        game()

if __name__ == "__main__":
  game()