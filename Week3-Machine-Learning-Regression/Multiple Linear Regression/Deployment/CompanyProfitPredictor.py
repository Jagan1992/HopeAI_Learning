import pickle;

filename = "Week3-Machine-Learning-Regression/Multiple Linear Regression/finalised_model_multiple_linear.sav"

load_model = pickle.load(open(filename,'rb'));

result = load_model.predict([[150000,50000,500000,1,0]]);

print(result);