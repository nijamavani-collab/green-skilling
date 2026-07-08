import pandas as pd

# Reading the CSV file
data = pd.read_csv("shreet 2.csv")

# Display the complete data
print("Original Data:")
print(data)

# 1. Show the first 5 rows
print("\n1. First 5 Rows:")
print(data.head())

# 2. Show the last 5 rows
print("\n2. Last 5 Rows:")
print(data.tail())

# 3. Display basic information about the dataset
print("\n3. Dataset Information:")
data.info()

# 4. Show statistical summary of numeric columns
print("\n4. Statistical Summary:")
print(data.describe())

# 5. Display all column names
print("\n5. Column Names:")
print(data.columns)

# 6. Display the number of rows and columns
print("\n6. Shape of Dataset:")
print(data.shape)

# 7. Check if there are any missing values
print("\n7. Missing Values:")
print(data.isnull().sum())

# 8. Sort the data according to Marks
print("\n8. Data Sorted by Marks:")
print(data.sort_values("Marks"))

# 9. Count how many students are in each course
print("\n9. Number of Students in Each Course:")
print(data["Course"].value_counts())

# 10. Calculate the average marks
print("\n10. Average Marks:")
print(data["Marks"].mean())