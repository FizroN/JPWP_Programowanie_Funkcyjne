class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.age = age
        self.surname = surname


class Passenger(Person):
    def __init__(self, name, surname, status, age, has_document):
        super().__init__(name, surname, age)
        self.status = status
        self.has_document = has_document 


class Conductor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        
    def Allow(self):
        print("Okay, have a nice trip")

    def Deny(self):
        print("I'm sorry, but you don't have proper rights to exemption")

    def Check(self, passenger):
        if passenger.status == "student":
            print("Please show me the student ID")
            if passenger.has_document:
                self.Allow()
            else:
                self.Deny()
        elif passenger.status == "senior":
            print("Please show me a document confirming a senior status")
            if passenger.has_document:
                self.Allow()


passengers = [
    Passenger("Bartek", "Gawel", "student", 21, False),
    Passenger("Karol", "Gawelek", "student", 20, True),
    Passenger("Ferdynand", "Kiepski", "senior", 80, True),
    Passenger("Janusz", "Kowalski", None, 34, False)
]
conductor = Conductor("Albert", "Abramczuk", 44)
for p in passengers:
    """if p.status is not None:
        if p.status == "student":
            print("Please show me the student ID")
            if p.has_document:
                print("Okay, have a nice trip")
            else:
                print("I'm sorry, but you don't have proper rights to exemption")
        elif p.status == "senior":
            print("Please show me a document confirming a senior status")
            if p.has_document:
                print("Okay, have a nice trip")
    else:
        print("Okay, have a nice trip")"""
    if p.status is not None:
        conductor.Check(p)
    else:
        conductor.Allow()
