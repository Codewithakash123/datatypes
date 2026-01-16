#datatypes
a = 5
b = 2.5
c = "Akash"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#arithmetic operations
e = 5
f = 2
print("Addition:",e+f)
print("Subraction:",e-f)
print("Multiplication",e*f)
print("Division:",e/f)
print("Floor Division:",e//f)
print("Modulo Division:",e%f)

#type casting
demo = "5"
print(int(demo))
print(float(demo))

#concatenation
age = 20
msg = "My age is" + str(age)
print(msg)

#error handling
try:
    num = input("Enter number:")
    int_val = int(num)
    print(int_val)
except:
    print("Invalid input")

#dynamic typing

g = 10
print(type(g))
g = "Hi"
print(type(g))
g = 3.0
print(type(g))
