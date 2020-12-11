n = int(input())
while len(str(n)) < 3:
    n = str(n)+"0"
num1 = 

for i in range(3):
  if num1 <= num2 and num2 <= num3:
    max = num3
    mid = num2
    min = num1
  elif num1 <= num3 and num3 <= num2:
    max = num2
    mid = num3
    min = num1
  elif num2 <= num3 and num3 <= num1:
    max = num1
    mid = num3
    min = num2
  elif num2 <= num1 and num1 <= num3:
    max = num3
    mid = num1
    min = num2
  elif num3 <= num1 and num1 <= num2:
    max = num2
    mid = num1
    min = num3
  else:
    max = num1
    mid = num2
    min = num3
  num_max = max*100 + mid*10 + min
  num_min = min*100 + mid*10 + max
  h = str(num_max - num_min)
  if i != 2:
    print(h, end=",")
  else:
    print(num_max - num_min)
