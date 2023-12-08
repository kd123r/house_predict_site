import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import pickle

filename = 'housing_price_dataset.csv'
data = pd.read_csv(filename)
# Create target object and call it y
y = data.Price
# Create X
features = ['SquareFeet', 'Bedrooms', 'Bathrooms', 'Neighborhood']
X = data[features]

# one-hot encoding
X = pd.get_dummies(X)

model = DecisionTreeRegressor(max_leaf_nodes=25, random_state=1)
model.fit(X.values, y.values)

# Save the model as a pkl file
output_filename = 'house_predict_model.pkl'
pickle.dump(model, open(output_filename, 'wb'))