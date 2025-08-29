import random
'''
1 for snake
-1 for water
0 for gun
'''


computer = random.choice([-1,0,1])
yourstr = input("Enter your choice : ").lower()
yourdic = {"snake":1 , "water":-1, "gun":0 }
reversedic = {1:"Snake" , -1 : "Water" , 0 : "Gun"}

you = yourdic[yourstr]

print(f"Your chose {reversedic[you]}\n Computer chose {reversedic[computer]}")

if (computer == you):
  print("Its a draw")
else:
  if(computer == -1 and you == 1):
    print("you win ! ")
  elif(computer == -1 and you == 0):
    print("You loose! ")
  elif(computer == 1 and you == -1):
    print("You lose! ")
  elif(computer == 1 and you == 0):
    print("You Win! ")
  elif(computer == 0 and you == 1):
    print("You lose! ")
  elif(computer == 0 and you == -1):
    print("You win!")
  else:
    print("Something went wrong!")
