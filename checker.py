#!/usr/bin/python3

# Define the filename of the file containing student answers
answers_file = "checkpoint-01-answers"

# Check if the answers file exists and is not empty
try:
    with open(answers_file, 'r') as f:
        if not f.read().strip():
            print(f"Error: File containing student answers '{answers_file}' is empty.")
            exit(1)
except FileNotFoundError:
    print(f"Error: File containing student answers '{answers_file}' does not exist.")
    exit(1)

# Define correct answers
correct_answers = [
    "b",
    "b",
    "c",
    "a",
    "c",
    "b"
]

# Check each question's answer
print("Checking answers...")
with open(answers_file, 'r') as f:
    for line in f:
        question, student_answer = line.strip().replace(".", "").split(" ")
        question = int(question)

        if student_answer == correct_answers[question-1]:
            print(f"{question}. Correct")
        else:
            print(f"{question}. Incorrect")

print("Checking completed.")

