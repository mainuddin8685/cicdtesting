import pandas as pd

a= pd.DataFrame([1,2,3,4,5])
##print(a)
b={
    "Name" :["John", "Alice", "Bob", "Eve", "Charlie"],
    "Age": [25, 30, 22, 28, 35],
    "Salary": [50000, 60000, 45000, 70000, 80000],
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales"]
}
data=pd.DataFrame(b)
print("===Data===")
print(data)
Sdata = pd.Series(b)
##print(pd.DataFrame(b))
##print(Sdata)
print(data.head(2))
print("=======================")
print(data.tail(2))
print("=======================")
data_1 = (data.rename(columns={"Name" : "E_Name"}))
print(data_1)