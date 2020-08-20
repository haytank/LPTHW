#defining the function "cheese and crackers" - how much cheese, how many crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20,30) #function: 20 cheese_count, 30 boxes_of_crackers
#cheese_and_crackers triggers those 4 print statements above.

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#variables will be input into function below
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) #comma separates terms no matter what is being calculated. follows the same meaning as orignal function


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #same as before, just adding variable with a number
