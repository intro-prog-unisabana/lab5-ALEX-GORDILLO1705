from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response

def main():
    seed = int(input("Enter a seed number: "))
    seed_secret_numbers(seed)

    secret = generate_secret_number(1, 100)

    attempts = 0
    guessed = False

    while not guessed:
        guess = int(input("What is your guess: "))
        attempts += 1

        message, guessed = input_response(secret, guess)
        print(message)

    print(f"It took you {attempts} tries!")

if __name__ == "__main__":
    main()