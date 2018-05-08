num = 0 
maxNum = -1
print("I shall take in a bunch of positive ints, and I will print the largest number, when you want me to stop please type -1")
while True:
  num = int(input())
  if num > maxNum:
    maxNum = num
  if num == -1:
    break
if num > -1:
  print(maxNum)
else:
  print("you have not entered any data")

