import pygame


class Paddle:
    def __init__(self, game_display, x, y, width, height, color, game_state):
        self.game_display = game_display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.game_state = game_state

    def update(self, up_key_down, down_key_down):
        if up_key_down:
            self.y -= self.game_state.paddle_speed
        if down_key_down:
            self.y += self.game_state.paddle_speed
        if self.y <= self.game_state.play_area_y - self.height:
            self.y = self.game_state.play_area_y - self.height
        if self.y >= self.game_state.play_area_y + self.game_state.play_area_height:
            self.y = self.game_state.play_area_y + self.game_state.play_area_height

    def draw(self):
        pygame.draw.rect(self.game_display, self.color, [self.x, self.y, self.width, self.height])
