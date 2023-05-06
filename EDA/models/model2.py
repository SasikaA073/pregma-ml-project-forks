import numpy as np
import pandas as pd

data = pd.read_csv('dataset.csv')

x = data.drop(['RiskLevel'], axis=1)

Y = data['RiskLevel']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, Y, test_size=0.3, random_state=0)

# Decision Tree Classifier
# from sklearn.tree import DecisionTreeClassifier

# model = DecisionTreeClassifier()

# Decision Tree Regressor
# from sklearn.tree import DecisionTreeRegressor

# model = DecisionTreeRegressor()

# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

# Train the model
model.fit(x_train, y_train)

# Predict the model
model.predict(x_test)

# Accuracy of the model
from sklearn.metrics import accuracy_score

accuracy_score(y_test, model.predict(x_test))

print("Accuracy of Decision Tree Classifier is: ", accuracy_score(y_test, model.predict(x_test)))

# Confusion Matrix
from sklearn.metrics import confusion_matrix

print("Confusion Matrix of Decision Tree Classifier is: ", confusion_matrix(y_test, model.predict(x_test)))