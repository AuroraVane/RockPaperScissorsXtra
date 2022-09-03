import random as rand
''' Module where string of shapes is being stored '''
from Assets import Shapes as shp

def Get_Shape(shape):
    if shape == "rock":
        return shp.Get_Rock()
    elif shape == "paper":
        return shp,Get_Paper()
    return shp,Get_Scissors()

def Setup_Game():
    ''' Select Difficulty and perform checks for typo'''

    difficulty = ['easy','medium','hard']
    choice = None
    while not choice in difficulty:
        choice = input("Choose Difficulty, Easy, Medium or Hard\n").lower()
        if choice in difficulty:
            return choice
            continue
        print("Type either Easy, Medium or Hard\n")

def Computate(inputs):
    def Check(num):
        if num == 0:
            return "P"
        return "C"
    
    ''' All is to check if all conditions in iterable is true'''
    if all(item in inputs for item in ['rock','paper']):
        '''Check which element contains the winning shape and return winner'''
        return Check(inputs.index('paper'))
    elif all(item in inputs for item in ['scissors','paper']):
        '''Check which element contains the winning shape and return winner'''
        return Check(inputs.index('scissors'))
    elif all(item in inputs for item in ['rock','scissors']):
        '''Check which element contains the winning shape and return winner'''
        return Check(inputs.index('rock'))
    return "D"
    
def main():        
    run = True
    print("\nWelcome to Rock Paper Scissors!\n\n")

    while run:
        diff = Setup_Game()
        player = input("\nChoose either Rock, Scissors, Paper\n").lower()
        pShape = Get_Shape(player)
        print(f"You Picked\n{pShape}")
        computer1 = rand.choice(['rock','paper','scissors'])
        computer2 = rand.choice(['rock','paper','scissors'])
        result1 = Computate([player,computer1])
        result2 = Computate([player,computer2])

        if diff == "easy":
            if result1 == "P" or result2 == "P":
                print("P Wins")
            elif result2 == "D":
                print("Draw")
            else:
                print("C Wins")

        elif diff == "hard":
            if result1 == "C" or result2 == "C":
                print("C Wins")
            elif result2 == "D":
                print("Draw")
            else:
                print("P Wins")
        else:
            if result1 == "C":
                print("C Wins")
            elif result1 == "D":
                print("Draw")
            else:
                print("P Wins")
        
if __name__ == "__main__":
    main()
