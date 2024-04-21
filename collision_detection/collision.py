class CollisionHandler:
    @staticmethod
    def check_collision_with_food(snake, food):
        head_position = snake.get_head_position()
        if head_position == (food.x, food.y):
            return True
        return False

    @staticmethod
    def check_collision_with_self(head_position, snake):
        for block in snake.body[1:]:
            if head_position == block:
                return True
        return False

    @staticmethod
    def check_collision_with_wall(head_position, screen_width, screen_height):
        if (
            head_position[0] < 0 or
            head_position[0] >= screen_width or
            head_position[1] < 0 or
            head_position[1] >= screen_height
        ):
            # print(
            #     f"head : {head_position}\nwidth : {screen_width}\nheight : {screen_height}\n\n")
            return True
        return False
