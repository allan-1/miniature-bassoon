import turtle             
window = turtle.Screen()
allan = turtle.Turtle()
allan.speed(2)
for i in range(30):
   allan.circle(5*i)
   allan.circle(-5*i)
   allan.left(i)
window.exitonclick()