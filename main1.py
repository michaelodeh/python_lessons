# import test
# test.greeting()
# import test as greet
# greet.greeting()
# from test import greeting
# greeting()

# Function override
# def greeting():
#     print("Holla")

# from test import greeting,name

# print(name)

# from test import *
# print(name)

# Prevent Function Overrides

from test import greeting as new
new()