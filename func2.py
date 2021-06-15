# defining a new function 
# function with argument / input 
# with fix number of input / argument 
'''
def  sum(x,y):
    z=x+y
    print(z)

# calling function 
sum(23,900)

# dynamic argument *var -- becomes tuple 
def  add(*t):
    print(t)
    print(type(t))
    # var with 0 value 
    sum1=0
    # calling for loop 
    for  i in t:
        sum1=i+sum1
    print(sum1) # printing answer

# calling function 
add(3,23,800)
'''

#  
def  sum2(x,y=3456):
    z=x+y
    print(z)
## calling function 
sum2(10,3457)

