#1 print 'CORRECT' if i == 10.
value = int(input("value:"));
if(value==10):
    print("Correct");

#2 print 'CORRECT' if i == 10.
password = str(input("Enter the password:"));
if(password == "HOPE@123"):
    print("the password is correct");
else:
    print("please check the password");

#3 Catagory the people by their age like children, adult, citizen, senior citizen...
age = int(input("age:"));
if(age<18):
    print("Children")
elif(age<35):
    print("Adult");
elif(age<59):
    print("Citizen");
else:
    print("Senior Citizen");


#4  Find whether given number is positive or negative.
num = int(input("Enter any number:"));
if(num>0):
    print("No is positive");
else:
    print("No is negative");


#5 Check whether the given number is divisible by 5.
value = int(input("Enter a number to check:"));
if(value%5==0):
    print("No is divisible by 5");
else:
    print("No is not divisible by 5");
