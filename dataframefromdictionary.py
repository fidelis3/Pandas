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

