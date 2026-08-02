class Calculator:

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

    def OddorEven(number):
     if(number%2==1):
          message = "The number is odd";
     else:
          message = "the number is even";
     return message;

#BMIIndex = Calculator.BMI();
#print(BMIIndex);

#CheckOddOEven = Calculator.OddorEven(23);
#print(CheckOddOEven);
