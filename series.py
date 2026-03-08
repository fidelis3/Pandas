
# A Series is a one-dimensional labeled array that can hold any data type (integers, floats, strings, etc.). It is a fundamental data structure in the pandas library and is often used to represent a single column of data in a DataFrame. Each element in a Series has an associated index, which allows for easy access and manipulation of the data.
import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)

print(s)  # Print the Series
print(s + 5)  # Add 5 to each element in the Series

#Accessing elements in a series
   #Accessing by label
print(s[0])  # Access the first element

   #Accessing by position
print(s.iloc[3]) # Access the element at position 3 (value 40)
   
   #Accessing a range of elements
print(s[1:4])   # Access a range of elements by label