# python quiz game

questions = (("Who created Python ? : "),
           ("What is the correct file extension for Python files ? : " ),
           ("Which data type is used to store multiple items in a single variable in Python ? : "),
           ("Which of the following data types is immutable in Python ? : "),
           ( "Which keyword is used to define a function in Python ? :"))

options  = (("A.James Gosling ", "b.Dennis Ritchie ", "C.Guido van Rossum ", "D.Bjarne Stroustrup "),
           ("A. .pt ", "b. .python ", "C. .py ", "D. .pyt "),
           ("A.int ", "b.list ", "C.float ", "D. bool "),
           ("A.List ", "b.Dictionary ", "C.Set ", "D.Tuple "),
           ("A.function ", "b.define ", "C.def ", "D.func "))

answers = ("C", "C", "B", "D", "C" )
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    
    guess = input("Enter (A, B, C, D ) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT ! ")
    else:
        print("INCORRECT ! ")
        print(f"{answers[question_num]} is the correct answer. ")
    question_num += 1


print("------------------")
print("      RESULTS     ")
print("------------------")

print("answers: " , end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: " , end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions)* 100)
print(f"Your score is {score}%")