class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name = "+self.last_name)
        print("Eye Color = "+self.eye_color)
        
class Child(Parent):
    def __init__(self, last_name, eye_color, no_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.no_of_toys = no_of_toys

    def show_info(self):
        print("Last Name = "+self.last_name)
        print("Eye Color = "+self.eye_color)
        print("No. of toys = "+str(self.no_of_toys))

rowhit = Parent("Swami", "Dark Brown")
yogi = Child("Swami", "Brown", 10)
rowhit.show_info()
yogi.show_info()
rowhit.last_name
