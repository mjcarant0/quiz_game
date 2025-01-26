#Python Quiz Game
import os

#loop for account sign up and log in
print("Welcome to the QuizUP!")
while True:
    print("1. Create an Account")
    print("2. Log in")
    print("3. Exit")
    
    option = input("Choose an option (1, 2, 3): ")
    
    if option == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        with open("quiz_game_account.txt", "r") as file:
            accounts = file.readlines()
            for account in accounts:
                stored_username = account.split(",")[0]
                if stored_username == username:
                    print("Account already exist! Please choose a different username.")
                    break
                else:
                    with open("quiz_game_account.txt", "a") as file:
                        file.write(f"{username},{password}\n")
                    print("Account created successfully")
    elif option == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        with open("quiz_game_account.txt", "r") as file:
            account = file.readlines()
            for account in accounts:
                stored_username, stored_password = account.strip().split(",")
                if stored_username == username and stored_password == password:
                    print("Log in successful!")
                    break
                else:
                    print("Invalid username or password")
                    continue
        
        break
    elif option == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid option, please try again.")
        
#loop to create and use a quiz folder, and take quiz
while True:
    print("What would you like to do?")
    print("1. Create a new quiz folder")
    print("2. Use an existing quiz folder")
    print("3. Exit the program")
    
    folder_choice = input("Choose an option (1, 2, 3): ")
    
    if folder_choice == "1":
        folder_name = input("Enter a name for your new quiz folder: ")
        folder_path = os.path.join(username, folder_name)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_name}' created successfully!")
        else:
            print(f"The folder '{folder_name}' already exists.")
            
        # Ask user to create questions and answers for the new quiz
        questions = []
        answers = []
        
        while True:
            question = input("Enter a question (or type 'done' to finish): ")
            if question == "done":
                break
            answer = input(f"Enter the answer for '{question}: ")
            
            questions.append(question)
            answers.append(answer)
            
        with open(os.path.join(folder_path, "quiz_game_account.txt"), "w") as file:
            for i in range(len(questions)):
                file.write(f"Q: {questions[i]}\nA: {answers[i]}\n\n")
                
        print("Your quiz has been saved in the folder.")
        
#list down the questions for the quiz
questions = ("What programming language is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics, used for general-purpose programming?: ",
             "Who created python?: ",
             "What is the date of first released of python?: ",
             "Where did the name of Python came from?: ", 
             "The python is maintained by?: ")
#list down the choices of each questions
options = (("A. Python", "B. CSS", "C. C++", "D. Java"),
           ("A. Anders Hejlsberg", "B. Bjarne Stroustrup", "C. Ada Lovelace", "D. Guido van Rossum"),
           ("A. February 21, 1989", "B. January 21, 1991", "C. February 20, 1991", "D. March 20, 1989"),
           ("A. Large Snake", "B. Kaa from The Jungle Book", "C. Ekans from Pokémon", "D. Monty Python's Flying Circus"),
           ("A. Guido van Rossum", "B. Python Software Foundation", "C. Rossum Foundation", "D. Python Programming Association"))
#list down the correct answer of each questions
answers = ("A", "D", "C", "D", "B")
# Initialize lists and counters to track player's guesses, current score, and question number
guesses = []
score = 0
question_num = 0
#print the questions and options/answers
for question in questions:
    print("-----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1
#print the result which is the correct answers of each questions, answers of the player, and score in percentage
print("-----------------------------------")
print("             RESULTS               ")
print("-----------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")



#reference video https://www.youtube.com/watch?v=zehwgTB0vV8
#reference of questions and answers https://pythoninstitute.org/about-python#:~:text=Python%20was%20created%20by%20Guido,called%20Monty%20Python's%20Flying%20Circus.