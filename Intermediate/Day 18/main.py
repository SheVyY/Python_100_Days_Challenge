import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color = (r, g, b)
	return color


# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
# 	tim.color(random_color())
# 	tim.forward(30)
# 	tim.setheading(random.choice(directions))


tim.speed("fastest")

def draw_spirograph(size_of_gap):
	for _ in range(int(360 / size_of_gap)):
		tim.color(color())
		tim.circle(100)
		tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(30)


screen = t.Screen()
screen.exitonclick()
