#1.Write logic to ask the user for their age and determine if they are eligible to vote based on whether they are 18 or older.
age = int(input("Enter your age:"));

def CheckAgeLimit():
    if(age>=18):
        print("you are eligible for voting");
    else:
        print("you are not eligible for voting");

CheckAgeLimit();

#2.Write logic to identify and return the largest number from a given list.

lst = [22,33,44,55,66,77,88];
print(max(lst));

#3.Write logic to determine the bonus amount based on the given salary.

salary = int(input("Enter your salary:"));

def CalPercentage():
    if(salary>50000):      
        bonus = (salary/100)*10;
        print("you are eligible for the bonus amount:",bonus,"based on the given salary:",salary);
    else:
       print("you are not eligible for the bonus amount because your salary is less than $50,000");

CalPercentage();

#4.Write logic to check whether a given number is even or odd.

number =  int(input("Ener your number:"));

def OddorEven():
    if(number%2==0):
        print("The number is even");
    else:
        print("The number is odd");

OddorEven();

#5.Write logic to take a word or sentence as input and produce its reversed version.

Word = input("Enter your word:");

def ReversalOfWord():
    str="";
    for i in Word:
        str = i+str;
    print(str);
        

ReversalOfWord();

#6. Write logic to check if a student has passed a subject by scoring at least 40 marks.

Score = int(input("Enter your Score:"));

def CheckScore():
    if(Score>=40):
        print("You are Passed");
    else:
        print("You are not Passed");

CheckScore();

#7. Write logic to calculate the final amount to be paid after applying the discount.

amount = int(input("Enter your amount:"));

def CalculateTotalAmount():
    if(amount>100):
        discount = (amount/100)*20;
        totalAmount = amount - discount;
        print("the final amount to be paid after 20% discount:",totalAmount);
    else:
        print("the total amount - ",amount, "does not exceeds $100 so you are not eligible for discount.");

    
CalculateTotalAmount();

#8. Write logic to check if a user has enough balance before allowing a withdrawal and update the remaining balance accordingly

wihdrawalAmount = int(input("Enter your WithDrawal Amount:"));

def CalWithDrawalAmount():
    if(wihdrawalAmount>0):
        remainingBalance = 1000 - wihdrawalAmount;
        print("the remainingbalance after withdrawal : ",remainingBalance);
    else:
        print("your are not having eligible balance for withdrawal");

CalWithDrawalAmount();

#9. Write logic to determine whether a given year is a leap year.

Year = int(input("Enter the year:"));

def CheckLeapYear():
    if((Year%4 == 0 and Year%100 != 0) or (Year % 400 == 0)):
        print(Year,"is a leap year");
    else:
        print(Year,"it's not a leap year");

CheckLeapYear();


#10. Write logic to extract and return only the even numbers from a list.

lst = [1,2,3,4,5,6,7,8,9,10];

def ExtractEvenNumbers():
    number = "";
    for i in lst:
        if(i%2==0):
            number += str(i) + " ";
    print(number);

ExtractEvenNumbers();


         
            

