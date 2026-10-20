import pickle;

filename = "Week3-Machine-Learning-Regression/finalised_model_linear.sav";

load_model = pickle.load(open(filename,'rb'));

result = load_model.predict([[12]]);

print(result);