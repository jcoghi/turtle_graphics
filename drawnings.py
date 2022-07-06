import turtle
from random import randint

def dots():
    timmy = turtle.Turtle()
    timmy.shape('circle')
    timmy.pensize(5)
    timmy.shapesize(0.5)
    my_screen = turtle.Screen()
    turtle.colormode(255)

    y_position = -300
    x_position = -300

    while True:
        timmy.hideturtle()
        timmy.speed('fastest')
        timmy.up()
        timmy.setx(x_position)
        timmy.sety(y_position)
        timmy.showturtle()
        while y_position <= 300:
            timmy.color(randint(1, 255), randint(1, 255), randint(1, 255))
            if x_position <= 300:
                if timmy.isdown():
                    timmy.stamp()
                    x_position += 20
                    timmy.up()
                else:
                    timmy.setx(x_position)
                    timmy.sety(y_position)
                    timmy.pendown()
            else:
                x_position = -300
                y_position += 20

        my_screen.exitonclick()

def triangle():
    cateto_oposto = float(input("Opposite side length : "))
    cateto_adjacente = float(input("Adjacente side length: "))
    timmy = turtle.Turtle()
    timmy.penup()
    # timmy.setposition(-200, -200)
    timmy.pd()
    my_screen = turtle.Screen()
    timmy.shapesize(0.5)
    while True:
        if cateto_oposto < 100 and cateto_adjacente < 100:
            timmy.forward(cateto_oposto*10)
            timmy.left(90)
            timmy.forward(cateto_adjacente*10)
            timmy.home()
        else:
            timmy.forward(cateto_oposto)
            timmy.left(90)
            timmy.forward(cateto_adjacente)
            timmy.setposition(-200, -200)
        my_screen.exitonclick()

def square(size):
    timmy = turtle.Turtle()
    my_screen = turtle.Screen()
    timmy.shapesize(0.5)
    timmy.shape("turtle")
    if size >= 300:
        timmy.penup()
        timmy.hideturtle()
        timmy.setx(-200)
        timmy.sety(-200)
        timmy.showturtle()
        timmy.pd()
        for i in range(4):
            timmy.forward(size)
            timmy.left(90)
    else:
        for i in range(4):
            timmy.forward(size)
            timmy.left(90)
    my_screen.exitonclick()

def spirograph():
    def size_graph(diammeter, size):
        for i in range(int(360 / size)):
            tim.setheading(tim.heading() + size)
            tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
            tim.circle(diammeter)

    diam = float(input("Insert a diameter: "))
    tim = turtle.Turtle()
    turtle.colormode(255)
    tim.speed("fastest")
    size_graph(diam, int(input("Insert a size between circles: ")))
    screen = turtle.Screen()
    screen.exitonclick()

def race():
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    racers = []
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    y_position = [-70, -40, -10, 20, 50, 80]
    x_position = -290
    for n_turtle in range(0, 6):
        new_turtle = turtle.Turtle(shape='turtle')
        new_turtle.hideturtle()
        new_turtle.pu()
        new_turtle.color(colors[n_turtle])
        new_turtle.goto(x=x_position, y=y_position[n_turtle])
        new_turtle.showturtle()
        racers.append(new_turtle)

    user_bet = screen.textinput(title="Turtle Race", prompt="Wich Turtle will win this race? Enter the color")
    is_race_on = False
    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle_racer in racers:
            if turtle_racer.xcor() > 270:
                if user_bet == turtle_racer.pencolor():
                    print("You Win")
                    is_race_on = False
                else:
                    print(f"You loose. The winning color is {turtle_racer.pencolor()}")
                    is_race_on = False
            else:
                rand_distance = randint(0, 10)
                turtle_racer.forward(rand_distance)

    screen.exitonclick()

def etch():
    def move_forward():
        tim.forward(10)

    def move_back():
        tim.backward(10)

    def move_left():
        tim.setheading(tim.heading() + 10)

    def move_right():
        tim.setheading(tim.heading() - 10)

    def clear():
        tim.clear()
        tim.penup()
        tim.home()
        tim.pendown()

    tim = turtle.Turtle()
    screen = turtle.Screen()
    screen.listen()
    screen.onkey(key='w', fun=move_forward)
    screen.onkey(key='s', fun=move_back)
    screen.onkey(key='d', fun=move_left)
    screen.onkey(key='a', fun=move_right)
    screen.onkey(key= 'c', fun=clear)

    screen.exitonclick()
