def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


2400 - 23 + 15 / 5 - 800
coffee = 2400
cream = 23
sugar = 5
milk = 5

tell_me = subtract(coffee, add(cream, divide(sugar, subtract(milk, 800))))

print "Now tell me the answers", tell_me
