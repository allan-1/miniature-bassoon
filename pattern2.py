import turtle
window = turtle.Screen()
my_pen = turtle.Turtle()       
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
window.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)
my_pen.hideturtle()
window.mainloop()