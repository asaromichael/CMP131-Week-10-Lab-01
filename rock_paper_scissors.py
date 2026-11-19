import random

def main():
    PC_result = PC_choice()
    user_reseult = user_choice()
    win = winner(PC_result, user_result)
    Display(win)

main()

def PC_choice():
    choice = random.randInt(1, 3)
    if (choice == 1):
        return "Rock"
    elif (choice == 2):
        return "Paper"
    else:
        return "Scissors"

def user_choice ():
    choice = int(input("Press 1 for rock, 2 for paper, or 3 for scissors."))
    if (choice == 1):
        return "Rock"
    elif (choice == 2):
        return "Paper"
    else:
        return "Scissors"
