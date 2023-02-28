
import random
options = ["Rock","Paper","Scissor"]

computer = random.choice(options)

print("Select an Option from below")
user = input(options)

print( "You chose :"+user)
print("Computer is :"+computer)

if computer == user:
    print("Its a tie!")

else:
    if user =="Rock":
        if computer == "Scissor":
            print("Rock smashes Scissors! You won!")
        elif computer == "Paper":
            print("Paper Covers Rock. Computer wins!")
    elif user == "Paper":
        if computer == "Rock":
            print("Paper Covers Rock . You won! ")
        elif computer == "Scissor":
            print("Scissor cuts Paper . Computer wins! ")
    else:
        if computer == "Rock":
            print("Rock destroyes Scissors . Computer wins! ")
        elif computer == "Paper":
            print("Scissor cuts Paper . You won! ")





