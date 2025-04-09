"""EX02: Wordle Exercise"""

__author__: str = "730549548"


def contains_char(word: str, char: str) -> bool:
    """We're checking to see if a letter is guessed correctly in the wordle"""
    assert (
        len(char) == 1  # this makes sure that we are checking one letter at a time
    ), f"len('{char}') is not 1"

    index = 0
    while index < len(
        word
    ):  # this goes through every character to see if a letter is matched
        if word[index] == char:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """We're giving the player hints to how close they are to the answer with color coded boxes (emojis)"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    # this makes sure the lengh of the guess and the length of the secret word are the same
    emojified_result = ""

    index = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            emojified_result += "\U0001F7E9"
        # if the letter is guessed correctly and its in the correct spot, we'll give out a green box
        elif contains_char(secret, guess[index]):
            emojified_result += "\U0001F7E8"
        # if a letter is guessed correctly but in the wrong spot, we'll give out a yellow box
        else:
            emojified_result += "\U00002B1C"
        # if they did not guess the letter correctly at all, we'll give out a white box
        index += 1

    return emojified_result


def input_guess(secret_word_len: int) -> str:
    """We're prompting the user for an input of a word with a certain number of characters"""
    guess = input("Enter a " + str(secret_word_len) + " character word: ")
    while (
        len(guess) != secret_word_len
    ):  # this continues to ask the user to guess a word until they guess a word with the correct length
        guess = input("That wasn't " + str(secret_word_len) + " chars! Try again: ")
    return guess


def main(secret_word: str) -> None:
    """This is the loop that keeps the game going for a certain number of turns or until the secret word is guessed correctly"""
    # the secret word is codes
    turns = 1
    won = False
    while turns <= 6 and not won:
        print(
            "Turn " + str(turns) + "/6"
        )  # going thru the game and printing (turn)/6 if not guessed correctly
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))

        if (
            guess == secret_word
        ):  # if they guessed word correctly, the player is notified of their win!
            won = True
            print("You won in " + str(turns) + "/6 turns!")
        else:  # if they did not guess correctly, we move on to the next turn
            turns += 1

    if (
        not won
    ):  # if they did not guess correctly after 6 turns, the player is notified of their loss!
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")
