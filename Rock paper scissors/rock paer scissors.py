#game of rock,paper scissors
import random

ch=input("enter rock,paper or scissors   ")
computer_guess=random.choice(["rock","paper","scissors"])
if ch== "rock" and computer_guess=="paper":
    print("computer won")
elif ch=="paper" and computer_guess=="scissors":
    print("computer won")
elif ch=="scissors" and computer_guess=="rock":
    print("computer won")
elif ch==computer_guess:
    print("draw!")
else:
    print("you won")            
