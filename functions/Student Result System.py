def result(marks):

    average = sum(marks) / len(marks)

    if average >= 90:
        return "A"

    elif average >= 75:
        return "B"

    elif average >= 60:
        return "C"

    else:
        return "Fail"

marks = [80,90,85,75,88]

print(result(marks))