import pandas as pd

data = {
    "Student":["Ravi","Priya","Bhargavi"],
    "CGPA":[8.5,9.2,9.07]
}

df = pd.DataFrame(data)

print(df)
#output will be a table with two columns, Student and CGPA, and three rows with the respective values.