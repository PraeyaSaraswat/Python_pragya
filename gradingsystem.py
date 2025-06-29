marks= int(input("Your marks are:"))
print("Your marks are:", marks)
name = str(input("Your name is:"))
print("Your name is: " , name)
if(marks>90 and marks<100):
        print("You got: A+")
        print("Remark: EXCELLENT")
        print("Status: PASS")
elif(marks>80 and marks<89):
        print("You got A")
        print("Remark: GREAT WORK")
        print("Status: PASS")
elif(marks>70 and marks<79):
        print("You got: B")
        print("Remark: GOOD JOB")
        print("Status: PASS")
elif(marks>60 and marks<69):
        print("You got: C")
        print("Remark: FAIR ENOUGH")
        print("Status: PASS")
elif(marks>50 and marks<59):
        print("You got : D") 
        print("Remark: NEEDS IMPROVEMENT")
        print("Status:PASS")
else:
        print("FAIL")                       