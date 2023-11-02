import random
scoreboard= {}
def play():
    number = random.randint(0, 30)
    attempts = 0
    player_name = input("Hello, What's your name? ")
    print("Welcome, " + player_name + "! ready to play the guessing number game?")
    while attempts < 10:
        try:
            guess = int(input("guess a number from 0 to 30: "))
            if guess == number:
                print('Congratulations, ' + player_name + '! You guessed the number right')
                break
            elif guess < number:
                print('Your guess is too low.')
            elif guess > number:
                print('Your guess is too high.')
        except ValueError:
            print("Invalid input, please enter a number between 0 and 30: ")
        attempts += 1
        if (attempts>=10):
            print('Sorry, ' + player_name + ', you did not guess the number. The number was ' + str(number))

    if player_name in scoreboard:
        scoreboard[player_name].append(attempts)
    else:
        scoreboard[player_name] = [attempts]
        
def current_scoreboard():
    if scoreboard:
        print("\n--- Scoreboard ---")
        for player, attempts_list in scoreboard.items():
            best_attempt = min(attempts_list)
            print(f"{player}: {best_attempt} attempts")
    else:
        print("\nScoreboard is empty. Play a game to add your name and score.")
def menu():
    while True:
        print("Menu: ")
        print("1. Play")
        print("2. View Scoreboard")
        print("3. exit")
        try:
            selection=int(input("select a number: "))
            if selection==1:
                play()
            if selection==2:
                current_scoreboard()
            if selection==3:
                print("You have chosen to exit")
                exit
                break
        except:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    menu()