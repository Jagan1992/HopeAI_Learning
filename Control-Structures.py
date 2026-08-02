# if statement.
age = int(input("Enter your age:"));
if(age==18):
    print("Adult");

# if-else statement.
num1 = int(input("Enter your age:"));
if(num1<18):
    print("Children");
else:
    print("Adult");


#if-elif statement.
num2=int(input("Enter you age:"));
if(num2<18):
    print("Children");
elif(num2<35):
    print("Adult");
elif(num2<59):
    print("Citizen");
else:
    print("Senior Citizen");

# for loop.
lst = [17,23,45,23,89];
for age in lst:
    if(age<18):
        print("Children");
    elif(age<35):
        print("Adult");
    elif(age<59):
        print("Citizen");
    else:
        print("Senior Citizen");

# odd or even.
num = int(input("Enter your number:"));
if(num%2==1):
    print("Odd Number");
else:
    print("Even Number");

# range.
num3 = range(0,10);
for num in num3:
    print(num);

# range with increment.
num4 = range(21,40,3);
for num in num4:
    print(num);
