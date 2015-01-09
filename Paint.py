import turtle
turtle.hideturtle()
turtle.speed(100)


isBlue = True
NiceJob = True
isSquare = True

def drawMenu():
    turtle.begin_fill()
    turtle.color("blue")
    drawsquare(-300,200,100)
    turtle.end_fill()
    turtle.color("black")
    turtle.begin_fill()
    turtle.color("red")
    drawsquare(-150,200,100)
    turtle.end_fill()
    turtle.color("black")
    drawsquare(150,200,120)
    drawsquare(320,200,120)
    drawcircle(380,200,60)

def drawsquare(x,y,size):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+size,y)
    turtle.goto(x+size,y+size)
    turtle.goto(x,y+size)
    turtle.goto(x,y)

def drawcircle(x,y,R):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(R)

def onClick(x,y):
    global isSquare
    global NiceJob
    global isBlue

    NiceJob = True
    
    if (150<x and x<270 and 200<y and y<320):
            isSquare = True
            NiceJob = False
    elif(320<x and x<440 and 200<y and y<320):
            isSquare = False
            NiceJob = False
    if(-300<x and x<-200 and 200<y and y<300):
        isBlue = True
        NiceJob = False
    elif(-150<x and x<-50 and 200<y and y<300):
        isBlue = False
        NiceJob = False
    
    if(NiceJob):
            if(isSquare):
                drawsquare(x,y,100)
            if(isSquare == False):
                drawcircle(x,y,60)

def onClick2(x,y):
    global isBlue
    global NiceJob

    if(NiceJob):
        if(isBlue and isSquare):
            turtle.begin_fill()
            turtle.color("blue")
            drawsquare(x,y,100)
            turtle.end_fill()
        elif(isBlue and isSquare == False):
            turtle.begin_fill()
            turtle.color("blue")
            drawcircle(x,y,60)
            turtle.end_fill()
        if(isBlue==False and isSquare):
            turtle.begin_fill()
            turtle.color("red")
            drawsquare(x,y,100)
            turtle.end_fill()
        elif(isBlue==False and isSquare==False):
            turtle.begin_fill()
            turtle.color("red")
            drawcircle(x,y,60)
            turtle.end_fill()



        
drawMenu()

turtle.onscreenclick(onClick,1,True)
turtle.onscreenclick(onClick2,1,True)

    

turtle.mainloop()
