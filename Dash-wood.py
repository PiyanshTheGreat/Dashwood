import random
from python.Dashwood.Movies import movies
welcome_message="Welcome to Dash-wood!"
print(welcome_message)
woods=["Bollywood", "Hollywood", "Marvelwood"]

number=1
for wood in woods:
    print(f"{number}. {wood}")
    number=number + 1

gamemode=input("What -wood would you like to choose? ")
if gamemode.isdigit() and 1<= int(gamemode) <= len(woods):
    chosen_wood=woods[int(gamemode)-1]
elif gamemode.capitalize() in woods:
    chosen_wood=gamemode.capitalize()
else:
    chosen_wood="Invalid Input"

if chosen_wood=="Invalid Input":
    print("Please a valide wood/number")
else:
    print("Gamemode: ", chosen_wood.upper())
    chosen_movie=random.choice(movies[chosen_wood])
    autofill_characters="""AEIOU~`!@#$%^&*()-_=+{[}]\|:;'"<>?,./1234567890"""

    board=[]    
    for letter in chosen_movie.upper():
        if letter in autofill_characters:
            board.append(letter)
        elif letter == " ":
            board.append("/")
        else:
            board.append("_")
    print("".join(board).replace("/", " / ").replace("_", " _ "))
    lives=list(chosen_wood.upper())
    while "_" in board:
        guess=input("Guess a Letter: ").upper()
        if guess in chosen_movie.upper():
            for index, letter in enumerate(chosen_movie.upper()):
                if letter==guess:
                    
                    board[index]=guess
        else:
            if len(lives)==0:
                print("".join(lives))
                print("You Lost :(")
                print("The Movie was: ", chosen_movie)
                break
            elif guess==lives[0]:
                print("".join(lives))
                print("Wrong, but no life deducted since you guessed the life letter you are currently on")
            else:
                lives.pop(0)
                print("".join(lives))
                print("Wrong Guess :( ")
        print("".join(lives))
        print("".join(board).replace("/", " / ").replace("_", " _ "))
    else:
        print("You Guessed the movie correctly!: ", chosen_movie)
