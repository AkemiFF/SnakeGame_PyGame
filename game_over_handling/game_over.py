import pygame
import sys
from utilities.utils import restart_game


class GameOver:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.SysFont(None, 36)

    def show_game_over_screen(self, screen, score, food, running):
        game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        score_text = self.font.render(
            "Score: " + str(score.get_score()), True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(
            center=(self.screen_width // 2, self.screen_height // 2 - 20))
        score_rect = score_text.get_rect(
            center=(self.screen_width // 2, self.screen_height // 2 + 20))

        button_font = pygame.font.SysFont(None, 24)
        restart_text = button_font.render("Restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(
            center=(self.screen_width // 2, self.screen_height // 2 + 60))

        quit_text = button_font.render("Quit", True, (255, 255, 255))
        quit_rect = restart_text.get_rect(
            center=(self.screen_width // 2+10, self.screen_height // 2 + 85))

        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)
        screen.blit(restart_text, restart_rect)
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if restart_rect.collidepoint(mouse_pos):
                        restart_game(food, score, running)
                        waiting = False

                    if quit_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
