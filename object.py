from animal import Turtle


class Object:
    def __init__(self, color, width=0, height=0, position = (0,0), type_shape ="square"):
        self.color = color
        self.width = width
        self.height = height
        self.position = position
        self.type = type_shape
        self.obj = Turtle()

    def draw_object(self):
        """
        Draws the object with the specified color, shape, size, and position.
        """
        self.obj.color(self.color)
        self.obj.shape(self.type)
        self.obj.shapesize(stretch_wid=self.height / 20, stretch_len=self.width / 20)
        self.obj.penup()
        self.obj.goto(self.position)

    def move_to(self, new_position):
        """
        moves the object to the specified position.
        :param new_position: the position to move the object to
        """
        self.obj.goto(new_position)

    def change_color(self, new_color):
        """
        Changes the color of the object.
        :param new_color: the new color of the object
        """
        self.color = new_color
        self.obj.color(new_color)