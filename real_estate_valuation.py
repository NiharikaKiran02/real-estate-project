import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('real_estate_data.csv')

# Preprocessing
# Strip extra spaces in column names
data.columns = data.columns.str.strip()

# Handle missing values if any
data = data.dropna()  # Drop rows with missing values

# Handling categorical variables (e.g., 'Crime Rate', 'Demand-Supply Dynamics', 'Seasonality')
# Convert categorical columns to dummy variables (one-hot encoding)
data = pd.get_dummies(data, columns=['Crime Rate', 'Demand-Supply Dynamics', 'Seasonality'], drop_first=True)

# Define features and target
X = data.drop(columns=['Sale Price', 'Sale Date', 'ZIP Code'])  # Features (exclude Sale Price, Sale Date, and ZIP)
y = data['Sale Price']  # Target variable (Sale Price)

# Train-test split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
# Verify the split sizes
print(f"Training set size: {len(X_train)}, Test set size: {len(X_test)}")

# Check if target values in test set are unique
print("Unique values in the test set's target variable (Sale Price):")
print(y_test.unique())
# Model Training with Random Forest Regressor
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Feature Importance (optional visualization)
importance = model.feature_importances_
feature_names = X.columns

# Plot feature importance
plt.barh(feature_names, importance)
plt.xlabel("Feature Importance")
plt.title("Feature Importance in Property Valuation")
plt.show()
