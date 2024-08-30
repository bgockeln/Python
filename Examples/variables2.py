#A variable outside of a function is a different one, even if they share the same name
x = "Popo Eklyptus"
def myfunc():
    x = "freaks"
    print("Trannys are " + x)

print(x)
myfunc()
print("--------")
#declaring a global variable makes them available in and outside of a function
def myfunc2():
    global y
    y = "a danger to society"

myfunc2()

print("Trannys are " + y)