#Quiz game

print("Welcome to my computer quiz game!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay,let's play!")

score = 0

answer = input("What's the capital of United Kingdom? ").upper()

if answer == "LONDON":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What's the captial of Spain? ").upper()

if answer == "MADRID":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Which is the biggest planet in our Solar System? ").upper()

if answer == "JUPITER":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = int(input ("How many planets are in our Solar System? "))

if answer == 9:
    print("That's correct!")
    score += 1
else :
    print("That's incorrect!")

answer = input("What RAM stands for? ").upper()
if answer == "RANDOM ACCESS MEMORY":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What CPU stands for? ").upper()
if answer =="CENTRAL PROCESSING UNIT":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the biggest manufacturer of CPUs? ").upper()
if answer == "INTEL":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What GPU stands for? ").upper()
if answer =="GRAPHIC PROCESSING UNIT":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the biggest manufacturer of GPUs ? ").upper()
if answer =="NVIDIA":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who won the european championship at football in 2021 ? ").upper()

if answer == "ITALY":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

print("Your score is " + str(score))
print("You got " + str(score/10  * 100) + "% of questions right.")