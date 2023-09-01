from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('cars.csv')  # Replace 'car_data.csv' with your dataset file

# Select relevant features for the model
features = ['name', 'company', 'year', 'kms_driven', 'fuel_type']

# Create the feature matrix X and the target variable y
X = data[features]
y = data['Price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing steps
# Categorical features
categorical_features = ['name', 'company', 'year','kms_driven', 'fuel_type']
categorical_transformer = OneHotEncoder()

# Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features)])

# Linear regression model
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', LinearRegression())])

# Train the linear regression model
model.fit(X_train, y_train)

# Make predictions on new data
def predict_car_value(name, company,  year, kms_driven, fuel_type):
    # Create a new dataframe with the input values
    input_data = pd.DataFrame([[name, company, year, kms_driven, fuel_type]], columns=features)

    # Make the prediction
    predicted_price = model.predict(input_data)
    

    predicted_price = round(predicted_price[0], 2)

    return predicted_price

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        company = request.form['company']
        year = int(request.form['year'])
        kms_driven = int(request.form['kms_driven'])
        fuel_type = request.form['fuel_type']

        predicted_value = predict_car_value(name, company, year, kms_driven, fuel_type)
        return render_template('index.html', predicted_value=predicted_value)
    
    # Create a list of years from 2000 to 2020
    year_range = list(range(2000, 2021))

    return render_template('index.html', year_range=year_range)


if __name__ == '__main__':
    app.run(debug=True)


