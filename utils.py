import random
from block import Block

def create_random_block(screen_width, screen_height, existing_blocks, min_distance=0):
    """
        Creates a random block with a random color, starting at the far right side of the screen,
        ensuring it doesn't overlap with existing blocks.

        :param screen_width: Width of the screen.
        :param screen_height: Height of the screen.
        :param existing_blocks: List of existing blocks to check for overlap.
        :param min_distance: Minimum distance to maintain between blocks.
        """
    colors = ["red", "blue", "green", "orange", "purple", "yellow", "cyan"]
    random_color = random.choice(colors)
    position = None
    overlap = True

    # Try to find a non-overlapping position
    while overlap:
        random_y = random.randint(-screen_height // 2 + 20, screen_height // 2 - 20)
        overlap = False  # Assume no overlap initially
        position = (screen_width // 2, random_y)

        # Check against all existing blocks
        for block in existing_blocks:
            if abs(block.obj.ycor() - random_y) < min_distance:
                overlap = True
                break  # Found overlap, retry with a new position
    # Create the block
    block = Block( width=50, height=20,position=position, color=random_color)
    return block
