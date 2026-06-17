#pip install pandas is a command to install pandas library in python.
import pandas as pd
data = {
    "Name":["Ravi","Priya"],
    "CGPA":[8.5,9.2]
}

df = pd.DataFrame(data)

print(df)
    