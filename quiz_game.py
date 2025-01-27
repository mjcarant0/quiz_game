#Python Quiz Game
import os

#file path for .txt file
file_path = r'D:\BSCpE\PLD\Individual\quiz_game\quiz_game_account.txt'

#loop for account sign up and log in
print("Welcome to the QuizUP!")
while True:
    print("1. Create an Account")
    print("2. Log in")
    print("3. Exit")
    
    option = input("Choose an option (1, 2, 3): ")
    
    #option 1
    if option == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        with open(file_path, "r") as file:
            accounts = file.readlines()
            
            account_exists = False #checking if the account already exists
            for account in accounts:
                stored_username = account.split(",")[0]
                if stored_username == username:
                    account_exists = True
                    print("Account already exist! Please choose a different username.")
                    break
            if not account_exists:
                with open(file_path, "a") as file:
                    file.write(f"{username},{password}\n")
                print("Account created successfully")
                
                user_folder_path = os.path.join("D:\\BSCpE\\PLD\\Individual\\quiz_game", username) #create a folder for user
                if not os.path.exists(user_folder_path):
                    os.makedirs(user_folder_path)
    #option 2            
    elif option == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        with open(file_path, "r") as file:
            accounts = file.readlines()
            logged_in = False
            for account in accounts:
                stored_username, stored_password = account.strip().split(",")
                if stored_username == username and stored_password == password:
                    logged_in = True
                    print("Log in successful!")
                    break
            if not logged_in:
                print("Invalid username or password")
                continue
        break
    #option 3
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
    
    #option 1
    if folder_choice == "1":
        user_folder_path = os.path.join("D:\\BSCpE\\PLD\\Individual\\quiz_game", username)
        
        quiz_folder_name = input("Enter the name of the new quiz folder: ")

        quiz_file_name = f"{quiz_folder_name}.txt"
        quiz_file_path = os.path.join(user_folder_path, quiz_file_name)
        
        questions = []
        answers = []
        
        while True:
            question = input("Enter a question (or type 'done' to finish): ")
            if question == "done":
                break
            answer = input(f"Enter the answer for '{question}': ")
            questions.append(question)
            answers.append(answer)
            
        #save quiz to a .txt file
        with open(quiz_file_path, "w") as file:
            for i in range(len(questions)):
                file.write(f"Q: {questions[i]}\nA: {answers[i]}\n\n")
        
        print(f"Your quiz has been saved in {quiz_file_name}.")
    
    #option 2
    elif folder_choice == "2":
        user_folder_path = os.path.join("D:\\BSCpE\\PLD\\Individual\\quiz_game", username)
        
        if os.path.exists(user_folder_path):
            existing_files = [f for f in os.listdir(user_folder_path) if f.endswith(".txt")]
            
            if existing_files:
                print("Here are your existing quizzes:")
                for idx, quiz_file in enumerate(existing_files, start=1):
                    print(f"{idx}. {quiz_file}")
                
                quiz_index = int(input(f"Choose a quiz (1-{len(existing_files)}): "))
                if 1 <= quiz_index <= len(existing_files):
                    quiz_file_name = existing_files[quiz_index - 1]
                    quiz_file_path = os.path.join(user_folder_path, quiz_file_name)
                    print(f"You chose the quiz: {quiz_file_name}")
                    
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("No quizzes found. Please create a new quiz first.")
        else:
            print(f"User folder '{username}' does not exist.")
    
    #option 3
    elif folder_choice == "3":
        print("Exiting the program.")
        break 
    
    else:
        print("Invalid option. Please try again.")
        
    #Create and take quiz
    take_quiz = input("Do you want to take a quiz in this folder? (yes/no): ").lower()
    
    if take_quiz == 'yes':
        while True:
            score = 0
            for i in range(len(questions)):
                print(f"Question {i+1}: {question[i]}")
                user_answer = input("Your answer: ").strip()
                if user_answer.lower() == answer[i].lower():
                    score += 1
                    print("Correct!")
                else:
                    print(f"Incorrect. The correct answer is: {answer[i]}")
                    
            print(f"Your final score: {score}/{len(questions)}")
            score_percentage = int(score / len(question) * 100)
            print(f"Your score percentage: {score_percentage}")
            
            retake_quiz = input("Would you like to retake the quiz? (yes/no: )").lower()
            if retake_quiz != "yes":
                break

#reference video https://www.youtube.com/watch?v=zehwgTB0vV8