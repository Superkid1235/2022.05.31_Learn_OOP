class Employee:

    def __init__(self, name, title, experience):
        self.name = "HAHA name"
        self.title = "HAHA title"
        self.experience = "haha experience"

    def get_experience(self):
        return self.experience

    # static method, invoked by a class, not an instance
    def class_detials():
        print("This is the parent class")


class Engineer(Employee):
    pass

eng1 = Engineer("Mr.Tim", "Static Eq. Engineer", 2.5)


Employee.class_detials()
Engineer.class_detials()