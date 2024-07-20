name=input("Type your name:")
print("welcome",name,"to this adventure!")
answer=input("You are on a dirt road,it has come to an end and you can go left or right. which way would you like to go? ").lower()
if answer=="left":
  answer=input("You come to a river,you can walk around it or swim across. Type walk to walk around or swim to swim across").lower()
  if answer=="swim":
     print("You swam across and were eaten by an alligator")  
  elif answer=="walk":
     print("You walked for many miles,ran out of water and lost the game")
  else:
    print("Not a valid option. You lose!")     
elif answer=="right":
  answer=input("You come to a bridge it looks woobly,do you want to cross it or head back(cross/back)? ").lower()
  if answer=="back":
     print("You go back and lose")  
  elif answer=="cross":
     answer=input("You cross the bridge and meet a stranger. Do you want to talk to them?(Yes/No) ").lower()
     if answer=="yes":
        print("You Won!")
     elif answer=="no":
        print("You were close to winning!")
     else:
       print("Not a valid option. You lose!") 
else:
 print("Not a valid option. You lose!")
print("Thank You for trying",name)