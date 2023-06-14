name = input("What is your name: ").title()
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
  answer = input("You come to a river, you can walk around it or swim accross? Type w to walk around and s to swim accross: ")
  
  if answer == "s":
    print("You swam accross and were eaten by an alligator. YOU LOST! 💀")
  elif answer == "w":
    print("You walked for many miles, ran out of water and you lost the game. 💀")
  else:
    print('Not a valid option. YOU LOST! 💀')

elif answer == "right":
  answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross / back)?")

  if answer == "back":
    print("You go back and lost.")
  elif answer == "cross":
    answer = input("You cross the bridge and meet a stranger. Do you talk to them (Y/ N)? ")
    if answer == "Y":
      print("You talk to the stranger and they gave you gold. YOU WON! 🎉")
    elif answer == "N":
      print("You ignored the stranger and they are offended, YOU LOST! 💀")
    else:
      print('Not a valid option. You Lose. 💀')

else:
  print('Not a valid option. You Lose. 💀')

print("Thank You", name, "for trying our game")