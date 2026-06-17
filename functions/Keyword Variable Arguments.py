def details(**data):

    for key, value in data.items():
        print(key, ":", value)

details(name="Bhargavi",
        age=21,
        course="CSE-AI")