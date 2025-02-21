class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print("Barks...")
    def sleep(self):
        print(" sleepyyyyy...")
class puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name=name
        self.age=age
    def play(self):
        print("playsssss")
my_puppy=puppy("daisy",7)
my_puppy.play()
my_puppy.bark()
my_puppy.sleep()