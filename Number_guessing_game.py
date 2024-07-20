import random
top_range=input("Type a number: ")
if top_range.isdigit():
    top_range=int(top_range)
    if top_range<=0:
        print("Please enter a number larger than zero next time")
        quit()
else:
    print("Please type a digit next time")
    quit()
guesses=0
rno=random.randint(0,top_range)
while True:
    guesses+=1
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
     user_guess=int(user_guess)
    else:
      print("Please type a digit next time")
      continue
    if user_guess==rno:
       print("Correct!")
       break
    elif user_guess>rno:
         print("You were above the number!")
    else:
          print("You were below the number!")
print("You got it in",guesses,"guesses")