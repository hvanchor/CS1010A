# CS1010A --- Programming Methodology
# Mission 0

############################################################################
# Note that written answers are commented out to allow us to run your code #
# easily while grading your problem set.                                   #
#                                                                          #
# The expected answer is what you think the line of code will produce if   #
# it were to be run in IDLE.                                               #
#                                                                          #
# The final answer is the actual output after running the line of code.    #
# You may leave the final answer blank if the output is what you expected. #
############################################################################

############################################################################
# The first line has already been uncommented for you.                     #
# If a line causes an error, you should leave it commented out.            #
#                                                                          #
# Just press F5 to run this file in IDLE.                                  #
# On Mac, the shortcut for running your script is <fn> + F5 or <cmd> + F5. #
# In some Windows systems, it may be <fn> + F5 or <ctrl> + F5.             #
############################################################################

##########
# Task 1 #
##########

# Example 1:
# My expected result is zero but upon printing the result is 0.
print(0)
# expected answer: zero
# final answer: 0

# Example 2:
# My expected result is 1 which turns out to be correct after I run the
# print statements, so I don't need to do anything for the final answer.
print(1)
# expected answer: 1
# final answer:

# Example 3:
# This print statement results in an error,
# so I need to comment it and put the specific error as shown.
#print(a)
# expected answer: NameError: name 'a' is not defined
# final answer:

##############################
## YOUR MISSION STARTS HERE ##
##############################

print(42)
# expected answer:
# final answer:

#print(0000)
# expected answer:
# final answer:

#print("the force!")
# expected answer:
# final answer:

#print("Hello World")
# expected answer:
# final answer:

#print(6 * 9)
# expected answer:
# final answer:

#print(2 + 3)
# expected answer:
# final answer:

#print(2 ** 4)
# expected answer:
# final answer:

#print(2.1**2.0)
# expected answer:
# final answer:

#print(15 > 9.7)
# expected answer:
# final answer:

#print((5 + 3) ** (5 - 3))
# expected answer:
# final answer:

#print(--4)
# expected answer:
# final answer:

#print(1 / 2)
# expected answer:
# final answer:

#print(1 / 3)
# expected answer:
# final answer:

#print(1 / 0)
# expected answer:
# final answer:

#print(7 / 3 == 7 / 3.0)
# expected answer:
# final answer:

#print(3 * 6 == 6.0 * 3.0)
# expected answer:
# final answer:

#print(11 % 3)
# expected answer:
# final answer:

#print(2 > 5 or (1 < 2 and 9 >= 11))
# expected answer:
# final answer:

#print(3 > 4 or (2 < 3 and 9 > 10))
# expected answer:
# final answer:

#print("2" + "3")
# expected answer:
# final answer:

#print("2" + "3" == "5")
# expected answer:
# final answer:

#print("2" <= "5")
# expected answer:
# final answer:

#print("2 + 3")
# expected answer:
# final answer:

#print("May the force" + " be " + "with you")
# expected answer:
# final answer:

#print("force"*2)
# expected answer:
# final answer:

#print('daw' in 'padawan')
# expected answer:
# final answer:

a, b = 3, 4 # Do not comment or remove this line

#print(a)
# expected answer:
# final answer:

#print(b)
# expected answer:
# final answer:

a, b = b, a # Do not comment or remove this line

#print(a)
# expected answer:
# final answer:

#print(b)
# expected answer:
# final answer:

#print(red == 44)
# expected answer:
# final answer:

red, green = 44, 43 # Do not comment or remove this line

#print(red == 44)
# expected answer:
# final answer:

#print(red = 44)
# expected answer:
# final answer:

#print("red is 1") if red == 1 else print("red is not 1")
# expected answer:
# final answer:

#print(red - green)
# expected answer:
# final answer:

purple = red + green # Do not comment or remove this line

#print("purple")
# expected answer:
# final answer:

#print("purple"[7])
# expected answer:
# final answer:

#print(red + green != purple + purple / purple - red % green)
# expected answer:
# final answer:

#print(green > red)
# expected answer:
# final answer:

#print("green bigger") if green > red else print("red equal or bigger")
# expected answer:
# final answer:

#print(green + 5)
# expected answer:
# final answer:

#print(round(3.8))
# expected answer:
# final answer:

#print(int(3.8))
# expected answer:
# final answer:

#print(int("3.8"))
# expected answer:
# final answer:

# Run these lines of code before proceeding to the next question!
# Do not comment these lines or remove it from your submission!
def f(n):
    if n == 1: return 1
    return n + f(n - 1)

#print(f(4))
# expected answer:
# final answer:

#print(f(f(2)))
# expected answer:
# final answer:

#print(f(0))
# expected answer:
# final answer:

d = {1: 2} # Do not comment or remove this line

#print(d[1])
# expected answer:
# final answer:

#print(d[2])
# expected answer:
# final answer:

d[2] = "apple" # Do not comment or remove this line

#print(d[2])
# expected answer:
# final answer:

###########################################################
# The following 7 questions are to ensure that you have   #
# installed all the packages correctly:                   #
# - PILLOW        - matplotlib       - scipy              #
# - seaborn       - numpy            - pyglet             #
# - cocos                                                 #
#                                                         #
# Just uncomment the line "from <package> import *",      #
# run the line, and observe the output.                   #
#                                                         #
# If there is no output, the packages have been installed #
# correctly, so answer "Nothing" to let us know that it's #
# working properly. Otherwise, if you see some errors, do #
# refer to the troubleshooting guide in the PDF file.     #
###########################################################

#from PIL import *
# expected answer:
# final answer:

#from matplotlib import *
# expected answer:
# final answer:

#from scipy import *
# expected answer:
# final answer:

#from seaborn import *
# expected answer:
# final answer:

#from numpy import *
# expected answer:
# final answer:

#from pyglet import *
# expected answer:
# final answer:

#from cocos import *
# expected answer:
# final answer:
