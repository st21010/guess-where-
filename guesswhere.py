import random

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
def country_quiz():
    # Keep track of the score
    score = 0
    
    # Shuffle the list of countries
    country_list = list(countries.items())
    random.shuffle(country_list)
    
    # Iterate over the shuffled list of countries
    for country, capital in country_list[:4]:
        # Print the question
        print("What is the capital of", country + "?")
        
        # Define a list of answer options
        answer_options = [capital]
        
        # Add three random capitals to the answer options
        while len(answer_options) < 4:
            random_country, random_capital = random.choice(list(countries.items()))
            if random_capital not in answer_options:
                answer_options.append(random_capital)
        
        # Shuffle the answer options
        random.shuffle(answer_options)
        
        # Print the answer options
        for i, option in enumerate(answer_options):
            print(chr(i + 97) + ") " + option)
        
        # Get the user's answer
        user_answer = input("Enter your answer (a, b, c, or d): ")
        
        # Check if the answer is correct
        if user_answer.lower() == "a" and answer_options[0] == capital:
            score += 1
        elif user_answer.lower() == "b" and answer_options[1] == capital:
            score += 1
        elif user_answer.lower() == "c" and answer_options[2] == capital:
            score += 1
        elif user_answer.lower() == "d" and answer_options[3] == capital:
            score += 1
    
    # Print the final score
    print("Your score is:", score, "out of 4")
    
# Call the quiz function
country_quiz()
In this version of the quiz, the questions are randomly selected from a list of countries and their capitals, and the answer options are also randomly generated. The user is presented with four answer options (labeled a, b, c, and d), and their score is based on how many questions they answer correctly out of the four presented.
