
'''
class Car:
    def __init__(self,windows,enginetype):
        self.windows=windows
        self.enginetype=enginetype
    
    def drive(self):
        print(f"The person will drive {self.enginetype} car")
        
car1=Car(4,'petrol')
#car1.drive()

# inherit car class to telsa
class Telsa(Car):
    def __init__(self, windows, enginetype,is_selfdrive):
        super().__init__(windows, enginetype)
        self.is_selfdrive=is_selfdrive
    
    def self_driving(self):
        print(f"Tesla car have a more feature i.e self driving: {self.is_selfdrive}")
    
tesla1 = Telsa(4,'electric',True)
#tesla1.self_driving()
#function of parents class can be accessed by child but vice versa can't
#tesla1.drive()

#MULTIPLE INHERTIENCE

#Base class 1
class Animal:
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        print("subclass must implement this method")
        
        
#Base class 2

class Pet:
    def __init__(self,owner):
        self.owner=owner
    
    def print_owner(self):
        print(f"owner of the pet is: {self.owner}")


# Derived class with multiple inhertinace

class Dog(Animal,Pet):
    def __init__(self, name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
        
    def speak(self):
        return f"{self.name} say woof"


#create object
dog1=Dog('buddy','lorish')
# speak method is in both child and parent but here child method will override it
print(dog1.speak())
dog1.print_owner()
print(f"owner is: {dog1.owner}")
 


# Polymorphism

#method overriding

       
#Base class 
class Animal:
    
    def speak(self):
        return 'sound of animal'

#Derived class
class Dog(Animal):
    def speak(self):
        return f"Woof!"
    

#Derived class
class Cat(Animal):
    def speak(self):
        return f"Meawwww....!"
    
# objects
dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())
    
#Function that demon polymorphism

def animal_speak(animal):
    print(animal.speak())

animal_speak(dog)
animal_speak(cat)    


## Polymorphism with abstract base class(Interface) (ABCs)

from abc import ABC,abstractmethod

# Define abstract class
class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def name(self):
        pass
    
#Derived class

class Car(vehicle):
    def start_engine(self):
        return " Car engine started...."
    
    def name(self):
        return "This is a car"
    
car=Car()
print(car.name())
print(car.start_engine())

'''
'''
# Encapuslation with getter setter methods
## public,protected,private variables

class Person:
    def __init__(self,name,age,gender):
        #public variables
        self.name=name
       
        #private variable
        self.__age=age
        
        #protected
        self._gender=gender
        
    #so to acces sprivate variable
    def get_age(person):
        return person.__age
        
person=Person('riya',23,'female')
print(person.name)
#print(person.age) #can't access here as it is private
print(person.get_age())
print(person._gender) #ccan be accessed within class but also can acces from derived class


class Emp(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
    

emp=Emp('krish',22,'male')
print(emp._gender)

# public variables also added to the directory of the objects
#print(dir(person)) #here private variable will modify to another name due to privacy



# Encapuslation with getter setter methods

class Person:
    def __init__(self,name,age):
        #private variable
        self.__name=name
        self.__age=age
        
     
            
    #so to acces sprivate variable
    def get_details(self):
        return self.__name,self.__age
    
    def set_details(self,name,age):
         self.__name= name 
         self.age=age
    
p=Person('krish',34)
print(p.get_details())
#access and modify private variables using getter and setter
p.set_details('riya',20)
print(p.get_details())



#Abstraction

from abc import ABC,abstractmethod

#Abstract base class

class vehicle(ABC):
    def drive(self):
        print('The vehicle is use for drive')
    
    @abstractmethod
    def engine_type(self):
        pass
    @abstractmethod
    def start_engine(self):
        pass

#write own define of abstract method compulsory when deriving from abstract class
class Car(vehicle):
    def engine_type(self):
        return 'electric'
    def start_engine(self):
        print("car started...!")

def operate_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.drive()

car=Car()
car.drive()
print(car.engine_type())
operate_vehicle(car)


#Magic methods


class Person:
    def __init__(self,name,age):
        #public variable
        self.name=name
        self.age=age
    #overide magic methods  
    def __str__(self):
        return f"{self.name},{self.age}"

person = Person('krish',23)
print(person)
'''
#operator overoading

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    

v=Vector(2,3)
v1=Vector(2,3)
print(v+v1)
        
        
        
        
        
           



