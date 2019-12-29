from two import question
question_prompt = ["What's the Brazil's capital?\n(a) Brasília\n(b) Buenos Aires\n(c) Washington\n", "What's the Argentina's capital?\n(a) Brasília\n(b) Buenos Aires\n(c) Washington\n", "What's the USA's capital?\n(a) Brasília\n(b) Buenos Aires\n(c) Washington\n"]

questions = [
    question(question_prompt[0], "a"),
    question(question_prompt[1], "b"),
    question(question_prompt[2], "c")
]

def function(questions):
    scr = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            scr += 1
    print("You got", scr, "/", len(questions))
    k = input("Press ENTER to exit...")
function(questions)