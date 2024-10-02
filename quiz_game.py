#Python Quiz Game
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