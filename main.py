import random

def draw_board(scores):
    print("     |     |     ")
    print("  ", end = "")
    print(scores[0], end = "")
    print("  |  ", end = "")
    print(scores[1], end = "")
    print("  |", end = "")
    print("  ", end = "")
    print(scores[2])
    print("-----|-----|-----")
    print("  ", end = "")
    print(scores[3], end = "")
    print("  |  ", end = "")
    print(scores[4], end = "")
    print("  |", end = "")
    print("  ", end = "")
    print(scores[5])
    print("-----|-----|-----")
    print("  ", end = "")
    print(scores[6], end = "")
    print("  |  ", end = "")
    print(scores[7], end = "")
    print("  |", end = "")
    print("  ", end = "")
    print(scores[8])
    print("     |     |     ")
def player_move(scores, player):
    number = int(input("Pick a number 1 - 9: "))
    number -= 1
    if scores[number] == " " and number > -1 and number < 10 and scores[number] != 'X' and scores[number] != 'O':
        scores[number] = player
        quit
    else:
        print("invalid Choice, Try again.")
        player_move(scores, player)
def computer_move(scores, computer, computer_scores):
    number = random.randint(1, 9) - 1

    while number in computer_scores or scores[number] != " ":
       number = random.randint(0, 8)

    computer_scores.append(number)
    print(computer_scores)

    scores[number] = computer
def check_winner(scores):
   if scores[0] == player and scores[0] != " " and scores[0] == scores[1] and scores[1] == scores[2]:
       print("You have WON!")
       return True
   elif scores[3] == player and scores[3] != " " and scores[3] == scores[4] and scores[4] == scores[5]:
       print("You have WON!")
       return True
   elif scores[6] == player and scores[6] != " " and scores[6] == scores[7] and scores[7] == scores[8]:
       print("You have WON!")
       return True
   elif scores[0] == player and scores[0] != " " and scores[0] == scores[3] and scores[3] == scores[6]:
       print("You have WON!")
       return True
   elif scores[1] == player and scores[1] != " " and scores[1] == scores[4] and scores[4] == scores[7]:
       print("You have WON!")
       return True
   elif scores[2] == player and scores[2] != " " and scores[2] == scores[5] and scores[5] == scores[8]:
       print("You have WON!")
       return True
   elif scores[0] == player and scores[0] != " " and scores[0] == scores[4] and scores[4] == scores[8]:
       print("You have WON!")
       return True
   elif scores[2] == player and scores[2] != " " and scores[2] == scores[4] and scores[4] == scores[6]:
       print("You have WON!")
       return True
   elif scores[0] == computer and scores[0] != " " and scores[0] == scores[1] and scores[1] == scores[2]:
       print("You have lost!")
       return True
   elif scores[3] == computer and scores[3] != " " and scores[3] == scores[4] and scores[4] == scores[5]:
       print("You have lost!")
       return True
   elif scores[6] == computer and scores[6] != " " and scores[6] == scores[7] and scores[7] == scores[8]:
       print("You have lost!")
       return True
   elif scores[0] == computer and scores[0] != " " and scores[0] == scores[3] and scores[3] == scores[6]:
       print("You have lost!")
       return True
   elif scores[1] == computer and scores[1] != " " and scores[1] == scores[4] and scores[4] == scores[7]:
       print("You have lost!")
       return True
   elif scores[2] == computer and scores[2] != " " and scores[2] == scores[5] and scores[5] == scores[8]:
       print("You have lost!")
       return True
   elif scores[0] == computer and scores[0] != " " and scores[0] == scores[4] and scores[4] == scores[8]:
       print("You have lost!")
       return True
   elif scores[2] == computer and scores[2] != " " and scores[2] == scores[4] and scores[4] == scores[6]:
       print("You have lost!")
       return True
   else:
       return False       
def check_tie(scores):
   if " " not in scores:
       print("Its a tie!")
       return True

scores = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player = 'X'
computer_scores = []
computer = 'O'
running = True

draw_board(scores)

while (running):

    player_move(scores, player)
    draw_board(scores)
    if check_winner(scores):
        running = False
        break
    if check_tie(scores):
        running = False
        break

    computer_move(scores, computer, computer_scores)
    draw_board(scores)
    if check_winner(scores):
        running = False
        break
    if check_tie(scores):
        running = False
        break

print("Thank you for playing")