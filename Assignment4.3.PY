class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.user_scores = {}

    def take_quiz(self, user, answers):
        score = 0
        for i, answer in enumerate(answers):
            if answer == self.questions[i].correct_option:
                score += 1
        self.user_scores[user] = score
        print(f"Quiz completed. Your score: {score}")

class User:
    def __init__(self, username):
        self.username = username

# Example usage:
question1 = Question("What is the capital of France?", ["A. Berlin", "B. Madrid", "C. Paris"], "C")
question2 = Question("What is the largest planet in our solar system?", ["A. Earth", "B. Jupiter", "C. Mars"], "B")

quiz = Quiz([question1, question2])

user1 = User("SAMEER")
user2 = User("MEHAR")

quiz.take_quiz(user1, ["C", "B"])
quiz.take_quiz(user2, ["C", "A"])

print(f"User {user1.username}'s score: {quiz.user_scores[user1]}")
print(f"User {user2.username}'s score: {quiz.user_scores[user2]}")
