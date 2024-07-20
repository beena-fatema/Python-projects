print("Welcome to my computer quiz!")
playing=input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay!Let's play :)")
score=0
answer=input("What does CPU stands for? ")
if answer.lower() =="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer=input("What does GPU stands for? ")
if answer.lower() =="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
print(f"You got {score} questions correct")
print(f"You got {(score/2)*100}%.")

