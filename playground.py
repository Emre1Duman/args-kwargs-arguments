
## *args accepts unlimited arguments ##
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
        

print(add(1, 2, 3, 17, 27))


## Unlimted Keyword Arguments ##
def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nisan", model="GTR")
print(my_car.model)