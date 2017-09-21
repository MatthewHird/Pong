import pygame
import os


class Window:
    def __init__(self, caption, icon, width, height):
        self.caption = caption
        self.icon = icon
        self.width = width
        self.height = height
        self.clock = None
        self.display = None

    def initiate(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        screen_dimensions = pygame.display.Info().current_w, pygame.display.Info().current_h
        win_pos_left = 1 + ((screen_dimensions[0] - self.width) // 2)
        win_pos_top = 1 + ((screen_dimensions[1] - self.height) // 2)
        os.environ['SDL_VIDEO_WINDOW_POS'] = '{0},{1}'.format(win_pos_left, win_pos_top)

        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)
        pygame.display.set_icon(pygame.image.load(self.icon))

        os.environ['SDL_VIDEO_WINDOW_POS'] = ''
