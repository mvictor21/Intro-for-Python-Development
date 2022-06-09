print("Welcome to the word guessing game!")
print(" ")
secret_word = "heaven"
guess_count = 0
life = 6

while life > 0:
    guess = input(f"Your hint is: ")

    if guess not in secret_word:
        print("")
        print(f"Your hint is: {guess}")
    
    for letter in secret_word:
        if letter in guess:
            print(letter,end=r"")
        else:
            print(r"_",end="")
        
    if guess == secret_word:
        print("")
        print("You guessed it!")
        break
    guess_count = guess_count+1

print(f"It took you {guess_count} guesses")