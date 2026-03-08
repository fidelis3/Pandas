import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df)


# Accessing columns in the DataFrame
print(df['Name'])  # Access the 'Name' column
print(df['Age'])   # Access the 'Age' column


# Accessing rows in the DataFrame
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])    # Access the second row by label

#Slicing 
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows


#To find unique elements
unique_dates = df['Age'].unique()
print(unique_dates)


#Saving the DataFrame to a CSV file
#o save a DataFrame to a CSV file, use the to_csv method and specify the filename with a “.csv” extension.Pandas provides other functions for saving DataFrames in different formats
df.to_csv('output.csv', index=True)  # Save the DataFrame to a CSV