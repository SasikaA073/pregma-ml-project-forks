# Code used to load data
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
pregma_file_path = 'dataset.csv'

# Fill in the line below to read the file into a variable home_data
pregma_data = pd.read_csv(pregma_file_path)

y = pregma_data.RiskLevel

# Create the list of features below
feature_names = ['Age', 'SystolicBP', 'DiastolicBP', 'BS', 'BodyTemp', 'HeartRate', 'RiskLevel']

# Select data corresponding to features in feature_names
X = pregma_data[feature_names]
 
# Import the train_test_split function and uncomment
from sklearn.model_selection import train_test_split

# fill in and uncomment
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify the model
pregma_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data.
pregma_model.fit(train_X, train_y)

# Predict with all validation observations
val_predictions = pregma_model.predict(val_X)

# print the top few validation predictions
print(pregma_model.predict(val_X))
# print the top few actual prices from validation data
print(pregma_model.predict(val_y))

from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(val_predictions, val_y)

# uncomment following line to see the validation_mae
print(val_mae)