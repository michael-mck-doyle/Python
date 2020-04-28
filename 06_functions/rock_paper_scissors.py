"""
take in a number 0-2 from the user that represents their hand
generate a random number 0-2 to use for the computer's hand
call the function get_hand to get the string representation of the user's hand
call the function get_hand to get the string representation of the computer's hand
call the function determine_winner to figure out who won
print out the player hand and computer hand
print out the winner

Instruction link here: https://github.com/CodingNomads/python_miniprojects/tree/master/rps_game

"""
from random import randrange


# take in a number 0-2 from the user that represents their hand
user_hand = int(input("Enter a number, 0 - 2: "))


# generate a random number 0-2 to use for the computer's hand
computer_hand = (randrange(0, 2))

rps = ["rock", "paper", "scissors"]


def get_user_hand(user_hand):
    x = rps[user_hand]
    return x


user = get_user_hand(user_hand)


def get_comp_hand(computer_hand):
    y = rps[computer_hand]
    return y


computer = get_user_hand(computer_hand)


def determine_winner(user, computer):
    if user == "rock" and computer == "paper":
        return "computer"
    elif user == "paper" and computer == "scissors":
        return "computer"
    elif user == "scissors" and computer == "rock":
        return "computer"
    elif computer == "rock" and user == "paper":
        return "user"
    elif computer == "paper" and user == "scissors":
        return "user"
    elif computer == "scissors" and user == "rock":
        return "user"
    else:
        return print(user, " : ", computer, " - It's a draw!")


winning_hand = determine_winner(user, computer)
print("The user hand is: ", user)
print("The computer hand is: ", computer)
print("The winner is...", winning_hand, "!!!")


