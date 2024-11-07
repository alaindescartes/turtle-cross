import screen
from turtle import Turtle

class TurtleClass:
    def __init__(self, screen_animal):
        self.turtle = Turtle()
        self.has_won = False

        # Position the turtle slightly above the bottom of the screen
        self.position = (0, - (screen_animal.screen.window_height() // 2) + 90)

        self.turtle.penup()
        self.turtle.goto(self.position)
        self.turtle.shape('turtle')

        # Set the color and shape size
        self.color = 'black'
        self.turtle.color(self.color)
        self.turtle.shapesize(1.5, 1.5, 1.5)
        self.turtle.setheading(90)

        # Bind the 'Up' key to the move method
        screen_animal.screen.listen()
        screen_animal.screen.onkey(self.move, 'Up')

    def move(self, height=600):
        """
        move the turtle forward one step
        :return:
        """
        # Move the turtle 20 units forward in its current direction
        self.turtle.forward(20)
        if self.check_bounds(height):
            self.has_won = True
            self.reset()

    def check_bounds(self, screen_height):
        """
        check if the turtle has is out of bounds
        :param screen_height: the height of the screen
        :return:
        """
        y_value = self.turtle.ycor()
        if y_value > screen_height // 2:
            return True
        return False


    def reset(self):
        """
        reset the turtle position
        :return:
        """
        self.turtle.goto(self.position)