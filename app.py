import pandas as pd
import statsmodels.api as sm
import streamlit as st

# Load data
jeera_data = pd.read_excel("JeeraPrice2020.xlsx")
weather_data = pd.read_excel("GujratTempHumiditySpeed.xlsx")

# Merge datasets
merged_data = pd.merge(jeera_data, weather_data, on="Date", how="inner")

# Preprocess data if needed
# Ensure that columns used for regression are numeric
numeric_columns = ['Temperature', 'Dew Point', 'Humidity', 'Wind Speed', 'Price']

# Convert relevant columns to numeric, coercing errors to NaN
merged_data[numeric_columns] = merged_data[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Drop rows with missing values
merged_data = merged_data.dropna()

# Add a constant column to the independent variables
X = sm.add_constant(merged_data[['Temperature', 'Dew Point', 'Humidity', 'Wind Speed']])
y = merged_data['Price']

# Ensure that the dependent variable is numeric
y = pd.to_numeric(y, errors='coerce')
y = y.dropna()

# Build the model
model = sm.OLS(y, X).fit()

# Streamlit App
st.title("Jeera Price Analysis")

# Display summary statistics
st.write("Summary Statistics:")
st.write(model.summary())

# Display scatter plots or any other visualizations

# Interpret coefficients
st.write("Interpretation of Coefficients:")
st.write("Temperature Coefficient:", model.params['Temperature'])
st.write("Dew Point Coefficient:", model.params['Dew Point'])
st.write("Humidity Coefficient:", model.params['Humidity'])
st.write("Wind Speed Coefficient:", model.params['Wind Speed'])

# Add more Streamlit components and visualizations as needed
