print("You've 12 chances, Good Luck ! ", "Junaid")

word=input("Player one Enter anything to let guess for player two : ")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
l=len(word)
print("Guess the characters:")

guesses = ''
A=""


turns = 12                              # any number of turns can be used here

while turns > 0:

    failed = 0                          # counts the number of times a user fails
    print(end="              ")
    for i in range(1,l+1):
        print(i,end=" ")
    print()
                                        # all characters from the input
                                        # word taking one at a time.
    print(end="              ")
    for char in word:

                                        # comparing that character with
                                        # the character in guesses

        if char in guesses:
            print(char,end=" ")

        else:
            print("*",end=" ")
            failed += 1                         # for every failure 1 will be
                                                # incremented in failure

    if failed == 0:
                                                # user will win the game if failure is 0
                                                # and 'You Win' will be given as output

        print("\nYou Win")

        # this print the correct word
        print("The word is: ", word)
        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("\nguess a character: ")
    if guess in word:
        pass
    else:
        A+=" "+guess
    print("Wrong letters :",end="")
    print("\t\t\t\t\t",A)

    guesses += guess                        # every input character will be stored in guesses

    if guess not in word:                   # check input with the character in word

        turns -= 1

                                            # if the character doesn’t match the word
                                            # then “Wrong” will be given as output
        print("W R O N G")

                                            # this will print the number of
                                            # turns left for the user
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
            print("The word was: ", word)