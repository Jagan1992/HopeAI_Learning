#1.
print("Welcome to Assignment-1");

#2.
num1 = int(input("Num1="));
num2 = int(input("Num2="));
Total = num1+num2;
print("Add:",Total);

#3 Body Mass Index.
Weight = float(input("Enter the BMI Index:"));
if(Weight<=18.5):
    print("UnderWeight");
elif(Weight<=24.9):
    print("Healthy Weight");
elif(Weight<=29.9):
    print("Overweight");
else:
    print("Very Overweight");
    