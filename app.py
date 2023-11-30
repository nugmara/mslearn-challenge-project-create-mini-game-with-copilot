# Import necessary modules to a random game of rock, paper, scissors
import random
import os
import sys

# Initialize variables to keep track of player score and rounds played
player_score = 0
computer_score = 0
rounds = 0

# Define a function to get the player input
def player_input():
    # While loop to keep prompting user for input until valid
    while True:
        # Get input from user
        player_choice = input("Enter your choice: ")
        # Check if input is valid
        if player_choice.lower() in ["rock", "paper", "scissors"]:
            # Return the input if valid
            return player_choice
        # If input is not valid, print error message and prompt user for input again
        else:
            print("Invalid input. Please try again.")


# Define a function to determine the winner of each round
def winner(player_choice, computer_choice):
    # Declare global variables to be modified
    global player_score
    global computer_score
    global rounds
    # Check if player and computer made the same choice
    if player_choice == computer_choice:
        # If so, print a tie message
        print(f"You both chose {player_choice}. It's a tie!")
    # If player chose rock
    elif player_choice == "rock":
        # Check if computer chose paper
        if computer_choice == "paper":
            # If so, print a message that computer won
            print("Paper covers rock. Computer wins this round!")
            # Increment computer score by 1
            computer_score += 1
        # If computer chose scissors
        elif computer_choice == "scissors":
            # Print a message that player won
            print("Rock smashes scissors. You win this round!")
            # Increment player score by 1
            player_score += 1
    # If player chose paper
    elif player_choice == "paper":
        # Check if computer chose scissors
        if computer_choice == "scissors":
            # If so, print a message that computer won
            print("Scissors cut paper. Computer wins this round!")
            # Increment computer score by 1
            computer_score += 1
        # If computer chose rock
        elif computer_choice == "rock":
            # Print a message that player won
            print("Paper covers rock. You win this round!")
            # Increment player score by 1
            player_score += 1
    # If player chose scissors
    elif player_choice == "scissors":
        # Check if computer chose rock
        if computer_choice == "rock":
            # If so, print a message that computer won
            print("Rock smashes scissors. Computer wins this round!")
            # Increment computer score by 1
            computer_score += 1
        # If computer chose paper
        elif computer_choice == "paper":
            # Print a message that player won
            print("Scissors cut paper. You win this round!")
            # Increment player score by 1
            player_score += 1

# Main game loop
while True:
    # Clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    # Print the current score
    print(f"Player: {player_score} | Computer: {computer_score}")
    # Print the current round
    print(f"Round {rounds + 1}")
    # Get player input
    player_choice = player_input()
    # Generate computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    # Print the computer choice
    print(f"The computer chose {computer_choice}.")
    # Determine the winner of the round
    winner(player_choice, computer_choice)
    # Increment rounds by 1
    rounds += 1
    # Prompt user to play again or quit
    play_again = input("Play again? (y/n): ")
    # If user inputs y or yes, continue to next round
    if play_again.lower() in ["y", "yes"]:
        continue
    # If user inputs n or no, print final score and quit
    elif play_again.lower() in ["n", "no"]:
        print(f"Final score: Player: {player_score} | Computer: {computer_score}")
        sys.exit()
    # If user inputs anything else, print error message and quit
    else:
        print("Invalid input. Exiting...")
        sys.exit()
