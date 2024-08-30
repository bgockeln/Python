#print("""
#simple calc test
#1 for addition
#2 for subtraction
#    """)
#calcing
    #addi
    #sub
#sample class
class Dog:
#class attribute
    attr1 = "mammal"
    attr2 = "dog"
#sample method
    def fun(self):
        print("I m a", self.attr1)
        print ("I m a", self.attr2)

#instance of an object of class Dog
Rodger = Dog()

#calls class attribute
print(Rodger.attr1)
#calls the method
Rodger.fun()