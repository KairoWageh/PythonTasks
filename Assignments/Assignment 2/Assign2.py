class Person:
    name = ''
    money = 0
    moods = ('happy','tired','lazy')
    healthRate = 0
    def healthRate(self):
        return self.__healthRate
    def healthRate(self,healthRate):
        if(healthRate in range(100)):
            return True
        else:
            return False
    def __init__(self):
        print("Person class")
    def sleep(self,hours):
        self.hours = hours
        if(hours == 7):
            mood = 'happy'
        elif(hours < 7):
            mood = 'tired'
        elif(hours > 7):
            mood = 'lazy'
    def eat(self,meals):
        self.meal = meals
        if(meals == 3):
            healthRate = 100
        elif(meals == 2):
            healthRate = 75
        elif(meals == 1):
            healthRate = 50
    def buy(self,items):
        self.items = items
        for item in items:
            money -= 10


class Employee(Person):
    import re
    moods = ('happy','tired','lazy')
    id = 0
    car = ''
    email = ''
    #salary = 0
    distanceToWork = 0
    def __init__(self):
        print('Employee class')
    def salary(self):
        return self.__salary
    def salary(self,salary):
        if salary >= 1000:
            return self.__salary
        else:
            return 0
    def email(self):
        return self.__email
    def email(self,email):
        if len(email) > 7:
            if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email):
                return True

    def work(self,hours):
        self.hours = hours
        if(hours == 8):
            mood = 'happy'
        elif(hours > 8):
            mood = 'tired'
        elif(hours < 8):
            mood = 'l0azy'

    def drive(self,distance):
        Car.run(distance)
    def refuel(self,gasAmount = 100):
        fuelRate += gasAmount

class Car:
    name = ''
    fuelRate = 0
    def velocity(self):
        return self.__velocity
    def velocity(self,velocity):
        if (velocity in range(200)):
            return True
        else:
            return False

    def fuelRate(self):
        return self.__fuelRate
    def fuelRate(self,fuelRate):
        if (fuelRate in range(100)):
            return True
        else:
            return False

    def run(self,velocity,distance):
        self.velocity = velocity
        self.distance = distance
        fuelRate -= 1

    def stop(self):
        velocity = 0
