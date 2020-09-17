def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def  multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(50, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")
#35+(74-(180*(100/2)))
what = add(age,subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")

print("Let's try to do our formula")

coca = subtract (45, 6)
sprite = add(1000, 500)
jus_orange = multiply(26, 78)
jus_raisin = divide(70, 30)

boisson = multiply(coca, add(sprite, divide(jus_orange,subtract(jus_raisin, 5))))