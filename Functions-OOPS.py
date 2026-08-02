
#1 Function without using return statement.
lst = [23,45,67,34,89];

def AgeCategory():
    for age in lst:
         if(age<18):
              print("Children");
         elif(age<35):
              print("Adult");
         elif(age<59):
              print("Citizen");
         else:
              print("Senior Citizen");

AgeCategory();

#2 Function with using return statement.
def AgeCategoryWithReturn():
     if(ageinput<18):
          cat="Children";
     elif(ageinput<35):
          cat="Adult";
     elif(ageinput<59):
          cat="Citizen";
     else:
          cat="Senior Citizen";
     return cat;

ageinput = int(input("Enter your age:"));
category = AgeCategoryWithReturn();
print(category);

number = int(input("Enter your number:"));

def OddorEven(number):
     if(number%2==1):
          message = "The number is odd";
     else:
          message = "the number is even";
     return message;

result = OddorEven(number);
print(result);

def BMI():
     Weight = int(input("Enter the BMI Index:"));
     if(Weight<=18.5):
          WeightStatus = "UnderWeight";
     elif(Weight<=24.9):
          WeightStatus = "Healthy Weight";
     elif(Weight<=29.9):
          WeightStatus = "Overweight";
     else:
          WeightStatus = "Very Overweight";
     return WeightStatus;

GetBMI = BMI();
print(GetBMI);

num1 = int(input("Enter your Num1:"));
num2 = int(input("Enter your Num2:"));

def addition(num1,num2):
     add = num1+num2;
     return add;

print(addition(num1,num2));

def subtract(num1,num2):
     sub = num1-num2;
     return sub;

print(subtract(10,3));