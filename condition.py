import  time
# loading time module / library 

x=input("enter a number : ")
# input will take data in string format only 
print(type(x))

if    int(x) > 5   :
    print("Hello world !!")

elif  int(x) == 5  : 
    print("HEllo PYthon")
    time.sleep(3)  # delay of 3 seconds  
    print("Welcome to LNB")
else :
    print("NO hello !!")




'''
# x1=eval("enter only number data : ")
# only number data in accepted 



if    x1 > 5   :
    print("Hello world !!")

elif  x1  == 5  : 
    print("HEllo PYthon")
    print("Welcome to LNB")
else :
    print("NO hello !!")

'''