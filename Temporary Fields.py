class Person:

    # constructor or initializer
    def __init__(self, name, telephone, address, x, y):
        self.name = name
        self.telephone = telephone
        self.address = address

    # method which returns a string
    def whoami(self):
        return "You are " + self.name

    def personalInfo(self):
        return self.whoami()+" telephone: "+self.telephone+" address:"+self.address


class Distance:

    def distance_square(self, x, y):
        return x*x+y*y
