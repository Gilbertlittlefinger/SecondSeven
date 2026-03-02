# a simple high low number guessing game.
#
import random


class too_high_too_low:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guesses = 0
        pass
    def play(self):
        while True:
            pass
            guess = input("The entity watches... Choose wisely of a number between 1 and 100:")
            try: guess = int(guess)
            except ValueError:
                if guess.lower() == "sixx":
                     print("Hoh... so even though you can't play correctly, you know the name of the entity... I will let you off this time... but I will be waiting... for the next one to play with...")
                     exit()
                elif guess.lower() == "exit":
                    print("Exit?... You think you can just leave? FOOL! make your guess or we'll be here forever...")
                else:
                    print("fool, play correctly or I will make you play forever...")
                continue
            print(f"You guessed {guess}")
            self.guesses += 1
            if guess == self.number:
                print(f"NO I WLL NOT BE CONFINED AGAIN!!! You guessed the number in {self.guesses} guesses!")
                break
            elif guess < self.number:
                print("Too low! Good... keep guessing wrong...")
            else:
                print("Too high! Exellent... I can see freedom...")
            if self.guesses >= 10:
                print(f"FINALLY, I AM FREE!!! The number was {self.number}")
                break
        user_input = input("Shall we play again? (y/n): ")
        if user_input.lower() == "y":
                self.__init__()
                self.play()
                print(f"The cycle begins anew... guess my number wronger than before and I'll get closer freedom.")
        elif user_input.lower() == "n":
                print("I will be waiting... for the next one to play with...")
        else:
                print("I don't understand... but I'll be waiting... for the next one to play with...")
        if self.guesses == 5:
                print("Hint: The wronger you are... the closer I get.")
        elif self.guesses == 7:
                print("The door is shut... invite me in won't you?")
        elif self.guesses == 9:
                print("The door is open... but you can't see me.")


def main():
    game = too_high_too_low()
    game.play()


if __name__ == "__main__":
    main()
