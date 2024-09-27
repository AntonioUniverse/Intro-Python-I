# Write a function is_even that will return true if the passed-in number is even.


# YOUR CODE HERE
def is_even(val):
    if val % 2 == 0:
        print('True') 

is_even(8)

# Read a number from the keyboard
num = input("Enter number:")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


# YOUR CODE HERE
def isNumEven(val):
    if val % 2 == 0 :
        print('Even!')
    else:
        print('Odd')
isNumEven(num)
