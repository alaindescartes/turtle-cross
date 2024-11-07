from turtle import Screen
class ScreenGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.listen()
        self.initialize_game()

    def initialize_game(self, height=600, width=600):
        self.screen.setup(width, height)
        self.screen.bgcolor('white')