# step 1 choice word
# step 2 set nedded word
# step 3 write the neded code
# add if player can not find answare
# finished


word = "secrate "

allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")

        else:
            print("_", end=" " )

    print(" ")


    guess = input(f'Allowed errors left{allowed_errors},try nest guess: ')
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break
    done = True

    if letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f' You found the word .Your word {word} ')
else:
    print(f'Game over.Your word {word}')






