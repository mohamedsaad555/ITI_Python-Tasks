#1
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(3)
print(NewCircle.area())
print(NewCircle.perimeter())


#2
from datetime import date
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

# Example usage
person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
# person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
# person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))
# Accessing attributes and calculating age
# print("Person 1:")
# print("Name:", person1.name)
# print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.calculate_age())

# print("\nPerson 2:")
# print("Name:", person2.name)
# print("Country:", person2.country)
# print("Date of Birth:", person2.date_of_birth)
# print("Age:", person2.calculate_age())

# print("\nPerson 3:")
# print("Name:", person3.name)
# print("Country:", person3.country)
# print("Date of Birth:", person3.date_of_birth)
# print("Age:", person3.calculate_age())

#3
import math

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


# Example usage
r = 7
circle = Circle(r)
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()

print("Radius of the circle:",r)
print("Circle Area:", circle_area)
print("Circle Perimeter:", circle_perimeter)


l = 5
w = 7
rectangle = Rectangle(l, w)
rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()
print("\nRectangle: Length =",l," Width =",w)
print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)

base = 5
height = 4
s1 = 4
s2 = 3
s3 = 5

print("\nTriangle: Base =",base," Height =",height," side1 =",s1," side2 =",s2," side3 =",s3)
triangle = Triangle(base,height,s1,s2,s3)
triangle_area = triangle.calculate_area()
triangle_perimeter = triangle.calculate_perimeter()
print("Triangle Area:", triangle_area)
print("Triangle Perimeter:", triangle_perimeter)

#4
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total


# Example usage
cart = ShoppingCart()

cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)

print("Current Items in Cart:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)

cart.remove_item("Orange")

print("\nUpdated Items in Cart after removing Orange:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)
 