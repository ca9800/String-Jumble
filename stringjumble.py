"""
stringjumble.py
Author: Claire 
Credit: none

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""


#inputs
text = input(str("Please enter a string of text (the bigger the better): "))
l = list(text)

#reverse letters
backwards = ''.join(list(reversed(l)))

#reverse words
w = text.split()            
w.reverse()                 
word = " ".join(w)        

#reverse both
wl = list(word)
both = ''.join(list(reversed(wl)))

#print
print (" You entered ", '"'+text+'".', "Now jumble it:")

print (backwards)
print (word)
print (both)
