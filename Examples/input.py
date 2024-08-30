#String input
str = input("Enter a String: ")

#Integer input
a = int(input("Enter an Integer Number: "))

#Floating point or decimal numbers input
b = float(input("Enter a Decimal Number: "))
print("String {}, Integer {}, Decimal {}".format(str, a, b))

str2 = input("Enter a short sentence: ")
print(str2.split()) #seperating words in a string with split

n = list(map(int, input("Enter a few numbers seperated by a space: ").split()))
print(n) #taking input and converting it into integer type

