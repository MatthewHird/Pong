import pygame
import time
import math
import random

from window import Window
from game_state import GameState
from menu_state import MenuState
from paddle import Paddle
from ball import Ball
from button import Button

display_width = 1000
display_height = 800

window = Window('Pong', 'pong_icon.png', display_width, display_height)
game_state = GameState(display_width, display_height)
menu_state = MenuState(display_width, display_height)

PI = math.pi
DEG = math.pi / 180


def main():
    window.initiate()
    menu()
    game()


def menu():
    menu_state.button_start = Button('Start', menu_state.button_menu_x, menu_state.button_start_y,
                                     menu_state.button_width, menu_state.button_height)
    menu_state.button_list.append(menu_state.button_start)
    menu_state.button_quit = Button('Quit', menu_state.button_menu_x, menu_state.button_quit_y,
                                    menu_state.button_width, menu_state.button_height)
    menu_state.button_list.append(menu_state.button_quit)

    while not menu_state.quit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                menu_state.mouse_x, menu_state.mouse_y = pygame.mouse.get_pos()
                for button in menu_state.button_list:
                    if button.hover(menu_state.mouse_x, menu_state.mouse_y):
                        if button == menu_state.button_start:
                            game()
                        elif button == menu_state.button_quit:
                            pygame.quit()
                            quit()

        menu_state.mouse_x, menu_state.mouse_y = pygame.mouse.get_pos()

        window.display.fill(game_state.black)
        message_display(menu_state.menu_title, menu_state.title_x, menu_state.title_y, menu_state.title_width,
                        menu_state.title_height, menu_state.font_type, menu_state.title_font, menu_state.sys_font)
        pygame.draw.rect(window.display, game_state.white, [menu_state.bar_x, menu_state.bar_y,
                                                            menu_state.bar_width, menu_state.bar_height])
        for button in menu_state.button_list:
            if button.hover(menu_state.mouse_x, menu_state.mouse_y):
                message_display(button.text, button.x, button.y, button.width, button.height,
                                menu_state.font_type, menu_state.large_font, menu_state.sys_font)
            else:
                message_display(button.text, button.x, button.y, button.width, button.height,
                                menu_state.font_type, menu_state.medium_font, menu_state.sys_font)

        pygame.display.update()
        window.clock.tick(30)


def game():
    game_state.paddle_a = Paddle(window.display, game_state.paddle_a_x_init, game_state.paddle_a_y_init,
                                 game_state.paddle_width, game_state.paddle_height, game_state.white, game_state)
    game_state.paddle_b = Paddle(window.display, game_state.paddle_b_x_init, game_state.paddle_b_y_init,
                                 game_state.paddle_width, game_state.paddle_height, game_state.white, game_state)
    game_state.ball = Ball(window.display, game_state.ball_x_init, game_state.ball_y_init,
                           game_state.ball_width, game_state.ball_height, game_state.white,
                           game_state.ball_speed_init, game_state.ball_angle_init, game_state)

    reset()

    while not game_state.quit_game:
        event_handler()
        update()
        draw()

        pygame.display.update()
        window.clock.tick(60)

    pygame.quit()
    quit()


def paused():
    return 0


def reset():
    game_state.paddle_a.x = game_state.paddle_a_x_init
    game_state.paddle_a.y = game_state.paddle_a_y_init
    game_state.paddle_b.x = game_state.paddle_b_x_init
    game_state.paddle_b.y = game_state.paddle_b_y_init
    game_state.ball.x = game_state.ball_x_init
    game_state.ball.y = game_state.ball_y_init
    game_state.ball.speed = game_state.ball_speed_init
    game_state.ball.angle = (random.choice([game_state.ball_angle_init, PI - game_state.ball_angle_init,
                                            PI + game_state.ball_angle_init, 2 * PI - game_state.ball_angle_init])
                             + random.randint(-5, 5) * DEG) % (2 * PI)
    draw()
    pygame.display.update()
    time.sleep(1)


def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.quit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused()
            elif event.key == pygame.K_a:
                game_state.paddle_a_up = True
            elif event.key == pygame.K_d:
                game_state.paddle_a_down = True
            elif event.key == pygame.K_j:
                game_state.paddle_b_up = True
            elif event.key == pygame.K_l:
                game_state.paddle_b_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                game_state.paddle_a_up = False
            elif event.key == pygame.K_d:
                game_state.paddle_a_down = False
            elif event.key == pygame.K_j:
                game_state.paddle_b_up = False
            elif event.key == pygame.K_l:
                game_state.paddle_b_down = False


def update():
    game_state.paddle_a.update(game_state.paddle_a_up, game_state.paddle_a_down)
    game_state.paddle_b.update(game_state.paddle_b_up, game_state.paddle_b_down)
    has_scored = game_state.ball.update()

    if has_scored == 0:
        return
    elif has_scored == 1:
        goal(1)
    elif has_scored == 2:
        goal(2)


def draw():
    window.display.fill(game_state.black)
    game_state.paddle_a.draw()
    game_state.paddle_b.draw()
    game_state.ball.draw()
    draw_divider()
    pygame.draw.rect(window.display, game_state.white, [game_state.border_top_x, game_state.border_top_y,
                                                        game_state.border_width, game_state.border_height])
    pygame.draw.rect(window.display, game_state.white, [game_state.border_bottom_x, game_state.border_bottom_y,
                                                        game_state.border_width, game_state.border_height])
    message_display(str(game_state.score_count_a), game_state.score_area_a_x, game_state.score_area_a_y,
                    game_state.score_area_width, game_state.score_area_height, game_state.font_type,
                    game_state.large_font, game_state.sys_font)
    message_display(str(game_state.score_count_b), game_state.score_area_b_x, game_state.score_area_b_y,
                    game_state.score_area_width, game_state.score_area_height, game_state.font_type,
                    game_state.large_font, game_state.sys_font)


def goal(x):
    if x == 1:
        game_state.score_count_a += 1
    elif x == 2:
        game_state.score_count_b += 1
    reset()


def message_display(text, x, y, width, height, font_name, font_size, sys_font):
    if sys_font:
        use_font = pygame.font.Font(font_name, font_size)
    else:
        use_font = pygame.font.SysFont(font_name, font_size)
    text_surface, text_rectangle = text_objects(text, use_font)
    text_rectangle.center = ((x + width / 2), (y + height / 2))
    window.display.blit(text_surface, text_rectangle)


def text_objects(text, font):
    text_surface = font.render(text, True, game_state.white)
    return text_surface, text_surface.get_rect()


def draw_divider():
    count = 11
    x = game_state.divider_start_x
    y = game_state.divider_start_y

    while count > 0:
        pygame.draw.rect(window.display, game_state.white, [x, y, game_state.divider_width,
                                                            game_state.divider_height])
        y += 2 * game_state.divider_height
        count -= 1


if __name__ == '__main__':
    main()
