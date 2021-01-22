import random
print("Welcome user")
print("Would you like to play a game?")
user_selection = input("Enter the key next to the option you would like to play.\n Games Available: \n -Number Guess: NG \n -Word Guess: WG \n :")


#Code for WordGuess
if user_selection.upper() == "WG":
    print("word guess opened")
    word_bank = open('random_words_list.txt', 'r')
    content = word_bank.read()
    print(content) 
    secret_word = content.split("")
    try: 
        print(content)
    except:
        print("error with line")
    else:
        print("nothing went wrong!")
    word_bank.close
    

#Number Guessing code when called.
print(user_selection.upper())
if user_selection.upper() == "NG":
    print("You Selected, Number Guess")
    secret_number = random.randrange(0,100)
    guesses = 7
    users_guess = ""
    while users_guess != secret_number:
        users_guess = int(input("Guess a number between 1 and 100: \n")) 
        if secret_number != users_guess > secret_number:
            print("***Your guess was a little too high, try again!***")
            guesses -= 1
            print(f"You have {guesses} guesses left")
        if secret_number != users_guess < secret_number: 
            print("***Your guess was too low, try again***")
            guesses -= 1
            print(f"You have {guesses} guesses left")
        if guesses == 0:
            print("You lose")
            break
    print(f"You guessed {users_guess}, that was correct!")



