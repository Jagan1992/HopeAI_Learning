import pandas as pd;
import pickle;
from sklearn.model_selection import train_test_split;
#refer sklearn.linear_model.LinearRegression documentation in google search.
from sklearn.linear_model import LinearRegression;
from sklearn.metrics import r2_score;

#reading
dataset = pd.read_csv("Week3-Machine-Learning-Regression/Multiple Linear Regression/50_Startups.csv");

#it contains some categorical data we need to use nominal data for one hot encoding for multiple column expansion.
#dataset = pd.get_dummies(dataset).astype(int);
dataset = pd.get_dummies(dataset,drop_first=True).astype(int);

#extracting the input values from dataset.
independent = dataset[["R&D Spend","Administration","Marketing Spend","State_Florida","State_New York"]];

#extracting the output values from dataset.
dependent = dataset[["Profit"]];

#Output.
x_train,x_test,y_train,y_test = train_test_split(independent,dependent,test_size=0.30,random_state=0);

regressor = LinearRegression();

regressor.fit(x_train,y_train);

#weight.
weight = regressor.coef_;

#bias.
bias = regressor.intercept_;

#Prediction.
y_pred = regressor.predict(x_test);

#R_Score.
r_score = r2_score(y_test,y_pred);

print(r_score);

#Save Model.
filename = "Week3-Machine-Learning-Regression/Multiple Linear Regression/finalised_model_multiple_linear.sav";

#save model as file.
pickle.dump(regressor,open(filename,'wb'));

#load model for testing.
load_model = pickle.load(open(filename,'rb'));

result = load_model.predict([[153441.51,101145.55,407934.54,1,0]]);

print(result);








