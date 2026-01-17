# note :- 'abc' file is inbuilt in python


from abc import ABC,abstractmethod

class Vehicle(ABC):                     #Abstract Class

    @abstractmethod
    def stop():
        pass


class Bike(Vehicle):
    def start(self):
        print('Bike started')

    def stop(self):
        print('Bike Stopped')

    
b1= Bike()
b1.start()
b1.stop()

# v1=Vehicle()      #Error





  