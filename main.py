import time
from animal import TurtleClass
from screen import ScreenGame
from utils import create_random_block
from message import Message

# Initialize screen
screen = ScreenGame()
turtle = TurtleClass(screen_animal=screen)
message = Message()
screen_width = 600
screen_height = 600
is_game_over = False
screen.initialize_game(width=screen_width, height=screen_height)
message.create_message(string_message="Level 1")

# List to hold active blocks
blocks = []
nbr_of_wins = 0

# Main loop
while True:
    # Create a new block at intervals
    if len(blocks) < 10:
        random_block = create_random_block(screen_width=screen_width,
                                           screen_height=screen_height, existing_blocks=blocks)
        random_block.draw_object()
        blocks.append(random_block)

    # Move each block left
    for block in blocks:
        x, y = block.obj.position()

        # Check if the turtle has won and increase speed and level if so
        if turtle.has_won:
            nbr_of_wins += 1
            turtle.has_won = False  # Reset win status for the next level
            message.create_message(string_message=f"Level {nbr_of_wins + 1}")

        # Set block speed based on number of wins
        block.obj.goto(x - (5 + nbr_of_wins), y)

        # Check for collision with the turtle
        if block.detect_collision(turtle=turtle):
            is_game_over = True

        # Remove blocks that have moved off-screen
        if block.obj.xcor() < -screen_width // 2:
            block.obj.hideturtle()
            blocks.remove(block)

    # End the game if collision is detected
    if is_game_over:
        message.create_message(string_message="Game Over", position=(0, 0))
        break

    screen.screen.update()
    time.sleep(0.05)

# Keep the window open after game over
screen.screen.mainloop()
