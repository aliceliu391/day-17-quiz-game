from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
quiz_brain = QuizBrain(question_bank)


for item in question_data:
    text = item["text"]
    answer = item["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was {quiz_brain.points}/{quiz_brain.question_number}")