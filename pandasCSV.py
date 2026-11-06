import pandas as pd

print("ANiket")
##print (pd.read_csv("data.csv"))
b={
    "Name" :["John", "Alice", "Bob", "Eve", "Charlie"],
    "Age": [25, 30, 22, 28, 35],
    "Salary": [50000, 60000, 45000, 70000, 80000],
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales"]
}
data=pd.DataFrame(b)
##print(data)
data.to_excel("myData1.xlsx", index=False)
excel = pd.read_excel("Emp.xlsx")

##selct Column
print(excel[["Id","Name", "Salary"]])

##select row

