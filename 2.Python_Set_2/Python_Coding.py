
#1.Write a Python program to find the reverse of a string. Expected Output (for input "hello"):

revstr = str(input("Enter the string:"));

def reverseString():
    if(len(revstr)==0):
        print("String cannot be empty or null");
        return;
    else:
        str1 = list(revstr);
        str1.reverse();
        strRev="";
        for i in str1:
            strRev+=i;
        return strRev;
                
strRevers = reverseString();

print(strRevers);

#2.Write a Python program to generate the Fibonacci sequence up to 10 terms.

print("\n");

def fibseries():
    n=10;
    a,b=0,1;
    for _ in range(n):
        print(a,end=" ");
        a,b=b,a+b;

fibseries();

#3. Write a Python function to check if a given string is a palindrome.

print("\n")

palindrome = str(input("Enter the string:"));

def CheckPalidrome():
    revPalindrome = "";
    if(len(revstr)==0):
        print("String cannot be empty or null");
        return;
    else:
        lstPalindrome = list(palindrome);
        lstPalindrome.reverse();
        for i in lstPalindrome:
            revPalindrome+=i;
    if(revPalindrome==palindrome):
        print(f"the given string {palindrome} is a palindrome");
    else:
        print(f"the given string {palindrome} is not a palindrome");


CheckPalidrome();


#4.Write a Python program to count the number of vowels in a given string.
print("\n");

vowelstring = str(input("Enter the string:"));

def CalVowelInString():
    vowCount=0;
    if(len(revstr)==0):
        print("String cannot be empty or null");
        return;
    else:
        lst = ['a','e','i','o','u'];
        vowlst = list(vowelstring);
       
        for i in vowlst:
            if i in lst:
                vowCount+=1;
    print("Number of vowels:",vowCount);

CalVowelInString();


#5.Write a Python program to remove duplicates from a list.

print("\n");

def removeDuplicates():
    lst = [1, 2, 2, 3, 4, 4, 5];
    duplst = list(set(lst));
    print(duplst);

removeDuplicates();



