#1. Write a Python program that prints numbers from 1 to 5.

def PrintNumber():
    for i in range(1,6,1):
        print(i);

PrintNumber();

#2. Write a Python program to print the first 5 even numbers. Expected Output:

def PrintEvenNumbers():
    print("\n");
    for i in range(1,11,1):
        if(i%2==0):
            print(i," ");

PrintEvenNumbers();

#3.Write a Python program to print the sum of numbers from 1 to 10.

def PrintTotalSumofNumbers():
    print("\n");
    totalSum = 0;  
    for i in range(1,11,1):
        totalSum+=i;
    print(totalSum);

PrintTotalSumofNumbers();

#4. Write a Python function to find the factorial of 5.

def FactorialofNumber():
    print("\n");
    factorial=1;
    for i in range(1,6,1):
        factorial*=i;
    print(factorial);

FactorialofNumber();


#5. Write a Python program to check if a number is prime.

print("\n");

number = int(input("Enter your number:"));

def PrimeNumber():
    PrimeNoflag = False;
    if(number == 0 or number == 1):
        PrimeNoflag = True;
    for i in range(2,number):
        if(number%i==0):
            PrimeNoflag = True;
    if(PrimeNoflag):
        print(number,"is not a prime number");
    else:
        print(number,"is a prime number");
    
PrimeNumber();



