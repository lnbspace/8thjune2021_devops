import time
import subprocess
import  os

user_input='''
Press 1 to Check current time and Date :- 
Press 2 to Check RAM Size of Your current OS  :- 
Press 3 to KNow Name of YOur current OS :- 
Press 4 to Check What is MAc Address of YOur lapTOP/PC/VM/CLoudVM :- 
Press 5 to create one directory IN your Desktop :- 
Press 6 to Restart Your current OS :- 
Press 7 to Print list of all available Wifi in your laptop Range :-
Press 8 to RUn another code in Your current folder  :-  
Press 9 to exit the programe :- 
'''
while True: 
    print(user_input)
    # to accept input from user 
    user_choice=input()
    # printing user input 
    #print("user has entered ",user_choice)

    if  user_choice ==  '1' :
        mytime=time.ctime()
        print("current date and time IS ",mytime)
        
    elif  user_choice  ==  '2' :
        print("checking my OS Name ..Plz wait ")

    elif  user_choice  ==  '8' :
        # calling another code
        os.system('python3 condi1.py')
    
    else :
        print("Jeevan me kuch samajh nhi aa rhii...")