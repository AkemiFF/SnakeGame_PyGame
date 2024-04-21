import pygame


class Snake:
    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.length = 3
        self.direction = "RIGHT"
        self.body = [(self.x, self.y)]
        self.moving = False

    def move(self):
        if self.direction == "UP":
            self.y -= self.block_size
        elif self.direction == "DOWN":
            self.y += self.block_size
        elif self.direction == "LEFT":
            self.x -= self.block_size
        elif self.direction == "RIGHT":
            self.x += self.block_size

        self.body.insert(0, (self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop()

        self.moving = True

    def draw(self, surface):
        for block in self.body:
            pygame.draw.rect(
                surface, (0, 255, 0), (block[0], block[1], self.block_size, self.block_size))

    def grow(self):
        self.length += 1

    def get_head_position(self):
        if self.moving:
            return self.body[0]
        else:
            return (10, 10)

    def reset(self, x, y, block_size):
        self.__init__(x, y, block_size)

    def stop(self):
        self.moving = False

    def update_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
