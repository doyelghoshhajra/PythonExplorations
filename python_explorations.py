# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 00:32:12 2023

@author: email
"""

print ("hello world!")

#function to convert farhenheit to celcius and vice versa

def func_cel_far (temp_in_cel):
    temp_in_far=(temp_in_cel*(9/5))+32
    return temp_in_far
final_temp=func_cel_far(30)
print("Temperature in Farhenheit = ", final_temp)

def func_far_cel (temp_in_far):
    temp_in_cel=(temp_in_far-32)*(5/9)
    return temp_in_cel
final_temp=func_far_cel(30)
print("Temperature in Celcius = ", final_temp)


#write a function to reverse a string

def reverse_name(any_name):
    result=""
    for i in any_name:
        result=i+result
    return result

def palindrome_check(original_string,reverse_string):
    if original_string == reverse_string:
        return True
    else:
        return False

The_name_I_want_to_pass="kadak"    
reverse_of_given_name=reverse_name(The_name_I_want_to_pass)
is_palindrome_check=palindrome_check(The_name_I_want_to_pass,reverse_of_given_name)
print("The reverse name of any given is = ", reverse_of_given_name)
print("There is a palindrome = ", is_palindrome_check)


#Write a Python function to check if a string is a palindrome.
def is_palindrome(string):
    return string == string[::-1]

#Write a Python program to count the occurrence of each character in a string
def count_characters(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

#Write a Python program to check if two strings are anagrams.
def are_anagrams(string1, string2):
    return sorted(string1) == sorted(string2)

#Write a Python program to find the first non-repeating character in a string
from collections import Counter
def first_non_repeating_char(string):
    char_count = Counter(string)
    for char in string:
        if char_count[char] == 1:
            return char
    return None


#python string related concepts:

# What is Pandas and how would you import it?
# A:Pandas is a Python library used for data manipulation and analysis.
# To import it, you can use:
    import pandas as pd.

# How do you read a CSV file using Pandas?
import pandas as pd
df = pd.read_csv('filename.csv')

# How would you check the first few rows of a DataFrame?
print(df.head())

#How do you handle missing values in a DataFrame?
# A:Drop rows with missing values
df.dropna(inplace=True)
# A:Fill missing values
df.fillna(value, inplace=True)

#Explain the difference between loc and iloc?
# A:loc is used for label-based indexing, while iloc is used for integer-based indexing. Example:
df.loc[2]  # Access row with label/index 2
df.iloc[2] # Access row with integer index 2

#How can you select specific columns from a DataFrame?
selected_columns = df[['column1', 'column2']]

#How do you group data using Pandas?
grouped = df.groupby('category_column')

#How do you calculate the mean and median of a DataFrame column?
mean_value = df['column'].mean()
median_value = df['column'].median()

#Explain what Matplotlib and Seaborn are used for.
# A:Matplotlib: A popular plotting library for creating static, interactive, and animated visualizations in Python.
# A:Seaborn: A higher-level interface for creating attractive and informative statistical graphics.

#How can you create a histogram using Matplotlib?
import matplotlib.pyplot as plt
plt.hist(df['column'], bins=10)
plt.show()

#What is a correlation matrix? How can you create and visualize it using Seaborn?
# A:A correlation matrix shows the correlation coefficients between variables in a DataFrame.
import seaborn as sns
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

#How can you perform a basic linear regression using a library like Scikit-Learn?
from sklearn.linear_model import LinearRegression
X = df[['feature1', 'feature2']]
y = df['target']
model = LinearRegression()
model.fit(X, y)

#python examples on: 
# data types
# operators
# decision making
# loops
# numbers
# strings
# lists
# tuples
# dictionary
# date-time
# functions
# modules
# files I/O
# exception
# class/object
# hello world
# local-global

# Data Types:
# Integer
age = 25
# Float
price = 29.99
# String
name = "John"
# Boolean
is_student = True
# List
fruits = ["apple", "banana", "orange"]
# Tuple
coordinates = (3, 5)
# Dictionary
person = {"name": "Alice", "age": 30}

#Operators:
# Arithmetic operators
result = 10 + 5 * 2
# Comparison operators
is_equal = 5 == 5
# Logical operators
is_both_true = True and False

#Decision Making (if-else):
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
    
#Loops (for and while):
# For loop
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1
    
#Numbers:
x = 5
y = 2
result = x + y

#Strings:
name = "Alice"
greeting = "Hello, " + name

#Lists:
fruits = ["apple", "banana", "orange"]
fruits.append("grape")

#Tuples:
coordinates = (3, 5)
x, y = coordinates

#Dictionary:
person = {"name": "Bob", "age": 25}
print(person["name"])

#Date-Time:
import datetime
current_time = datetime.datetime.now()
print(current_time)

#Functions:
def greet(name):
    return "Hello, " + name
message = greet("Alice")
print(message)

#importing a module and using it to get a result:
import math
square_root = math.sqrt(25)

#Files I/O:
with open("example.txt", "r") as file:
    content = file.read()
    
#Exception Handling:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
    
#Class/Object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

#Hello World:
print("Hello, World!")

#Local and Global Variables:
global_var = "This is a global variable"

def func():
    local_var = "This is a local variable"
    print(global_var)

func()

# Some commonly used functions and methods in the Pandas library for data analysis:

# Data Loading:
# pd.read_csv(filename): Load data from a CSV file into a DataFrame.
# pd.read_excel(filename): Load data from an Excel file into a DataFrame.
# pd.read_sql(query, connection): Load data from a SQL query into a DataFrame.

# Data Exploration:
# df.head(n): Display the first n rows of the DataFrame.
# df.tail(n): Display the last n rows of the DataFrame.
# df.shape: Get the dimensions (rows, columns) of the DataFrame.
# df.info(): Display summary information about the DataFrame.
# df.describe(): Generate summary statistics of numeric columns.

# Data Selection and Indexing:
# df['column']: Access a single column by label.
# df[['column1', 'column2']]: Access multiple columns as a new DataFrame.
# df.loc[row_label, col_label]: Access a specific row and column by label.
# df.iloc[row_index, col_index]: Access a specific row and column by index.

# Data Cleaning:
# df.drop(columns=['column']): Remove a column from the DataFrame.
# df.dropna(): Remove rows with missing values.
# df.fillna(value): Fill missing values with a specific value.
# df.replace(old_value, new_value): Replace specific values in the DataFrame.

# Data Transformation:
# df.groupby('column').agg(func): Group data by a column and apply an aggregation function.
# df['new_column'] = df['column'].apply(func): Apply a function to create a new column.
# df.sort_values('column'): Sort the DataFrame by a specific column.
# df.drop_duplicates(): Remove duplicate rows from the DataFrame.

# Data Visualization:
# df.plot(kind='line', x='x_column', y='y_column'): Create simple plots using Matplotlib.
# sns.heatmap(corr_matrix): Create a heatmap of correlation matrix using Seaborn.
# df.plot.bar(), df.plot.hist(), df.plot.box(), etc.: Create various types of plots.

# Data Aggregation:
# df.groupby('column').agg({'other_column': 'mean', 'another_column': 'sum'}): Aggregate multiple columns using different functions.
# df.pivot_table(values='value_column', index='index_column', columns='column'): Create a pivot table.

# Data Merging and Joining:
# pd.concat([df1, df2]): Concatenate DataFrames vertically.
# pd.merge(df1, df2, on='column'): Merge DataFrames based on a common column.

# Time Series Operations:
# pd.to_datetime(df['date_column']): Convert a column to datetime format.
# df.resample('D').sum(): Resample time-series data at a specific frequency.



