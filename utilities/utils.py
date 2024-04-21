import pygame


def draw_grid(surface, screen_width, screen_height, block_size):
    for x in range(0, screen_width, block_size):
        pygame.draw.line(surface, (100, 100, 100), (x, 0), (x, screen_height))
    for y in range(0, screen_height, block_size):
        pygame.draw.line(surface, (100, 100, 100), (0, y), (screen_width, y))


def redraw_screen(surface, snake, food, score):
    surface.fill((0, 0, 0))
    snake.draw(surface)
    food.draw(surface)
    draw_grid(surface, surface.get_width(),
              surface.get_height(), snake.block_size)

    score_font = pygame.font.SysFont(None, 24)
    score_text = score_font.render(
        "Score: " + str(score.get_score()), True, (255, 255, 255))
    surface.blit(score_text, (10, 10))

    pygame.display.update()


def restart_game(food, score, running):
    running.set_running_true()
    food.respawn()
    score.reset_score()
