quiz = [["A. lois", "B. ires", "C. Diana", "D. suprema"], ["A. Superman", "B. Joker", "C. Penguin", "D. Riddler"],
        ["A. Stan Lee", "B. Micheal Bay", "C. zack Snyder", "D. spidy"]]

question = ["What was Wonder Woman originally named?",
            "Which super villain was once the Iranian Ambassador to the U.N.?",
            "Question: Which Marvel writer worked for DC Comics?"]

try:
    i = 0
    human_answer = ""
    while i < 3:
        print(str(i + 1) + " " + question[0])

        for quizzing in quiz[i]:
            print(quizzing)

        answer = input("===>").upper()

        if i == 0:

            if answer == "D":
                human_answer += "D"
        if i == 1:

            if answer == "B":
                human_answer += "B"
        if i == 2:
            if answer == "A":
                human_answer += "A"
        if answer != "A" and answer != "B" and answer != "C" and 'D' != answer:
            i = -1
            print("restarting...")
            print("can only show A B C D")
            human_answer=""
        i += 1
        print(i)
    print(f"your Answer: {human_answer}")
    print("Correct Answers DBA")
    print(f"Percentage: {(len(human_answer) / 3) * 100} %")

except ValueError as e:
    print(e)


