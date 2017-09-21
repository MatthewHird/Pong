import pygame
import random
import math


PI = math.pi
DEG = math.pi / 180


class Ball:
    def __init__(self, game_display, x, y, width, height, color, speed, angle, game_state):
        self.game_display = game_display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.angle = angle
        self.game_state = game_state

    def update(self):
        self.y = self.y + self.speed * math.sin(self.angle)

        if self.y <= self.game_state.play_area_y:
            self.y = self.game_state.play_area_y
            self.angle = 2 * PI - self.angle + random.randint(-1, 1) * DEG
        elif self.y >= self.game_state.play_area_y + self.game_state.play_area_height - self.height:
            self.y = self.game_state.play_area_y + self.game_state.play_area_height - self.height
            self.angle = 2 * PI - self.angle + random.randint(-1, 1) * DEG

        self.angle = (self.angle + 2 * PI) % (2 * PI)

        ecc_a = ((self.game_state.paddle_a.y + self.game_state.paddle_height / 2) - (self.y + self.height / 2)
                 ) / self.game_state.paddle_height * self.game_state.paddle_aim
        ecc_b = ((self.y + self.height / 2) - (self.game_state.paddle_b.y + self.game_state.paddle_height / 2)
                 ) / self.game_state.paddle_height * self.game_state.paddle_aim

        self.x = self.x + self.speed * math.cos(self.angle)

        if self.x <= self.game_state.play_area_x:
            if self.y + self.height >= self.game_state.paddle_a.y and \
                            self.y <= self.game_state.paddle_a.y + self.game_state.paddle_height:
                self.x = self.game_state.play_area_x
                if self.angle == PI:
                    self.angle = (2 * PI + random.randint(-1, 1) * DEG) % (2 * PI)
                else:
                    self.angle = (3 * PI - self.angle) % (2 * PI) - ((PI / 2 - (self.angle % (PI / 2))) * ecc_a)

                self.speed += self.game_state.stroke_speed
                return 0
            else:
                return 2

        elif self.x >= self.game_state.play_area_x + self.game_state.play_area_width - self.width:
            if self.y + self.height >= self.game_state.paddle_b.y \
               and self.y <= self.game_state.paddle_b.y + self.game_state.paddle_height:

                self.x = self.game_state.play_area_x + self.game_state.play_area_width - self.width
                if self.angle == 0:
                    self.angle = PI + random.randint(-1, 1) * DEG
                else:
                    self.angle = (3 * PI - self.angle) % (2 * PI) - ((PI / 2 - (self.angle % (PI / 2))) * ecc_b)

                self.speed += self.game_state.stroke_speed
                return 0
            else:
                return 1

    def draw(self):
        pygame.draw.rect(self.game_display, self.color, [self.x, self.y, self.width, self.height])
