with open("student.txt", "r") as source:
    data = source.read()

with open("backup.txt", "w") as target:
    target.write(data)

print("File copied successfully")