print("Welcome to Quantome Quiz")
print('Enter your name:')
x = input()
print('Hello, ' + x)
Answer = input("Do you want to continue?  (yes/no): ")
if Answer == "yes":
    print("Great! Let's start the quiz.") #Go straight to line 10
else:
    print("Thank you for cosidering us today. We hope to see you again soon!") #Do not go to line 10
print("Question 1: What is the capital of Pakistan?")
Answer1 = input("a) Islamabad\nb) Karachi\nc) Lahore\nd) Peshawar\nYour answer:") 
