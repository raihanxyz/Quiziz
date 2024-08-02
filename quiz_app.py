import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz")
        
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "What is the largest planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
            {"question": "What is the boiling point of water?", "options": ["90°C", "80°C", "100°C", "70°C"], "answer": "100°C"},
            {"question": "What is the square root of 9?", "options": ["2", "3", "4", "5"], "answer": "3"},
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=20)
        
        self.options_var = tk.StringVar(value="")
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.options_var, value="", tristatevalue="x")
            rb.pack(anchor="w")
            self.option_buttons.append(rb)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=20)
        
        self.display_question()
    
    def display_question(self):
        q = self.questions[self.current_question]
        self.question_label.config(text=q["question"])
        self.options_var.set("")
        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(text=option, value=option)
    
    def submit_answer(self):
        selected_option = self.options_var.get()
        if not selected_option:
            messagebox.showwarning("No selection", "Please select an answer!")
            return
        
        if selected_option == self.questions[self.current_question]["answer"]:
            self.score += 1
        
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_result()
    
    def show_result(self):
        result_text = f"You scored {self.score} out of {len(self.questions)}"
        messagebox.showinfo("Quiz Result", result_text)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
