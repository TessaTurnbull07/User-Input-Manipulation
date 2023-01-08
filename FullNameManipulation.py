#takes user input and splits it apart
fullName = input().split()

#if the user gives three names
#[0] is for initials only
if len(fullName) == 3:
  firstName, middleName, lastName = fullName
  print(f"{lastName}, {firstName[0]}.{middleName[0]}.")
  
#if the user gives 2 names
elif len(fullName) == 2:
  firstName, lastName = fullName
  print(f"{lastName}, {firstName[0]}.")
  
#if the user gives a different amount of names
else:
  print("Valid name not entered.")
