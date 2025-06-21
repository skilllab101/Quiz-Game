questions = [
    "1. What is the capital of India?",
    "2. Which language is used to write Python code?",
    "3. Which number is a prime number? (2, 4, 6)",
    "4. What does CPU stand for?",
    "5. Is Python compiled or interpreted? (compiled/interpreted)",
    "6. What is 5 + 7?",
    "7. Which symbol is used for comments in Python?",
    "8. What is the output of: print(2 * 3)?",
    "9. Which data type is used for True/False values?",
    "10. What keyword is used to start a loop in Python?"
]

answers = [
    "Delhi",
    "English",
    "2",
    "Central Processing Unit",
    "interpreted",
    "12",
    "#",
    "6",
    "bool",
    "for"
]

# Start the game
score = 0
print("🧠 Welcome to the Python Basics Quiz Game!")
print("------------------------------------------\n")

# Loop through all 10 questions
for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer: ")

    # Check the answer
    if user_answer.strip().lower() == answers[i].lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {answers[i]}\n")

# Final score summary
print("🎉 Quiz Completed!")
print(f"Your Final Score: {score}/10")

#Performance Feedback
if score==10:
  print("🏆 Perfect Score")
elif score>=7:
  print("👍 Good Score")
elif score>=5:
  print("👍 Average Score")
else:
  print("👎 Fail Try Again")
