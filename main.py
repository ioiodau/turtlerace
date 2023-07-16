import random
import turtle
import time

WIDTH, HEIGHT = 500, 500
COLORS = ["#9e0142", "#d53e4f", "#f46d43", "#fdae61", "#fee08b", "#e6f598", "#abdda4", "#66c2a5", "#3288bd", "#5e4fa2"]
TURTLES = []


def get_racers():
    while True:
        racers = int(input("Please enter the number of turtles you would like (2 - 10): "))
        if 2 <= racers <= 10:
            return racers
        else:
            print("Invalid number, please try again.")


def initialize_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")


def create_racers(racers, colors):
    division = HEIGHT/(racers + 1)
    space = HEIGHT/2-division
    for x in range(racers):
        racer = turtle.Turtle()
        racer.color(colors[x])
        racer.shape("turtle")
        racer.penup()
        racer.setpos(-230, space)
        racer.pendown()
        TURTLES.append(racer)
        space -= division
    return turtle


def race(racers, colors):
    create_racers(racers, colors)
    while True:
        for racers in TURTLES:
            distance = random.randrange(1, 20)
            racers.forward(distance)

            x = racers.xcor()
            if x >= 220:
                return colors[TURTLES.index(racers)]


def main():
    racers = get_racers()
    initialize_turtle()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    winner = race(racers, colors)
    turtle.color(winner)
    turtle.penup()
    turtle.write("The winner is... Turtle " + winner + "!", align='center', font=('Courier', 12, 'bold'))
    turtle.pendown()
    print(f"The winner is... Turtle {winner}!")
    time.sleep(10)


main()
