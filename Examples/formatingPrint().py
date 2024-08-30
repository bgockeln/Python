name = "Dikt"
age = "42"
loca = "Hagen"
print("Name: {}, Age: {}, Living in: {}".format(name, age, loca)) #formating the string with format()
print("------")
print("Gawkeln", "Benedict", sep=", ") #using a , to seperate the words using sep
print("---------")
print("Gawkeln", "Benedict", sep=", ", end="!") #example of 'sep' and 'end'
print("------")
#formating with string method
cstr = "I love female legs"
print("Center aligned string with fillchr: ")
print(cstr.center(40, "#"))

print("The left aligned string is : ")
print(cstr.ljust(40, "-"))

print("The right aligned string is : ")
print(cstr.rjust(40, "-"))