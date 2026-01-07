import turtle
turtle.Screen().bgcolor("pink" )
turtle.Screen().setup(600, 600)
turtle.Screen(). title( "Turtle polygon")
p=turtle.Turtle()
side=8
len=100
a=360/side
for i in range(side):
    p. forward(len)
    p. left(a)
turtle.done()