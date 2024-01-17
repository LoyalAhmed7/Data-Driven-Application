# Name: Ahmed Raheem #
# Campus: Bath Spa University, RAK #
# Class: Creative Computing Year 2 Group 1 #
# In this module we were asked to create a GUI using the APIs given in the Assessment Brief #
# I choose the Open Trivia API to create a quiz. My application name is Raquiz Trivia. It is a #
# multi choice quiz with 10 questions to answer correctly. #


from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from random import shuffle
import html

question_bank = []
for question in question_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question(question_text, correct_answer, choices)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)


print("This concludes the quiz")
print(f"Final Score: {quiz.score}/{quiz.question_no}")
