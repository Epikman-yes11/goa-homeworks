from turtle import*


#we want to paint a house


width(7)

color("green")


forward(200)

left(90)

forward(200)
      
left(90)

forward(200)

left(90)

forward(200)

left(90)

forward(70)

left(90)
forward(85)
right(90)
forward(45)
right(90)
forward(85)

penup()
goto(200,200)
pendown()
color("blue")
begin_fill()
right(180)
forward(15)
left(50)
forward(125)
left(75)
forward(125)
left(50)
forward(21)
end_fill()

penup()
goto(50,80)
pendown()
color("light blue")
begin_fill()
left(90)
forward(5)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(150,80)
pendown()
color("light blue")
begin_fill()
forward(40)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(12)
end_fill()

exitonclick()
