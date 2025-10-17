# pandas-python-project


## 🌟 Project Overview

This project is a detailed **Exploratory Data Analysis (EDA)** performed on a synthetic student dataset using **Python** and the powerful **Pandas** library. The primary goal was to demonstrate strong proficiency in fundamental data manipulation, cleaning, and analysis techniques to extract meaningful insights from raw data.

The project covers a comprehensive workflow, from checking data quality to performing conditional filtering and statistical aggregations.


**Pdf Link ** [pandas project_compressed.pdf](https://github.com/user-attachments/files/22969641/pandas.project_compressed.pdf)

## ✨ Key Analysis and Tasks Performed

The analysis was executed through a series of steps to thoroughly explore the dataset:


### Q1-Display name and marks of female students.
```
a=df[df["Gender"] =="Female"] [["Name","Marks"]]
print(a)
```
### Q2-Sort the DataFrame as per the marks column.
```
srt=df.sort_values(by="Marks",ascending=True,axis=0)
print(srt) 
```

### Q3- Check the first three rows of the dataset.

```
top=df.head(3)
print(top) 
```


### Q4-Check the last three rows of the dataset
```
bottom= df.tail(3)
print(bottom) 
```
### Q5-Find the shape of the dataset (number of rows and columns)

```
data_shape=df.shape
print("no of rows",data_shape[0]),
print("no of colums",data_shape[1])
```


### Q6-Get information about the dataset, including total number of rows, total number of columns, data types of each column, and memory usage
```
information=df.info()
print(information) 
```

### Q7-Check for null values in the dataset
```
null_value=df.isnull()
print(null_value.sum())
```

### Q8-Get overall statistics about the DataFrame
```
info=df.describe(include="all") 
print(info) 
```
### Q9-Find the unique values from the gender column.
```
gender= df["Gender"].unique()
print(gender) 
```


### Q10-Find the number of unique values in the gender column
```
count= df ["Gender"].nunique()
print(count) 
```

### Q11-Display the count of unique values in the gender column.
```
gd_count= df["Gender"].value_counts()
print(gd_count) 
```

### Q12-FIND THE TOTAL NUMBER OF STUDENTS HAVING MARKS BETWEEN 90 TO 100 (INCLUSIVE) USING THE BETWEEN() METHOD.
```
good_student= sum(df["Marks"].between(90,100))
print(good_student) 
```
### Q13-FIND THE AVERAGE MARKS.
```
avg= df["Marks"].mean()
print(avg)  
```
### Q14-USE THE APPLY() METHOD 

```
def marks(x):
    return x/2
df ["half"]=df["Marks"].apply(marks)
print(df) 
```


### Q15-Use the map() function

```
df ["m&f"]=df ["Gender"].map({"Male":1,"Female":0})
print(df) 
```

### Q16-Drop a column from the DataFrame
```
df.drop(["half","m&f"],axis=1, inplace=True)
print(df)
```
### Q17-PRINT THE NAMES OF ALL COLUMNS
```
print(df.columns) 
```


## 🛠 Technologies Used

| Tool | Description |
| :--- | :--- |
| **Python** | The core programming language used for scripting. |
| **Pandas** | Essential library for data structures and data analysis operations. |



## 🧑‍💻 Author

This project was developed by:

* **Name:** Ammar Khan
* **Email:** ammarkhan6949@gmail.com





