
Fields = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing'];

#1.SubFields
def SubFields() :
    print("Sub-Fields in AI are:")
    for Field in Fields:
        print(Field);

SubFields();

#2.OddEven
number = int(input("Enter your Number:"));
def OddEven():
    if(number%2==0):
        print(number ,"is Even Number");
    else:
        print(number ,"is Odd Number");

OddEven();

#3.ElegiblityForMarriage
Gender = str(input("Your Gender:"));
Age = int(input("Your Age:"));

def ElegiblityForMarriage():
    if(Age<=20):
        print("Not Eligible");
    else:
        print("Eligible");

ElegiblityForMarriage();

#4 Percentage.
lstPercentage = [98,87,95,95,93];

def Percentage():
    i=0;
    total=0;
    for percent in lstPercentage:
        i+=1;
        print("Subject",i,"=",percent);
        total+=percent;
    print("Total:",total);
    print("Percentage: ",total/len(lstPercentage));

Percentage();

#5 Triangle.
def Triangle():
    height = int(input("Height:"));
    breadth = int(input("Breadth:"));
    print("Area of Triangle:",height*breadth/2);
    height1 = int(input("Height1:"));
    height2 = int(input("Height2:"));
    breadth1 = int(input("Breadth:"));
    print("Perimeter Triangle:",height1+height2+breadth1);

Triangle();

