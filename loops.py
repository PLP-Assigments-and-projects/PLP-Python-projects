#For loop:  Used for repeating tasks over a range. without setting any/much conditions---Repeats a block of code a fixed number of times.

# Print numbers 0 to 4
for i in range(5):
    print(i)

#i stands for an iteration(an act that is repeated)


#While Loop: Runs as long as a condition is True.

#(Repeats as long as a condition is true.)

countdown = 5

while countdown > 0:
    print("Counting down:", countdown)
    countdown -= 1

print("Blast off! 🚀")



#Customized Module in python
from Functions import greet
greet("Faith")
greet("Morris")