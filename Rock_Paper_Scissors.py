import random

def game_wins(user,comp):
    # This function returns the results of the game.
    if user == comp:
        return None
    elif user == "rock":
        if comp == "paper":
            return False
        elif comp == "scissors":
            return True
    elif user == "paper":
        if comp == "rock":
            return True
        elif comp == "scissors":
            return False
    elif user == "scissors":
        if comp == "rock":
            return False
        elif comp == "paper":
            return True 

def accuracy(user):
    # Make the program more accurate and prevents user's mistake
    if user.startswith("r"):
        return "rock"
    elif user.startswith("p"):
        return "paper"
    elif user.startswith("s"):
        return "scissors"
    else:
        return False


print("--------------------------------------------------------------")
turns = int(input("Enter Your Turns: "))
won = 0
lose = 0
tie = 0
player = []
computer = []
play_turns = 0
for turn in range(1, turns+1):

    list = ["rock", "paper", "scissors"]
    comp = random.choice(list)
    
    print("--------------------------------------------------------------")
    user = input(f"{turn}.Enter your Choice: ")
    user = accuracy(user.lower())

    if user == False:
        print("Invalid Input!")
        print("Game Over!!!")
        break

    player.append(user)
    computer.append(comp)

    print(f"\nYou Choice '{user.capitalize()}' and Computer Choice '{comp.capitalize()}'")
    result = game_wins(user,comp)

    if result == None:
        print("\nGame is Tie!")
        tie = tie + 1
    elif result == True:
        print("\nYou Win the Game!")
        won = won + 1
    else:
        print("\nYou Lost the Game!")
        lose = lose + 1
    play_turns += 1

print("--------------------------------------------------------------")
print("Game Results")
print("--------------------------------------------------------------")
print(f"You Won: {won} times")
print(f"You Lose: {lose} times")
print(f"Game Tie: {tie} times")
print("--------------------------------------------------------------")

# Make a file for result
# This file is only created if user not enter any invalid input!!! 
if turns == play_turns:
    with open("Result.txt","w") as f:
        f.write("------------------------------------------------------\n")
        f.write("                Rock Paper Scissors\n")
        f.write("------------------------------------------------------\n")
        for turn in range(turns):
            f.write(f"Turn {turn+1}.\nYou Choice '{player[turn].capitalize()}' and Computer Choice '{computer[turn].capitalize()}'\n")
            f.write("------------------------------------------------------\n")

        f.write(f"You Won: {won} times\n")
        f.write(f"You Lose: {lose} times\n")
        f.write(f"You Tie: {tie} times\n")
        f.write("-------------------------------------------------------")
