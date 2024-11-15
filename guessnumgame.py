import random


def guess():
    count = 0
    num = random.randint(1, 128)

    while count < 7:
        guess_num = int(input("Guess a number between 1 and 128: "))
        if guess_num == num:
            return "Correct!"
        elif guess_num < num:
            count += 1
            print("Too low!")
        elif guess_num > num:
            count += 1
            print("Too high!")
        else:
            return "Invalid input!"

    else:
        return f"Too many attempts! The correct number was {num}."


if __name__ == '__main__':
    print(guess())
