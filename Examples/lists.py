#creating a list named squares
squares = [1, 4, 9, 16, 25]
print(squares)
#indexing the items in squares
print(squares[0])
print(squares[-1])
print(squares[3])
#slicing returns a new list
print(squares[3:])
#List concatenation
print(squares + [36, 49, 64, 81, 100])
#replacing an item
cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64 #Replace 65 with 64
print(cubes)
#appending an item to a list
rgb = ["Red", "Green", "Blue"]
print(rgb)
rgb.append("Alph")
print(rgb)
#making a 'Shallow Copy' and correcting an entry
correct_rgb = rgb[:] #makes the copy(slicing operation)
correct_rgb[-1] = "Alpha" #replace
print(correct_rgb)
print("--------")
#replacing items in a list, removing items, emptying the list
letters = ["a", "b", "c", "d", "e", "f", "g",]
print(letters)
#replacing some values
letters[2:5] = ["C", "D", "E"]
print(letters)
#removing values
letters[2:5] = [] #replacing with an empty list
print(letters)
#clear the list
letters[:] = []
print(letters)
lettas = ["a", "b", "c", "d"]
print(len(lettas))
print("----")
#nesting a list in another list
a = ["a", "b", "c", "d"]
b = [1, 2, 3, 4]
x = [a, b]
print(x)
print(x[0])
print(x[1])
print(x[0][2])
print(x[1][2])