#1. Write logic to determine whether the amount is positive, negative, or zero

amount = int(input("Enter the amount:"));

def CheckAmount():
    if(amount==0):
        print("Amount entered is Zero");
    elif(amount<0):
        print("Amount entered is negative");
    elif(amount>0):
        print("Amount entered is positive");

CheckAmount();

#2. Write logic to compute the sum of the digits of a given number.

passcode = int(input("Enter the Passcode:"));

def CalPassCode():
    calsum=0;
    if(passcode<0):
        print("Passcode should be greater than zero");
    else:
        result = [int(digit) for digit in str(passcode)];
        for i in result:
            calsum+=i;
        print(calsum);

CalPassCode();

#3.  Write logic to take a number and return its reverse.

number = int(input("Enter the number:"));

def CalReverse():
    revstr= "";
    if(number<0):
        print("number should be greater than zero");
    else:
        result = [int(digit) for digit in str(number)];
        result.reverse()
        for i in result:
           revstr+=str(i)
        print(revstr);

CalReverse();

#4. Write logic to check if a given number is prime.
num1 = int(input("Enter the number:"));

def PrimeNumber():
    PrimeNoflag = False;
    if(num1 == 0 or num1 == 1):
        PrimeNoflag = True;
    for i in range(2,num1):
        if(num1%i==0):
            PrimeNoflag = True;
    if(PrimeNoflag):
        print(num1,"is not a prime number");
    else:
        print(num1,"is a prime number");
    
PrimeNumber();

#5. Write logic to find the factorial of a given number using recursion.

factorialNumber = int(input("Enter the factorial of the number:"));

def CalFactorialNumber():
     calfac=1;
     result = [int(digit) for digit in str(factorialNumber)];
     if(factorialNumber<0):
         print("The number should not be less than zero or equal to zero");
     else:
        for i in result:
         calfac*=i;
        print(calfac);

    
CalFactorialNumber();

#6.  Write logic to check whether a given number is an Armstrong number.

armstrongNumber = int(input("Enter the number:"));

def CalArmStrongNumber():
    numberlen = len(str(armstrongNumber));
    arm_num = 0;
    n = armstrongNumber;
    while(n>0):
        m = n%10;
        arm_num += m**numberlen;
        n //= 10;
    return arm_num == armstrongNumber;

CalArmStrongNumber();

if(CalArmStrongNumber()):
    print(f"{armstrongNumber} is a Armstrong number");
else:
    print(f"{armstrongNumber} is not a Armstrong number");

#7. Write logic to perform swapping the first and last characters of user-generated passwords. this operation on a given string.

password = input("Enter the password:")

def PasswordManager():
    if(len(password)<=-1):
        print("Password cannot be null");
    
    result = password[-1] + password[1:-1] + password[0];

    print(result);


PasswordManager();


#8. Write logic to convert a given decimal number into its binary equivalent

def dectobin():
    decNumber = float(input("Enter the Decimal Number:"));
    binary_digits=[];
    if(decNumber==0):
        print("the decimal no cannot be zero");
    else:
        while(decNumber>0):
            rem = decNumber%2;
            binary_digits.append(str(rem));
            decNumber = decNumber // 2;
        return "".join(binary_digits[::1]);

bin_number = dectobin();

print(bin_number);

#9 Write logic to find the longest word in a sentence.

word = str(input("Enter the sentence:"));

def findlongword():
    if(len(word)==0):
        print("Enter the word");
    else:
        splitword = word.split();
        longest_word = max(splitword,key=len);
        print("the lonngest word in the sentence is :",longest_word);


findlongword();


#10. Write logic to check whether two given strings are anagrams.

FirstString = str(input("Enter the string one:"));

SecondString = str(input("Enter the string two:"));

def CheckAnagrams():
   if(sorted(FirstString.lower()) == sorted(SecondString.lower())):
       print("the given two string are anagrams");
   else:
       print("the given two strings are not anagrams");

CheckAnagrams();









