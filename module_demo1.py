import time
import sys,os
# want to take inline input
#print(sys.argv)
# printing all inline input values including file name as well
only_input=sys.argv[1:]
print(only_input)
# checking inputs are command or not 
for i in only_input:
    out=os.system(i)
    if out == 0 : 
        print("yes ",i," command is present in current os")
    else :
        print("command ",i," not present in OS")