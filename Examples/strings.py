#String literals can span multiple lines. 
# One way is using triple-quotes: """...""" or '''...'''. 
print("""\
Usage: thingy [Options]
      -h                        Display this usage message
      -H hostname               Hostname to connect to
""")
#String concatenation
print("Py"+"thon")
prefix = "Popo"
suffix = "eklyptus"
print(prefix + suffix)
#String indexing
word = "Python"
print(word[0]) #First letter
print(word[5]) #5th letter
print(word[-1]) #Last letter
print(word[-3])
#Slicing Strings
print(word[0:2])
print(word[3:5])
#Length of a string
s = "I m tired of working in that goddamned House"
print(len(s))