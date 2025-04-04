import random

def computer():
    return random.choice(['rock','paper','scissors'])
def get_winner(player,computer):
    if player==computer:
        return"it's a tie!"
    
    elif (player=='rock'and computer=='scissors') or\
         (player=='scissors'and computer=='paper') or\
         (player=='paper'and computer=='rock'):
        return"you win!"
         
    else:
        "computer wins!"


def main():
    while True:
        player_choice=input("Enter rock,paper or scissors (or'quit' to exit):").lower()

        if player_choice=='quit':
            print("Thanks for playing")
            break
        if player_choice not in ['rock','paper','scissors']:
            print("Invalid choice,Try again")
            continue
        computer_choice=computer()
        print(f"computer chose:[computer_choice]")
        print(get_winner(player_choice,computer_choice))



if __name__ == "__main__":
    main()

        