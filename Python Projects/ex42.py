#Animal is a object, check extra credit questions

class Animal(object):
    pass

class Dog(Animal):
    

    def __init__(self, name):
            ##??
            self.name = name


##is-a
class Cat(Animal):

    def __init__(self, name):
        ## ?? 
        self.name = name


## has-a
class Person(object):
    


    def __init__(self, name):
        ## ?? 
        self.name = name

        ## Person has a pet of some kind

        self.pet = None


##is-a
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?

        super(Employee, self).__init__(name)
        ## ?? 
        self.salary = salary

##has-a
class Fish(object):
    pass

##is-a
class Salmon(Fish):
    pass

##is-a
class Halibut(Fish):
    pass

## rover is a Dog
rover = Dog("Rover")

##satan is-a Cat
satan = Cat("Satan")
##is-a person
mary = Person("Mary")
##has-a pet
mary.pet = satan
##is-a Employee
frank = Employee("Frank", 120000)
##has-a pet
frank.pet = rover

#is-a
flipper = Fish()
##is-a Salmon
crouse = Salmon()

harry = Halibut()

