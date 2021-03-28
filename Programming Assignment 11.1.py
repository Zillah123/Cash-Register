#File name: Programming Assignment 11.1.py
#Name: Emmanuel Vidal
#Date: 02/23/2020
#Course: DSC510-T302 - Introduction to Programming (2203-1)
#Assignment number: 11.1
#Purpose of the assignment: This program will create a simple cash register program by using an Object Oriented Programming
print("Welcome Prof. Michael Eller. Thank you for grading my assignment") #Welcome Message
class CashRegister: #Class CashRegister
    def __init__(self): #Initializer of the class
        self.price=0.00
        self.totalPrice=0.00
        self.itemCount=0


    def addItem(self,price,): #Instance method called addItem
        self.itemCount=self.itemCount+1 #Keep track of items in the chart
        self.totalPrice=self.totalPrice+price #Total price in the Object
        self.price=price

    def getTotal(self,): #Getter methods
        return self.totalPrice

    def getCount(self): #Getter methods
        return self.itemCount

register=CashRegister() #Instance of the CashRegister

while True: #Iterate through a loop until the user is done
    user_cont = input('Do you want to purchase an item, Y for yes and N for No?') #Options for user
    if user_cont == 'Y': #user selects Y
        price=float(input("Please enter the Price of the purchased item:")) #User enters prices
        register.addItem(price)
    elif user_cont == 'N':
        break
    else:
        print("Invalid User Input")


print("-----------------Receipt Details-----------------") #Print Receipt
print("Total Number of Items in The Cart:",register.getCount()) #Print Number of items in the cart
print("Total price of Items in the the cart:","$",register.getTotal(),sep="") #Print Price of items
