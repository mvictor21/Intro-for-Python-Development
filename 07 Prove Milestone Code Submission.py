print("Welcome to the word guessing game!")
print(" ")
secret_word = "heaven"
guess_count = 0
display = '_'*len(secret_word)

(len(secret_word)-1)
word = ["_"] * len(secret_word)
while True:
    guess = input("What is your guess? ")
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            word[i] = guess
    if guess == secret_word:
        print("")
        print("You guessed it!")
        break
    else:
        print("".join(word))
        guess_count = guess_count+1

print(f"It took you {guess_count} guesses")