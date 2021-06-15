import turtle
colors=["purple","blue","red","green","orange","yellow"]
mypen=turtle.Pen()
turtle.bgcolor('black') 
for x in range(360):
    mypen.pencolor(colors[x%6])
    mypen.width(x/100 +1)
    mypen.forward(x)
    mypen.left(59)