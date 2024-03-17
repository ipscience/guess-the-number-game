import sys
import random

def read_int(prompt, error_message="Invalid input. Please enter a valid integer."):
    """Helper function to read an integer from stdin with error handling."""
    while True:
        sys.stdout.buffer.write(prompt.encode())
        sys.stdout.flush()
        try:
            return int(sys.stdin.buffer.readline())
        except ValueError:
            sys.stdout.buffer.write(error_message.encode() + b'\n')
            sys.stdout.flush()

def main():
    sys.stdout.buffer.write(b'Guess-the-number game\n')

    minNumber = read_int('Enter the minimum number: ')
    maxNumber = read_int('Enter the maximum number: ')

    # Ensure minNumber is less than or equal to maxNumber
    if minNumber > maxNumber:
        minNumber, maxNumber = maxNumber, minNumber

    randNumber = random.randint(minNumber, maxNumber)

    tries = maxNumber - minNumber + 1
    for _ in range(tries):
        guessNumber = read_int('Guess the number: ')

        if guessNumber == randNumber:
            sys.stdout.buffer.write(b'You win!\n')
            sys.stdout.flush()
            break
        elif guessNumber < randNumber:
            sys.stdout.buffer.write(b'The number is higher.\n')
        else:
            sys.stdout.buffer.write(b'The number is lower.\n')
        sys.stdout.flush()
    else:
        sys.stdout.buffer.write(b'You lose! The number was: ' + str(randNumber).encode() + b'\n')
        sys.stdout.flush()

if __name__ == '__main__':
    main()
