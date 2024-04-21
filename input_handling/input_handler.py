import sys


class InputHandler:
    def __init__(self):
        pass

    def handle_events(self, pygame, running, snake):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running.set_running_false()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z or event.key == pygame.K_UP:
                    snake.update_direction("UP")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    snake.update_direction("DOWN")
                elif event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    snake.update_direction("LEFT")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    snake.update_direction("RIGHT")
