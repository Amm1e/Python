import pyjokes
"""
Multiline Comments(dont use these days)
modules are the code which we import as packages.
pip command is used to install modules in python.
"""
# This prints a joke using pyjokes module
# You can comments many line together by selecting all the lines then ctrl + /
joke = pyjokes.get_joke()
print("==================Printing Jokes================")
print(joke)