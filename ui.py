from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class Quiz_interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text="Score: 0", fg="white")
        self.label.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, background="white")
        self.text = self.canvas.create_text(150, 125, text="insert questions", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)


        #false button
        false_image = PhotoImage("images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)
        #true button
        true_image = PhotoImage("images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)
        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="No more questions available")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")


    def true_answer(self):
        verified_answer = self.quiz.check_answer("True")
        self.get_feedback(True)

    def false_answer(self):
        verified_answer = self.quiz.check_answer("false")
        self.get_feedback(False)

    def get_feedback(self, color: bool):
        if color == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question())


