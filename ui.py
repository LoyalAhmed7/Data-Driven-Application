import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0  # Initialize the question number to 0
        self.score = 0  # Initialize the score to 0
        self.question_list = q_list  # Assign the question list to the instance variable
        self.current_question = None  # Initialize the current question to None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)  # Check if there are still questions left

    def next_question(self):
        self.current_question = self.question_list[self.question_number]  # Get the current question
        self.question_number += 1  # Increment the question number
        q_text = html.unescape(self.current_question.text)  # Unescape the HTML characters in the question text
        return f"Q.{self.question_number}: {q_text} (True/False): "  # Return the formatted question text
      
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer  # Get the correct answer for the current question
        if user_answer.lower() == correct_answer.lower():  # Check if the user's answer is correct
            self.score += 1  # Increment the score if the answer is correct
            return True  # Return True if the answer is correct
        else:
            return False  # Return False if the answer is incorrect
