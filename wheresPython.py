import sys
print("Python Path: {}".format(sys.executable))
print ("Python Version: {}".format(sys.version))


def greet(who2greet): 
    greeting = "Hello, {}".format(who2greet)
    return greeting

print(greet("GIT"))
print(greet("Steve"))
#47:47 GIT`