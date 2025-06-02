#Concepts of def
def add(a: float, b: float) -> float:
    return a + b
print("Lets get a sum of our float:")
print(add(1,2))

#Class - a class is a blueprint of code

class car:
    #An initializer is used to set up an instance of the class
    def __init__(self, colour: str, horsepower: int) -> None: 
        self.colour = colour
        self.horsepower = horsepower

#Now lets make an instance of the class

volvo: car = car('red', 200)
print('Our first car: Volvo')
print(volvo.colour)
print(volvo.horsepower)

bmw: car = car('blue', 40)
print('The new car, BMW: ')
print(bmw.colour)
print(bmw.horsepower)

bagatata: car = car('purple', 600)
print('The new car now is bagatata')
print (bagatata.colour)
print(bagatata.horsepower)
#Classes simplify the process of creating objects


#Now we are going to learn about methods

