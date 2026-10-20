import pandas as pd;
import pickle;
from sklearn.model_selection import train_test_split;
#refer sklearn.linear_model.LinearRegression documentation in google search.
from sklearn.linear_model import LinearRegression;
from sklearn.metrics import r2_score;


#reading the values.
salarydataset = pd.read_csv("Week3-Machine-Learning-Regression/Single Linear Regression/Salary_Data.csv");

#parsing the values for YearsExperience.
Years_Of_Experience_input = salarydataset[["YearsExperience"]];

#parsing the values for Salary.
Salary_input = salarydataset[["Salary"]];

#output.
x_train,x_test,y_train,y_test = train_test_split(Years_Of_Experience_input,Salary_input,test_size=0.30,random_state=0);

regressor = LinearRegression();

regressor.fit(x_train,y_train);

#Weight.
weight = regressor.coef_;

#bias.
bias = regressor.intercept_;

#Prediction.
y_pred = regressor.predict(x_test);

#R_Score.
r_score = r2_score(y_test,y_pred);

print(r_score);

#Save Model.
filename = "Week3-Machine-Learning-Regression/Single Linear Regression/finalised_model_linear.sav";

#save model as file.
pickle.dump(regressor,open(filename,'wb'));

#load model for testing.
load_model = pickle.load(open(filename,'rb'));

result = load_model.predict([[15]]);

print(result);




