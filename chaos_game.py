# Connor Luckett
# This is the main method to run

import random
import turtle


def main():

    draw()


def draw():

    # Collect starting point
    startX = int(input("Input starting x: "))
    startY = int(input("Input starting y: "))
    numTrials = int(input("Input number of points: "))

    # Points of the triangle
    xPos1 = -100
    yPos1 = 0

    xPos2 = 100
    yPos2 = 0

    xPos3 = 0
    yPos3 = 100 * (3 ** (1/2))

    # Create a turtle
    turt = turtle.Turtle()
    turt.speed(9)
    minX = -150
    minY = -50
    maxX = 150
    maxY = 170
    screen = turt.getscreen()
    screen.reset()
    screen.setworldcoordinates(minX, minY, maxX, maxY)

    # Send the turtle home and pickup
    turt.home()
    turt.penup()

    # Go to starting point
    turt.goto(startX, startY)

    # Dot
    turt.dot(1.5, "red")

    # Loop through until done
    i = 0
    while i < numTrials:
        # Roll for a random integer
        roll = random.randint(1, 3)

        # Find the new place to go for x and y position
        if roll == 1:
            startX = findNew(startX, xPos1)
            startY = findNew(startY, yPos1)
        elif roll == 2:
            startX = findNew(startX, xPos2)
            startY = findNew(startY, yPos2)
        else:
            startX = findNew(startX, xPos3)
            startY = findNew(startY, yPos3)

        # Go to the new point
        turt.goto(startX, startY)

        # Dot
        turt.dot(1.5, "blue")

        # Increment through loop
        i += 1

    # Mr. Turtle should stay around
    turtle.exitonclick()


# i for initial, n for direction of new
def findNew(i, n):
    newPos = (i + n) / 2
    return newPos


if __name__ == "__main__": main()
