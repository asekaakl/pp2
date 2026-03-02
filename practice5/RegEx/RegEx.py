#Python has a built-in package called re, which can be used to work with Regular Expressions. Import the re module:
import re



import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)



#The findall() function returns a list containing all matches.
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


#example
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

#The search() function searches the string for a match, and returns a Match object if there is a match.
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#example
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)



#The split() function returns a list where the string has been split at each match:
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#example
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


#The sub() Function
#he sub() function replaces the matches with the text of your choice:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


#Match Object
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

""""
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match"
"""

#example
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
#example
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#example
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())