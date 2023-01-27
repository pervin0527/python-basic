from data import question_data, question_data2
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data2:
    # text, answer = question["text"], question["answer"]
    text, answer = question["question"], question["correct_answer"]
    question_object = Question(text, answer)
    question_bank.append(question_object)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You completed the quiz")
print(f"Your final score was {quiz_brain.score}/{len(quiz_brain.question_list)}")