import time

# name of function -- motd -- message of the day
# function without argument / input 
def  motd():
    print("Hey !! How are you..?")
    time.sleep(1)
    print("current time is ",time.ctime())
    time.sleep(1)
    print("Lets work !!")
# define function 
def  sum():
    result=10+20
    print(result)
    time.sleep(2)
    # calling function 
    motd()
# calling function 
sum() 





