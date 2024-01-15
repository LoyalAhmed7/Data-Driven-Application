# Import the necessary modules and classes
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Initialize the user_answer variable
user_answer = None

# Create an empty list to store the Question objects
question_bank = []

# Loop through the question_data list and create Question objects
for question in question_data:
    # Extract the question text and correct answer from the question dictionary
    question_text = question["question"]
    question_answer = question["correct_answer"]
    
    # Create a new Question object with the extracted data
    new_question = Question(question_text, question_answer)
    
    # Add the new_question to the question_bank list
    question_bank.append(new_question)

# Create a QuizBrain object with the question_bank
quiz = QuizBrain(question_bank)

# Create a QuizInterface object with the quiz
quiz_ui = QuizInterface(quiz)

# Print a message to indicate the completion of the quiz
print("You've completed the quiz")

# Print the final score of the quiz
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
