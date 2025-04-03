import random
def number_guessing_game():
    print("welcome to the number guessing game")
    secret=random.randint(1,10)
    attempts=0
    while True:
        try:
            guess=int(input("Guess a number between 1and10:"))
            attempts +=1
            if guess<secret:
                print("too low!Try again.")
            
            elif guess>secret:
                print("Too high!Try again")
            
            else:
                print("congratulations you guessed the number in {attempts} attempts")
                break

        except ValueError:
            print("pleas enter a valid number")

if __name__ == "__main__":
    number_guessing_game()