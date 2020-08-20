def coffee_preference(black_coffee, cream_and_sugar):
    print "%d people drink their coffee unadulterated." % black_coffee
    print "While %d prefer to mix in cream and sugar." % cream_and_sugar
    print "All of them like hot coffee."
    print "But some like it iced too."

print "This one's just getting numbers..."
coffee_preference(15, 22)

print "I'll add variables for this guy."
drinkers_that_added_nothing = 43
drinkers_that_added_stuff = 34


coffee_preference (drinkers_that_added_nothing, drinkers_that_added_stuff)


print "I guess we could do math too - gross"
coffee_preference(13 + 59, 32 + 28)


print "And since we're feeling extra, we'll do math and variables together."
coffee_preference(drinkers_that_added_nothing + 100, drinkers_that_added_stuff + 101)
