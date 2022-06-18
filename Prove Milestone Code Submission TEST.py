word_tuple = ("c", "o", "d", "e", "c")

# We use this list to keep in memory the letters found
found = [False] * len(word_tuple)

word = ""

# The `all` method return True only if the list contains only True values
# Which means, while all letters are not found

while not all(found):
    # the `lower` method allows you to not take in account the uppercases
    word = input("Give a word of " +  str(len(word_tuple)) + " characters: ").lower()

    if len(word) == len(word_tuple):
        for charac in word_tuple:
            if charac in word:
                found = [b or word_tuple[index] in word for index, b in enumerate(found)]
        # The `any` method return True only if the list contains at least one True value
        # Which means we print Wrong only if there is no letter found
        if not any(found):
            print('Wrong!')
        else:
            print('Almost there! The word is "', end='')
            for i in range(len(word_tuple)):
                if found[i]:
                    print(word_tuple[i], end="")
                else:
                    print('*', end='')
            print('"')

    else:
        print('Wrong!')
# The method `join` allows you to join every string of an iterable
# Which means it joins every character of your tuple to a printable string
while word != ''.join(word_tuple):
    print('Close, try again')
    word = input("Give a word of " +  str(len(word_tuple)) + " characters: ").lower()

print('You found the word!')