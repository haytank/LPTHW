#import argument variable - variable holds the arguments you pass to your python script when it runs
from sys import argv

#unpacks argument variable - assigning argument to these variables
script, filename = argv

#command to open
txt = open(filename)

print "Here's your file %r:" % filename #command to print the filename
print txt.read() #command to read the text in file - function on txt

print "Type the file name again:" 
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()