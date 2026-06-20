import random

print("=== Rock Paper Scissors Game ===")

user_score = 0
computer_score = 0

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("\nYour Choice:", choice)
    print("Computer Choice:", computer_choice)

    if choice == computer_choice:
        print("It's a Tie!")

    elif (
        (choice == "rock" and computer_choice == "scissors") or
        (choice == "paper" and computer_choice == "rock") or
        (choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScore Board")
    print("You:", user_score)
    print("Computer:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\n=== Final Score ===")
print("You:", user_score)
print("Computer:", computer_score)

if user_score > computer_score:
    print("Congratulations! You won the game.")
elif computer_score > user_score:
    print("Computer won the game.")
else:
    print("The game ended in a tie.")

print("Thank you for playing!")