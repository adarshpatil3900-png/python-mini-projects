# python rock, paper, scissors game 
import random

options = ("rock","paper","scissors")
running = True

while running:

  player = None
  computer = random.choice(options)

  while player not in options:
    player = input(f"Enter a choice (rock, paper, scissors) :")

  print(f"player: {player}")
  print(f"computer: {computer}")

  if player == computer:
    print(f"its a tie")
  elif player == "paper" and computer == "rock":
    print(f"you win !")
  elif player == "rock" and computer == "paper":
    print(f"you win!")
  elif player == "scissors" and computer == "paper":
    print(f"you win!")
  else:
    print(f"you lose!")

  if not input("play again ? (y/n): ").lower()=="y":
    running = False

print(f"THANKS FOR PLAYING !")