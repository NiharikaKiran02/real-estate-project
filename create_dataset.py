import pandas as pd

# Create the dataset manually with more entries
data = {
    'ZIP Code': ['90210', '10001', '30301', '60614', '98101', '30303', '94110', '75201', '33139', '02139'],
    'Square Footage': [2500, 1500, 3200, 1800, 2700, 1500, 2200, 3000, 1800, 2200],
    'Number of Bedrooms': [4, 3, 5, 2, 4, 3, 3, 4, 2, 3],
    'Number of Bathrooms': [3, 2, 4, 2, 3, 2, 2, 3, 2, 3],
    'Floors': [2, 1, 2, 1, 2, 1, 2, 2, 1, 2],
    'Age of Property': [10, 20, 5, 15, 8, 30, 25, 12, 18, 6],
    'Population Density': [1200, 8000, 3000, 5000, 4000, 4500, 6700, 1500, 3500, 3800],
    'Household Income': [120000, 95000, 105000, 85000, 115000, 125000, 95000, 110000, 80000, 115000],
    'Average Age': [35, 40, 37, 42, 36, 45, 41, 39, 38, 34],
    'Proximity to Amenities': [1.2, 0.8, 1.5, 0.9, 1.1, 0.6, 1.3, 0.7, 1.0, 1.2],  # Distance in km
    'Crime Rate': ['Low', 'Moderate', 'Low', 'High', 'Moderate', 'Low', 'Moderate', 'Low', 'High', 'Low'],
    'Recent Sales Trend': [5, 3, 4, 2, 6, 4, 3, 5, 4, 6],  # Scale 1-10
    'Property Appreciation Rate': [2.5, 1.8, 3.2, 2.1, 2.7, 1.9, 2.4, 3.1, 2.0, 2.6],  # % per year
    'Demand-Supply Dynamics': ['High Demand', 'Balanced', 'High Demand', 'Low Demand', 'Balanced', 'High Demand', 'Low Demand', 'Balanced', 'High Demand', 'Low Demand'],
    'Sale Date': ['2024-01-15', '2023-12-10', '2024-03-05', '2023-11-20', '2024-02-25', '2024-02-10', '2023-10-15', '2023-08-30', '2024-03-12', '2024-04-05'],
    'Seasonality': ['Winter', 'Winter', 'Spring', 'Fall', 'Winter', 'Spring', 'Fall', 'Winter', 'Spring', 'Winter'],
    'Sale Price': [850000, 550000, 1250000, 600000, 920000, 750000, 850000, 950000, 670000, 750000]
}

# Convert the dictionary to a DataFrame
real_estate_data = pd.DataFrame(data)

# Save the dataset as a CSV file
real_estate_data.to_csv('real_estate_data.csv', index=False)

# Print the first few rows of the dataset
print("Dataset created successfully! Here are the first few rows:")
print(real_estate_data.head())
