import random as rand

#Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

difficulty = ['Easy','Medium','Hard']
print("Welcome to Rock Paper Scissors Xtra")
input("Press Enter to continue")
while(True):
    diff = input("\nChoose Difficulty, Easy, Medium or Hard\n")
    if diff in difficulty:
        break
    else:
        print("Difficulty not found")

while(True):
    print("\nChoose either Rock, Scissors, Paper")
    player = input("Pick your choice: ")
    if(player == 'Rock'):
        print(rock)
        break
    elif(player == 'Paper'):
        print(paper)
        break
    elif(player == 'Scissors'):
        print(scissors)
        break
    else:
        print("Pick a correct sign\n")

if(diff == "Easy"):
    computer = rand.choice(['Rock','Paper','Scissors'])
    if player == 'Rock' and computer == 'Scissors':
        print("Computer picked: "+computer)
        print(rock)
        print('Player wins!')
    elif player == 'Paper' and computer == 'Rock':
        print("Computer picked: "+computer)
        print(paper)
        print('Player wins!')
    elif player == 'Scissors' and computer == 'Paper':
        print("Computer picked: "+computer)
        print(scissors)
        print('Player wins!')
    else:
        computer = rand.choice(['Rock','Paper','Scissors'])
        print("Computer picked: "+computer)
        if(computer == 'Rock'):
            print(rock)
        elif(computer == 'Paper'):
            print(paper)
        else:
            print(scissors)
        if player == computer:
            print('DRAW!')
        elif player == 'Rock' and computer == 'Scissors':
            print('Player wins!')
        elif player == 'Rock' and computer == 'Paper':
            print('Computer wins!')
        elif player == 'Paper' and computer == 'Rock':
            print('Player wins!')
        elif player == 'Paper' and computer == 'Scissors':
            print('Computer wins!')
        elif player == 'Scissors' and computer == 'Paper':
            print('Player wins!')
        elif player == 'Scissors' and computer == 'Rock':
            print('Computer wins!')
    
if(diff == "Medium"):
    computer = rand.choice(['Rock','Paper','Scissors'])
    print("Computer picked: "+computer)
    if(computer == 'Rock'):
        print(rock)
    elif(computer == 'Paper'):
        print(paper)
    else:
        print(scissors)
    if player == computer:
        print('DRAW!')
    elif player == 'Rock' and computer == 'Scissors':
        print('Player wins!')
    elif player == 'Rock' and computer == 'Paper':
        print('Computer wins!')
    elif player == 'Paper' and computer == 'Rock':
        print('Player wins!')
    elif player == 'Paper' and computer == 'Scissors':
        print('Computer wins!')
    elif player == 'Scissors' and computer == 'Paper':
        print('Player wins!')
    elif player == 'Scissors' and computer == 'Rock':
        print('Computer wins!')
    
else:
    computer = rand.choice(['Rock','Paper','Scissors'])
    if player == 'Rock' and computer == 'Paper':
        print("Computer picked: "+computer)
        print(paper)
        print('Computer wins!')
    elif player == 'Paper' and computer == 'Scissors':
        print("Computer picked: "+computer)
        print(scissors)
        print('Computer wins!')
    elif player == 'Scissors' and computer == 'Rock':
        print("Computer picked: "+computer)
        print(rock)
        print('Computer wins!')
    else:
        computer = rand.choice(['Rock','Paper','Scissors'])
        print("Computer picked: "+computer)
        if(computer == 'Rock'):
            print(rock)
        elif(computer == 'Paper'):
            print(paper)
        else:
            print(scissors)
        if player == computer:
            print('DRAW!')
        elif player == 'Rock' and computer == 'Scissors':
            print('Player wins!')
        elif player == 'Rock' and computer == 'Paper':
            print('Computer wins!')
        elif player == 'Paper' and computer == 'Rock':
            print('Player wins!')
        elif player == 'Paper' and computer == 'Scissors':
            print('Computer wins!')
        elif player == 'Scissors' and computer == 'Paper':
            print('Player wins!')
        elif player == 'Scissors' and computer == 'Rock':
            print('Computer wins!')

input()
   
