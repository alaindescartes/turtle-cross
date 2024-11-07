from object import Object

class Block(Object):
    def __init__(self, width=0, height=0, position=(0, 0), type_shape="square",color=(0, 0, 0)):
        super().__init__(width=width, position=position, height=height, color=color, type_shape=type_shape)
        self.collision_active = False

    def move_to(self, new_position, forward_distance=0):
        super().move_to(new_position)
        if forward_distance > 0:
            self.obj.forward(forward_distance)


    def detect_collision(self, turtle):
        # Check if distance is below the collision threshold
        if self.obj.distance(turtle.turtle.position()) < 15:
            if not self.collision_active:
                print("Collision detected")
                self.collision_active = True
            return True
        else:
            self.collision_active = False
        return False