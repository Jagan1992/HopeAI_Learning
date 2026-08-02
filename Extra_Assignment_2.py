#1 print 0 to 20 by using range.
num1 = range(0,20);
print("# print 0 to 20 by using range");
for num in num1:
    print(num);

#2 print range 10 to 20.
num2 = range(10,20);
print("# print range 10 to 20");
for num in num2:
    print(num);

#3 Print number of items in the list by using 'len'.
lst = [10, 20, 14, 55, 43, 87, 76]
print("Number of item in the List:",len(lst));

#4.
word = "Artificial Intelligence";
print(word);
strlen= len(word);
for i in range(0,len(word)):
    print(word[i]);

#5.
Name = str(input("Enter your Name:"));
Age = str(input("Enter your Age:"));
Pro = str(input("Enter your Proffession:"));

#6.
tuple = (1,'Wlecome',2,'Hope');
print(tuple);


#7.
tuple1 = ((0,1,2,3),('python','HOPE'));
print(tuple1);

#8 print Odd Numbers in the list.
oddlst = (20,10,16,19,25,1,276,188);
for num in oddlst:
    if(num%2==1):
        print(num,"is odd");

#10 print Even numbers in the list.
evenlst = (20,10,16,19,25,1,276,188);
for num in evenlst:
    if(num%2==0):
        print(num,"is even");



