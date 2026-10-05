import tkinter as tk
from tkinter import messagebox, ttk
import random


# -----------------------------
# Quiz Questions
# -----------------------------

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["input()", "print()", "display()", "output()"],
        "answer": "print()"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["String", "Integer", "Boolean", "Float"],
        "answer": "Boolean"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "/* */", "#", "--"],
        "answer": "#"
    },
    {
        "question": "Which data type stores multiple items?",
        "options": ["List", "Integer", "Boolean", "Float"],
        "answer": "List"
    },
    {
        "question": "Which keyword is used for a condition?",
        "options": ["when", "if", "check", "condition"],
        "answer": "if"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["^", "**", "//", "%%"],
        "answer": "**"
    },
    {
        "question": "Which language is this quiz application written in?",
        "options": ["Java", "C++", "Python", "HTML"],
        "answer": "Python"
    }
]


# -----------------------------
# Main Application
# -----------------------------

class QuizApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Python Quiz Application")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.username = ""
        self.current_question = 0
        self.score = 0
        self.time_left = 60

        self.quiz_questions = questions.copy()
        random.shuffle(self.quiz_questions)

        self.answers = [None] * len(self.quiz_questions)

        self.selected_answer = tk.StringVar()

        # Start Home Page
        self.home_page()


    # -----------------------------
    # Clear Current Page
    # -----------------------------

    def clear_page(self):

        for widget in self.root.winfo_children():
            widget.destroy()


    # -----------------------------
    # HOME PAGE
    # -----------------------------

    def home_page(self):

        self.clear_page()

        self.root.configure(bg="#EAF2F8")

        title = tk.Label(
            self.root,
            text="PYTHON QUIZ",
            font=("Arial", 32, "bold"),
            bg="#EAF2F8"
        )
        title.pack(pady=70)

        subtitle = tk.Label(
            self.root,
            text="Test Your Python Knowledge",
            font=("Arial", 18),
            bg="#EAF2F8"
        )
        subtitle.pack(pady=10)

        name_label = tk.Label(
            self.root,
            text="Enter Your Name",
            font=("Arial", 14, "bold"),
            bg="#EAF2F8"
        )
        name_label.pack(pady=20)

        self.name_entry = tk.Entry(
            self.root,
            font=("Arial", 16),
            width=25,
            justify="center"
        )
        self.name_entry.pack(pady=10)

        start_button = tk.Button(
            self.root,
            text="START QUIZ",
            font=("Arial", 16, "bold"),
            width=18,
            height=2,
            command=self.start_quiz
        )
        start_button.pack(pady=35)


    # -----------------------------
    # START QUIZ
    # -----------------------------

    def start_quiz(self):

        self.username = self.name_entry.get().strip()

        if self.username == "":
            messagebox.showwarning(
                "Name Required",
                "Please enter your name."
            )
            return

        self.current_question = 0
        self.score = 0
        self.time_left = 60

        self.quiz_questions = questions.copy()
        random.shuffle(self.quiz_questions)

        self.answers = [None] * len(self.quiz_questions)

        self.quiz_page()

        self.update_timer()


    # -----------------------------
    # QUIZ PAGE
    # -----------------------------

    def quiz_page(self):

        self.clear_page()

        self.root.configure(bg="#F8F9FA")

        # Header
        header = tk.Label(
            self.root,
            text=f"Welcome, {self.username}!",
            font=("Arial", 20, "bold"),
            bg="#F8F9FA"
        )
        header.pack(pady=15)

        # Question Number
        self.question_number = tk.Label(
            self.root,
            text="",
            font=("Arial", 14, "bold"),
            bg="#F8F9FA"
        )
        self.question_number.pack()

        # Timer
        self.timer_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14, "bold"),
            bg="#F8F9FA"
        )
        self.timer_label.pack(pady=5)

        # Progress Bar
        self.progress = ttk.Progressbar(
            self.root,
            length=500,
            mode="determinate"
        )
        self.progress.pack(pady=10)

        # Question
        self.question_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 18, "bold"),
            wraplength=650,
            justify="center",
            bg="#F8F9FA"
        )
        self.question_label.pack(pady=30)

        # Options
        self.option_buttons = []

        for i in range(4):

            button = tk.Radiobutton(
                self.root,
                text="",
                variable=self.selected_answer,
                value="",
                font=("Arial", 14),
                width=35,
                anchor="w",
                bg="#FFFFFF",
                padx=10,
                pady=8
            )

            button.pack(pady=5)

            self.option_buttons.append(button)


        # Navigation Frame
        navigation = tk.Frame(
            self.root,
            bg="#F8F9FA"
        )
        navigation.pack(pady=25)

        self.previous_button = tk.Button(
            navigation,
            text="← Previous",
            font=("Arial", 12, "bold"),
            width=12,
            command=self.previous_question
        )
        self.previous_button.grid(row=0, column=0, padx=15)

        self.next_button = tk.Button(
            navigation,
            text="Next →",
            font=("Arial", 12, "bold"),
            width=12,
            command=self.next_question
        )
        self.next_button.grid(row=0, column=1, padx=15)

        self.show_question()


    # -----------------------------
    # SHOW QUESTION
    # -----------------------------

    def show_question(self):

        question_data = self.quiz_questions[self.current_question]

        total = len(self.quiz_questions)

        self.question_number.config(
            text=f"Question {self.current_question + 1} of {total}"
        )

        self.question_label.config(
            text=question_data["question"]
        )

        # Progress
        progress_value = (
            (self.current_question + 1) / total
        ) * 100

        self.progress["value"] = progress_value

        # Previous Button
        if self.current_question == 0:
            self.previous_button.config(
                state="disabled"
            )
        else:
            self.previous_button.config(
                state="normal"
            )

        # Selected answer
        if self.answers[self.current_question] is not None:

            self.selected_answer.set(
                self.answers[self.current_question]
            )

        else:

            self.selected_answer.set("")


        # Options
        for i in range(4):

            self.option_buttons[i].config(
                text=question_data["options"][i],
                value=question_data["options"][i]
            )


        # Last question
        if self.current_question == total - 1:

            self.next_button.config(
                text="Finish ✓"
            )

        else:

            self.next_button.config(
                text="Next →"
            )


    # -----------------------------
    # NEXT QUESTION
    # -----------------------------

    def next_question(self):

        answer = self.selected_answer.get()

        if answer == "":
            messagebox.showwarning(
                "Select Answer",
                "Please select an answer."
            )
            return

        # Save answer
        self.answers[self.current_question] = answer

        # Last question
        if self.current_question == len(self.quiz_questions) - 1:

            self.calculate_score()
            self.result_page()

        else:

            self.current_question += 1
            self.show_question()


    # -----------------------------
    # PREVIOUS QUESTION
    # -----------------------------

    def previous_question(self):

        answer = self.selected_answer.get()

        if answer != "":
            self.answers[self.current_question] = answer

        if self.current_question > 0:

            self.current_question -= 1

            self.show_question()


    # -----------------------------
    # CALCULATE SCORE
    # -----------------------------

    def calculate_score(self):

        self.score = 0

        for i in range(len(self.quiz_questions)):

            correct_answer = self.quiz_questions[i]["answer"]

            if self.answers[i] == correct_answer:
                self.score += 1


    # -----------------------------
    # TIMER
    # -----------------------------

    def update_timer(self):

        if self.time_left > 0:

            minutes = self.time_left // 60
            seconds = self.time_left % 60

            self.timer_label.config(
                text=f"Time Left: {minutes:02d}:{seconds:02d}"
            )

            self.time_left -= 1

            self.root.after(
                1000,
                self.update_timer
            )

        else:

            messagebox.showinfo(
                "Time Up",
                "Time is over!"
            )

            self.calculate_score()
            self.result_page()


    # -----------------------------
    # RESULT PAGE
    # -----------------------------

    def result_page(self):

        self.clear_page()

        self.root.configure(bg="#E8F8F5")

        total = len(self.quiz_questions)

        percentage = (
            self.score / total
        ) * 100

        title = tk.Label(
            self.root,
            text="QUIZ COMPLETED!",
            font=("Arial", 30, "bold"),
            bg="#E8F8F5"
        )
        title.pack(pady=50)

        user_label = tk.Label(
            self.root,
            text=f"Well done, {self.username}!",
            font=("Arial", 20),
            bg="#E8F8F5"
        )
        user_label.pack(pady=10)

        score_label = tk.Label(
            self.root,
            text=f"Score: {self.score} / {total}",
            font=("Arial", 22, "bold"),
            bg="#E8F8F5"
        )
        score_label.pack(pady=10)

        percentage_label = tk.Label(
            self.root,
            text=f"Percentage: {percentage:.2f}%",
            font=("Arial", 18),
            bg="#E8F8F5"
        )
        percentage_label.pack(pady=10)


        if percentage >= 80:

            result = "Excellent! 🏆"

        elif percentage >= 60:

            result = "Good Job! 👏"

        elif percentage >= 40:

            result = "Keep Practicing! 📚"

        else:

            result = "Try Again! 💪"


        result_label = tk.Label(
            self.root,
            text=result,
            font=("Arial", 22, "bold"),
            bg="E8F8F5"
        )
        result_label.pack(pady=20)


        restart_button = tk.Button(
            self.root,
            text="RESTART QUIZ",
            font=("Arial", 14, "bold"),
            width=18,
            height=2,
            command=self.start_again
        )
        restart_button.pack(pady=10)


        exit_button = tk.Button(
            self.root,
            text="EXIT",
            font=("Arial", 14, "bold"),
            width=18,
            height=2,
            command=self.root.destroy
        )
        exit_button.pack(pady=10)


    # -----------------------------
    # RESTART
    # -----------------------------

    def start_again(self):

        self.time_left = 60

        self.home_page()


# -----------------------------
# Run Application
# -----------------------------

if __name__ == "__main__":

    root = tk.Tk()

    app = QuizApp(root)

    root.mainloop()