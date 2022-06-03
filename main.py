class car:
    # create class variables
    vehicle = "car"

    def __init__(self, brand, model):
        # initialize instance variables
        self.brand = brand
        self.model = model


c1 = car("Toyota", "Altist")
print("Class Variable  = ", c1.vehicle)
print("Instance Variable = ", c1.brand, c1.model)




