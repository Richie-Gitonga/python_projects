class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print("My name is " + self.name + ". I am a " + str(self.age) + " years old " + self.gender + " student ")

person1 = Person("Jonzing", 35, "Male")
person1.introduce()
