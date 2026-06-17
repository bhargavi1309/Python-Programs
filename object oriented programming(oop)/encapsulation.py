class student:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)
#name and show() are packed inside one class.
# Example usage
s1 = student("Bhargavi Pulindla")
s1.show()#output: Bhargavi Pulindla