import tkinter as tk
from tkinter import messagebox

# List of questions
questions = [
    {"prompt": "What is the name of the sword that was reforged into Andúril?",
     "choices": ["Glamdring", "Narsil", "Sting", "Orcrist"], "answer": "Narsil"},
    {"prompt": "Who is the eldest of the Ents in *The Lord of the Rings*?",
     "choices": ["Quickbeam", "Fangorn", "Treebeard", "Skinbark"], "answer": "Treebeard"},
    {"prompt": "Which city is known as the White City?",
     "choices": ["Edoras", "Minas Morgul", "Minas Tirith", "Osgiliath"], "answer": "Minas Tirith"},
    {"prompt": "What is the name of Sauron's all-seeing tower?",
     "choices": ["Barad-dûr", "Orthanc", "Weathertop", "Dol Guldur"], "answer": "Barad-dûr"},
    {"prompt": "What race is Legolas?",
     "choices": ["Dwarf", "Hobbit", "Elf", "Man"], "answer": "Elf"},
    {"prompt": "What is the name of the inn where Frodo and his companions meet Aragorn?",
     "choices": ["The Golden Perch", "The Prancing Pony", "The Green Dragon", "The Silver Spoon"],
     "answer": "The Prancing Pony"},
    {"prompt": "Who kills the Witch-King of Angmar?",
     "choices": ["Aragorn", "Eowyn", "Gandalf", "Legolas"], "answer": "Eowyn"},
    {"prompt": "What is the name of Gollum's original Hobbit-like self?",
     "choices": ["Deagol", "Bilbo", "Smeagol", "Frodo"], "answer": "Smeagol"},
    {"prompt": "Which creature does Gandalf battle on the Bridge of Khazad-dûm?",
     "choices": ["A Balrog", "A Fell Beast", "A Nazgûl", "A Warg"], "answer": "A Balrog"},
    {"prompt": "What is the name of Frodo's sword?",
     "choices": ["Narsil", "Andúril", "Glamdring", "Sting"], "answer": "Sting"}
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LOTR Quiz Game")
        self.question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12), width=30, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.next_question()

    def next_question(self):
        if self.question_index < len(questions):
            q = questions[self.question_index]
            self.question_label.config(text=q["prompt"])

            for i, choice in enumerate(q["choices"]):
                self.buttons[i].config(text=choice)
        else:
            self.show_results()

    def check_answer(self, choice_index):
        q = questions[self.question_index]
        if q["choices"][choice_index] == q["answer"]:
            self.score += 1

        self.question_index += 1
        self.next_question()

    def show_results(self):
        messagebox.showinfo("Quiz Over", f"You got {self.score} out of {len(questions)} correct!")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
