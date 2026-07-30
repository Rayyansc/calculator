print("Welcome to Quantome Quiz")
print('Enter your name:')
x = input()
print('Hello, ' + x)
Correct_Answer = 0
Answer = input("Do you want to continue?  (yes/no): ")
if Answer == "yes":
    print("Great! Let's start the quiz.") #Go straight to line 10
else:
    print("Thank you for cosidering us today. We hope to see you again soon!") #Do not go to line 10
print("Question 1: What is the capital of Pakistan?")
Answer1 = input("a) Karachi\nb) Islamabad\nc) Lahore\nd) Peshawar\nYour answer:") 
if Answer1 == "b":
    Correct_Answer += 1
print("Question 2: What is the capital of Germany")
Answer2 = input("a) Berlin\nb) Munich\nc) Frankfurt\nd) Hamburg\nYour answer:")
if Answer2 == "a":
    Correct_Answer += 1
print("Question 3: who made python code?")
Answer3 = input("a) Brendan Eich\nb) James Gosling\nc) Dennis Ritchie\nd) Guido van Rossum\nYour answer:")
if Answer3 == "d":
    Correct_Answer += 1
print("Where did Guido van Rossum make python code?")
Answer4 = input("a) Netherlands\nb) United States\nc) Canada\nd) Australia\nYour answer:")
if Answer4 == "a":
    Correct_Answer += 1
print("Question 5: Who was the creator of microsoft?")
Answer5 = input("a) Jeff Bezos\nb) Steve Jobs\nc) Bill Gates\nd) Mark Zuckerberg\nYour answer:")
if Answer5 == "c":
    Correct_Answer += 1
print("Question 6: Where did Bill Gates make Microsoft?")
Answer6 = input("a) Netherlands\nb) United States\nc) Canada\nd) Australia\nYour answer:")
if Answer6 == "b":
    Correct_Answer += 1
print("Question 7: Who was the creator of Facebook?")
Answer7 = input("a) Jeff Bezos\nb) Steve Jobs\nc) Bill Gates\nd) Mark Zuckerberg\nYour answer:")
if Answer7 == "d":
    Correct_Answer += 1
print("Question 8: Where did Mark Zuckerberg make Facebook?")
Answer8 = input("a) Netherlands\nb) United States\nc) Canada\nd) Australia\nYour answer:")
if Answer8 == "b":
    Correct_Answer += 1
print("Question 9: Who was the creator of Amazon?")
Answer9 = input("a) Jeff Bezos\nb) Griff patch\nc) Bill Gates\nd) Poopy dog\nYour answer:")
if Answer9 == "a":
    Correct_Answer += 1
print("Question 10: Where did Jeff Bezos make Amazon?")
Answer10 = input("a) Netherlands\nb) Australia\nc)England\nd) United States\nYour answer:")
if Answer10 == "d":
    Correct_Answer += 1
print("Who was the creator of linkedin?")
Answer11 = input("a) Jeff Bezos\nb) Reid Hoffman\nc) Bill Gates\nd) Poopy dog\nYour answer:")
if Answer11 == "b":
    Correct_Answer += 1
print("Question 12: Who was the creator of pinterest?")
Answer12 = input("a) Ben Silbermann\nb) Reid Hoffman\nc) Pingu\nd) Poopy dog\nYour answer:")
if Answer12 == "a":
    Correct_Answer += 1