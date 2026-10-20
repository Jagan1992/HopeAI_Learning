import pandas as pd;
from sklearn.model_selection import train_test_split;
#refer https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html in google search.
from sklearn.tree import DecisionTreeRegressor;
import matplotlib.pyplot as plot;
from sklearn import tree;
from sklearn.metrics import r2_score;


dataset = pd.read_csv("Week3-Machine-Learning-Regression/Decision Tree/50_Startups.csv");

#it contains some categorical data we need to use nominal data for one hot encoding for multiple column expansion.
#dataset = pd.get_dummies(dataset).astype(int);
dataset = pd.get_dummies(dataset,drop_first=True).astype(int);

#extracting the input values from dataset.
independent = dataset[["R&D Spend","Administration","Marketing Spend","State_Florida","State_New York"]];

#extracting the output values from dataset.
dependent = dataset[["Profit"]];

#Output.
x_train,x_test,y_train,y_test = train_test_split(independent,dependent,test_size=0.30,random_state=10);

#import Decision Tree algorithm.
regressor = DecisionTreeRegressor(criterion='poisson',splitter="best",random_state=10);
regressor.fit(x_train,y_train);

#import plot.
tree.plot_tree(regressor);
plot.show();

#Prediction.
y_pred = regressor.predict(x_test);

#R_Score.
r_score = r2_score(y_test,y_pred);

print(r_score);







