class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "choices": ["a. Berlin", "b. Madrid", "c. Paris", "d. Rome"],
                "answer": "c"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "choices": ["a. Earth", "b. Jupiter", "c. Mars", "d. Saturn"],
                "answer": "b"
            },
            {
                "question": "What is the boiling point of water?",
                "choices": ["a. 90°C", "b. 100°C", "c. 110°C", "d. 120°C"],
                "answer": "b"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "choices": ["a. Charles Dickens", "b. William Shakespeare", "c. Mark Twain", "d. Jane Austen"],
                "answer": "b"
            },
            {
                "question": "What is the chemical symbol for gold?",
                "choices": ["a. Ag", "b. Au", "c. Pb", "d. Fe"],
                "answer": "b"
            }
        ]
        self.score = 0

    def start_quiz(self):
        print("Welcome to the Quiz! Answer the following questions:")
        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i+1}: {question['question']}")
            for choice in question['choices']:
                print(choice)
            answer = input("Your answer (a/b/c/d): ").strip().lower()
            if answer == question['answer']:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}.")

        self.show_result()

    def show_result(self):
        print("\nQuiz completed!")
        print(f"Your total score is: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()
