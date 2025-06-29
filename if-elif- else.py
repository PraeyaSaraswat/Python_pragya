#CONDITIONAL OPERATORS
# <,>,<=, >=, ==, !=
a = int(input("age:"))
print("Your age is:", a)
if(a>18):
    print("You can drive")
else:
    print("You cannot drive")
print(a>18)
print(a<18)
print(a==18)
print(a != 18)   
Mangoprice = 250
budget = 300
if(Mangoprice <= budget):
    print("Yay mango shake in the house")
else:
    print("noooooooo")   
#if elif else
num = int(input("num :"))
print("The value of num:" , num)

if(num<0):
    print("Negative")
elif(num==0):
    print("Zero")
else:
    print("Positive")       