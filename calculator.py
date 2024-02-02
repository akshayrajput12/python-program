print("addition = +")
print("sunstrction = -")
print("multiplication = *")
print("division = /")

i = "yes"
while i == "yes":
  
  a = int(input("Enter a number: "))
  b = int(input("Enter a number: "))
  o = input("choose a operator: ")
  if (o == "+"):
    print(f"The value of {a} + {b} is = ", a + b)
  elif (o == "-"):
    print(f"the value of {a} - {b} is ", a - b)
  elif (o == "*"):
    print(f"the value of {a} * {b} is ", a * b)
  elif (o == "/"):
    print(f"The value of {a} / {b} is ", a / b)
  else:
    print("Choose corect operation from above")

  i = input("let do new calculation  (yes/no): ")
  
  
