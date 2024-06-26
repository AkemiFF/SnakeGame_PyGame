from collision_detection.collision import CollisionHandler
import pygame
from entities.snake import Snake
from entities.food import Food
from scoring.score import Score
from input_handling.input_handler import InputHandler
from game_over_handling.game_over import GameOver
from utilities.utils import redraw_screen
import numpy as np


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
FPS = 10

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")


class Running():
    def __init__(self):
        self.running_status = True

    def get_status(self):
        return self.running_status

    def set_running_true(self):
        self.running_status = True

    def set_running_false(self):
        self.running_status = False


def main():
    snake = Snake(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BLOCK_SIZE)
    food = Food(BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT)
    score_list = np.array([0])
    score = Score()
    input_handler = InputHandler()
    game_over_handler = GameOver(SCREEN_WIDTH, SCREEN_HEIGHT)
    collision_handler = CollisionHandler()

    highest_score = 0
    running = Running()
    while running.get_status():

        snake.move()
        head_position = snake.get_head_position()
        input_handler.handle_events(pygame, running, snake)

        if snake.get_head_position() == (food.x, food.y):
            food.respawn()
            snake.grow()
            score.increase_score()

        if collision_handler.check_collision_with_self(head_position, snake) or collision_handler.check_collision_with_wall(head_position, SCREEN_WIDTH, SCREEN_HEIGHT):
            running.set_running_false()
            snake.reset(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BLOCK_SIZE)
            score_list = np.append(score_list, score.get_score())
            highest_score = score_list.max()
            game_over_handler.show_game_over_screen(
                screen, score, food, running, highest_score)

        redraw_screen(screen, snake, food, score, highest_score)

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
