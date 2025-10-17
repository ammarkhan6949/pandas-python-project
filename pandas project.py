import pandas as pd
data={
"Name": ["priyang","Aadhya","Krisha","Vedant","Parshv","Mittal","Archana"],
"Marks":[98,89,99,87,90,83,99],
"Gender":["Male","Female","Female","Male","Male","Female","Female"]
}
df= pd.DataFrame(data)


a=df[df["Gender"] =="Female"] [["Name","Marks"]]
print(a)

srt=df.sort_values(by="Marks",ascending=True,axis=0)
print(srt) 

top=df.head(3)
print(top) 

bottom= df.tail(3)
print(bottom) 

data_shape=df.shape
print("no of rows",data_shape[0]),
print("no of colums",data_shape[1])

information=df.info()
print(information) 


null_value=df.isnull()
print(null_value.sum()) 


info=df.describe(include="all") 
print(info) 


gender= df["Gender"].unique()
print(gender) 


count= df ["Gender"].nunique()
print(count) 


gd_count= df["Gender"].value_counts()
print(gd_count) 


good_student= sum(df["Marks"].between(90,100))
print(good_student) 


avg= df["Marks"].mean()
print(avg) 


def marks(x):
    return x/2
df ["half"]=df["Marks"].apply(marks)
print(df) 


df ["m&f"]=df ["Gender"].map({"Male":1,"Female":0})
print(df) 


df.drop(["half","m&f"],axis=1, inplace=True)
print(df)