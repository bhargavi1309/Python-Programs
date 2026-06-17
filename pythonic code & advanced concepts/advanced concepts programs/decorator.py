def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper

@decorator#this is called decorator syntax, it is a shorthand for hello = decorator(hello)
def hello():
    print("Hello")

hello()