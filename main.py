number = int(input("Which number do you want to check? "))

if (number % 2) == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

if (number % 4) == 0:
  print(f"{number} is cleanly divisible by 4.")
else: 
  print(f"{number} is not cleanly divisible by 4.")
