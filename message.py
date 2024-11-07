from turtle import Turtle
class Message:
    def __init__(self):
        self.message = Turtle()
        self.position = None
        self.color = None
        self.string_message = None

    def create_message(self, position=(-270, (600 // 2) - 30), color="black", string_message=""):
        """
        Creates or updates a message on the screen at a specified position, color, and text.

        :param position: Tuple specifying (x, y) coordinates.
        :param color: Color of the text.
        :param string_message: The message text to display.
        """
        # Set attributes
        self.position = position
        self.color = color
        self.string_message = string_message

        # Clear the previous message, set color, and display the new message
        self.message.clear()
        self.message.hideturtle()
        self.message.penup()
        self.message.color(self.color)
        self.message.goto(self.position)
        self.message.write(self.string_message, align="left", font=('Arial', 15, 'normal'))