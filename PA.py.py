import random

def ask_questions():
    questions = [
        ("What is your name?", "name"),
        ("How old are you?", "age"),
        ("What is your favorite color?", "color"),
        ("What is your favorite food?", "food"),
        ("Which city do you live in?", "city"),
        ("Which SHS did you attend?", "shs"),
        ("What is your favourite soccer team?", "soccer_team"),
    ]

    random.shuffle(questions)

    answers = {}
    for question, key in questions:
        answer = input(question + " ")
        answers[key] = answer

    return answers

def display_summary(data):
    summary = (
        f"\n--- Personalized Summary ---\n"
        f"Hello, {data['name']}!\n"
        f"You are {data['age']} years old, love the color {data['color']}, and enjoy eating {data['food']}.\n"
        f"Life must be awesome in {data['city']}!\n"
        f"You attended {data['shs']} and support {data['soccer_team']} soccer team.\n"
    )
    print(summary)
    return summary

def save_to_file(name, summary, rating):
    filename = f"{name}.txt"
    with open(filename, "w") as file:
        file.write(summary)
        file.write(f"\nUser Rating: {rating} stars\n")
    print(f"Summary and rating saved to {filename}\n")

def main():
    while True:
        data = ask_questions()
        summary = display_summary(data)

        # Option to save
        save = input("Would you like to save this summary to a text file? (yes/no): ").strip().lower()
        if save == 'yes':
            # Ask for a fun rating
            while True:
                try:
                    rating = int(input("Please rate this assistant from 1 to 5 stars: "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            save_to_file(data['name'], summary, rating)

        # Option to restart
        restart = input("Would you like to restart and enter details again? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("Thank you for using the Simple Personal Assistant. Goodbye!")
            break

if __name__ == "__main__":
    main()
