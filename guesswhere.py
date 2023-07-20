import random
import tkinter as tk
from tkinter import messagebox

# Define a list of countries and their capitals
countries = {
    "Argentina": "Buenos Aires",
    "Japan": "Tokyo",
    "India": "New Delhi",
    "Vatican City": "Vatican City",
    "Italy": "Rome",
    "Thailand": "Bangkok",
    "Brazil": "Brasilia",
    "France": "Paris",
    "Egypt": "Cairo",
    "South Africa": "Pretoria",
    "Mexico": "Mexico City",
    "Russia": "Moscow",
    "China": "Beijing",
    "Spain": "Madrid",
    "Australia": "Canberra",
    "Canada": "Ottawa",
    "Germany": "Berlin",
    "United Kingdom": "London",
    "South Korea": "Seoul",
    "Nigeria": "Abuja"
}

# Define a function to administer the quiz
def guesswhere_quiz():
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Guesswhere")

    # Create a score label
    score_label = tk.Label(window, text="Score: 0")
    score_label.pack()

    # Shuffle the list of countries
    country_list = list(countries.items())
    random.shuffle(country_list)

    # Keep track of the score
    score = 0

    # Define a function to handle answer submission
    def submit_answer(user_answer, capital):
        nonlocal score

        # Check if the answer is correct
        if user_answer.lower() == capital.lower():
            score += 1

        # Update the score label
        score_label.config(text="Score: {}".format(score))

        # Clear the entry field
        answer_entry.delete(0, tk.END)

        # Move to the next question
        ask_question()

    # Define a function to ask a new question
    def ask_question():
        # Check if all questions have been asked
        if len(country_list) == 0:
            # Display the final score in a message box
            messagebox.showinfo("Quiz Complete", "Quiz completed! Your final score is {} out of 4.".format(score))
            # Close the window
            window.destroy()
            return

        # Get the next country and capital
        country, capital = country_list.pop()

        # Clear the question frame
        for widget in question_frame.winfo_children():
            widget.destroy()

        # Create the question label
        question_label = tk.Label(question_frame, text="What is the capital of {}?".format(country))
        question_label.pack()

        # Define a list of answer options
        answer_options = [capital]

        # Add three random capitals to the answer options
        while len(answer_options) < 4:
            random_country, random_capital = random.choice(list(countries.items()))
            if random_capital not in answer_options:
                answer_options.append(random_capital)

        # Shuffle the answer options
        random.shuffle(answer_options)

        # Create the answer option buttons
        option_buttons = []
        for i, option in enumerate(answer_options):
            button = tk.Button(question_frame, text=option, command=lambda option=option: submit_answer(option, capital))
            button.pack()
            option_buttons.append(button)

    # Create the question frame
    question_frame = tk.Frame(window)
    question_frame.pack(pady=20)

    # Start the quiz
    ask_question()

    # Run the Tkinter event loop
    window.mainloop()

# Call the quiz function
guesswhere_quiz()
