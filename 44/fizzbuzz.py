max=11
num=1

while num < max:
  if num % 3 == 0:
    if num % 5 == 0:
      print("Fizz Buzz")
    else:
      print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)
  num = num+1