import math
# area of a rectangle

s1 = float(input("Hello user, let's calculate the area of a rectangle, but first what is the length? "))
s2 = float(input("Awesome, now what is the width? "))
rec = s1*s2
print(f"The area of your chosen rectangle is {rec:.2f} units squared, well done!")

# Area of Circle
radius = float(input("What about a circle? choose length of radius: "))
circle = math.pi*(radius**2)
print(f"The area of this circle is {circle:.2f} units squared!! woww well done!!")

# Area of Triangle
base = float(input("OK user, what say lastly we try work out the area of a triangle? Type in the length of the base: "))
height = float(input("Nice, Now what is its height? "))
tri = (base*height)/2
print(f"You did it! The area of your triangle is {tri:.2f} units squared.")



