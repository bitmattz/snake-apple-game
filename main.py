import time
import random
import os

matrix = [
	[" ", " ", " ", " ", " "," ", " ", " "," "," "," "," "," "," "," "],
	[" ", " ", " ", " ", " "," ", " ", " "," "," "," "," "," "," "," "],
	[" ", " ", " ", " ", " "," ", " ", " "," "," "," "," "," "," "," "],
	[" ", " ", " ", " ", " "," ", " ", " "," "," "," "," "," "," "," "],
	[" ", " ", " ", " ", " "," ", " ", " "," "," "," "," "," "," "," "],
	[" ", " ", " ", " ", " "," ", " ", " "," "," "," "," "," "," "," "],
	[" ", " ", " ", " ", " "," ", " ", " "," "," "," "," "," "," "," "],
	[" ", " ", " ", " ", " "," ", " ", " "," "," "," "," "," "," "," "],
	[" ", " ", " ", " ", " "," ", " ", " "," "," "," "," "," "," "," "]
]

snakeLocationY = 4
snakeLocationX = 7
snakeSprint = "@"
isAlive= True

direction =""
snakeSize = 1
appleY = random.randint(0,8)
appleX = random.randint(0,14)
basketX = random.randint(0,8)
basketY = random.randint(0,14)
matrix[appleY][appleX] = "*"
matrix[basketY][basketX] = "O"
hasApple = False
delivered = False
score = 0
apples = 0
while isAlive:
	direction = input(direction)
	if snakeLocationY == appleY and snakeLocationX == appleX:
		hasApple =True
	if hasApple:
		apples = 1	

	if snakeLocationY == basketY and snakeLocationX == basketX:
		hasApple =False
		score = score + 15
		apples = 0
		delivered = True
	if delivered == True:
		appleY = random.randint(0,8)
		appleX = random.randint(0,14)
		basketY = random.randint(0,8)
		basketX = random.randint(0,14)
		matrix[appleY][appleX] = "*"
		matrix[basketY][basketX] = "O"
		delivered = False
	print(""+str(apples) +"x * | score: "+str(score))
  for i in matrix:
    previousLocationY = snakeLocationY
    previousLocationX = snakeLocationX
    if direction == "w":
      snakeLocationY = snakeLocationY - 1
    if direction == "s":
      snakeLocationY = snakeLocationY + 1
    if direction == "a":
      snakeLocationX = snakeLocationX - 1
    if direction == "d":
      snakeLocationX = snakeLocationX + 1
    direction = " "
    matrix[previousLocationY][previousLocationX] = " "
    matrix[snakeLocationY][snakeLocationX]="@"
    for j in i:
      if j!= "":
        print(j,end=" ")
      else:
        print("|", end="")
    print(" ")
else:
  quit()
