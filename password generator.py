import random

cap="ABCDEFGHIJKLMNOPQRSTUVWZYZ"


special="!@#$%^&*/|_-"


number="1234567890"


char="abcdefghijklmnopqrstuvwxyz"


passwordlength=int(input("Enter your password lenghth to generate your password: "))




caplength=int(input("How many capitals letter do you want in your password: "))

if (caplength>=passwordlength-3):
  print("Error")
  print(f"maximum value of special letter is {passwordlength-3}")

else:
  speciallenth=int(input("How many special letter word do you want in your password: "))
  if  (speciallenth>=passwordlength-2):
    print("Error")
    print(f"maximum value of special letter is  {passwordlength-2}")

  else:
    numberlenth=int(input("How many numbers word do you want in your password: "))
    if (caplength<=0) :
       print("Please select atleast 1 in caplength to generate your password")
    elif (speciallenth<=0):
      print("please select atleast 1 in speciallength to generate your password")


    elif (numberlenth<=0) :
      print("please select atleast 1 in numberlength to generate your password")

  
    elif (caplength<=0) and (numberlenth<=0) and (speciallenth<=0) :
      print("Please Select atleast 1 in caplength,numberlength and specialletterlength to generate your password")




    else:
      passwordlength_final=passwordlength-(caplength+speciallenth+numberlenth)
      pass1=""
      pass2=""
      pass3=""
      for i in range(caplength):
       pass1=pass1+random.choice(cap)
        
      for i in range(speciallenth):
        pass2=pass2+random.choice(special)
    
    
      for i in range(numberlenth):
        pass3=pass3+random.choice(number)
    
      password=pass1+pass2+pass3
      for i in range(passwordlength_final):
        password=password+random.choice(char)
      print("Your generated password is :",password)












  




