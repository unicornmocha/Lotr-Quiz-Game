questions = [
     {
        "prompt": "What is the name of the sword that was reforged into Andúril?",
        "choices": ["A) Glamdring", "B) Narsil", "C) Sting", "D) Orcrist"],
        "answer": "B"
    },
     {
        "prompt": "Who is the eldest of the Ents in *The Lord of the Rings*?",
        "choices": ["A) Quickbeam", "B) Fangorn", "C) Treebeard", "D) Skinbark"],
        "answer": "C"
    },
     {
        "prompt": "Which city is known as the White City?",
        "choices": ["A) Edoras", "B) Minas Morgul", "C) Minas Tirith", "D) Osgiliath"],
        "answer": "C"
    },
     {
        "prompt": "What is the name of Sauron's all-seeing tower?",
        "choices": ["A) Barad-dûr", "B) Orthanc", "C) Weathertop", "D) Dol Guldur"],
        "answer": "A"
    },
     {
        "prompt": "What race is Legolas?",
        "choices": ["A) Dwarf", "B) Hobbit", "C) Elf", "D) Man"],
        "answer": "C"
    },
     {
        "prompt": "What is the name of the inn where Frodo and his companions meet Aragorn?",
        "choices": ["A) The Golden Perch", "B) The Prancing Pony", "C) The Green Dragon", "D) The Silver Spoon"],
        "answer": "B"
    },
     {
        "prompt": "Who kills the Witch-King of Angmar?",
        "choices": ["A) Aragorn", "B) Eowyn", "C) Gandalf", "D) Legolas"],
        "answer": "B"
    },
     {
        "prompt": "What is the name of Gollum's original Hobbit-like self?",
        "choices": ["A) Deagol", "B) Bilbo", "C) Smeagol", "D) Frodo"],
        "answer": "C"
    },
     {
        "prompt": "Which creature does Gandalf battle on the Bridge of Khazad-dûm?",
        "choices": ["A) A Balrog", "B) A Fell Beast", "C) A Nazgûl", "D) A Warg"],
        "answer": "A"
    },
     {
        "prompt": "What is the name of Frodo's sword?",
        "choices": ["A) Narsil", "B) Andúril", "C) Glamdring", "D) Sting"],
        "answer": "D"
    }
]

def run_quiz(questions):
    score = 0
    print("Are you a real LOTR fan or just a poser??")
    for question in questions:
        print(question["prompt"])
        for choice in question["choices"]:
            print(choice)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")
    if score > 5:
        print("Heh, looks like you were a real fan after all!")
    else:
        print("Pff, I knew you were a poser!")

run_quiz(questions)

