import turtle
polygon = turtle.Turtle()
polygon2 = turtle.Turtle()
num_sides = int(input('要畫幾邊形(3-100)?'))
side_length = 10
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    polygon2.back(side_length)
    polygon2.right(angle)
turtle.done()