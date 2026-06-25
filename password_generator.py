import random
import string

print("===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length should be at least 4.")
            continue

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        all_characters = lowercase + uppercase + digits + symbols

        password = (
            random.choice(lowercase)
            + random.choice(uppercase)
            + random.choice(digits)
            + random.choice(symbols)
        )

        for _ in range(length - 4):
            password += random.choice(all_characters)

        password_list = list(password)
        random.shuffle(password_list)
        password = "".join(password_list)

        print("\nGenerated Password:")
        print(password)

        again = input("\nGenerate another password? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")