import turtle
turtle. Screen(). bgcolor( "pink" )
turtle.Screen( ).setup(500, 500)
turtle.Screen().title ("spiral pattern")
p=turtle.Turtle()
S=0
while True:
    for i in range(8):
        p. forward(s+1) 
        p.right(45)
        s=s-5
    s=s+1