import sys
import requests
from os import rename


print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("Word"))
print(greet("Railyn"))
