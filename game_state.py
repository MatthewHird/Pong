class GameState:
    def __init__(self, display_width, display_height):
        self.ball_angle_init = 0.35
        self.ball_speed_init = 5
        self.paddle_speed = 5
        self.stroke_speed = 0.5
        self.paddle_aim = 0.75
        
        self.margin_width = 0.04 * display_width
        self.margin_height = 0.04 * display_width
        self.score_area_width = 0.08 * display_width
        self.score_area_height = 2 * self.margin_height
        self.border_width = display_width - 2 * self.margin_width
        self.border_height = 0.016 * display_width
        self.play_area_width = display_width - 2 * self.margin_width
        self.play_area_height = display_height - 4 * self.margin_height - self.score_area_height
        self.divider_width = 0.008 * display_width
        self.divider_height = self.play_area_height / 20.95
        
        self.paddle_height = 0.12 * display_width
        self.paddle_width = 0.016 * display_width
        self.ball_height = 0.016 * display_width
        self.ball_width = 0.016 * display_width
        
        # add '- [item_dimension] / 2' to self.centre the item
        self.centre_x = self.play_area_width / 2 + self.margin_width
        self.centre_y = self.margin_height + self.score_area_height + self.play_area_height / 2
         
        self.play_area_x = self.margin_width
        self.play_area_y = self.margin_height + self.score_area_height
        self.score_area_a_x = self.margin_width
        self.score_area_a_y = self.margin_height / 2
        self.score_area_b_x = self.margin_width + self.play_area_width - self.score_area_width
        self.score_area_b_y = self.margin_height / 2
        self.border_top_x = self.margin_width
        self.border_top_y = self.play_area_y - self.border_height
        self.border_bottom_x = self.margin_width
        self.border_bottom_y = self.play_area_y + self.play_area_height
        self.divider_start_x = self.centre_x - self.divider_width / 2
        self.divider_start_y = self.play_area_y
        
        self.paddle_a_x_init = self.margin_width - self.paddle_width
        self.paddle_a_y_init = self.centre_y - self.paddle_height / 2
        self.paddle_b_x_init = self.margin_width + self.play_area_width
        self.paddle_b_y_init = self.centre_y - self.paddle_height / 2
        self.ball_x_init = self.centre_x - self.ball_width / 2
        self.ball_y_init = self.centre_y - self.border_height / 2
        
        self.score_count_a = 0
        self.score_count_b = 0
        
        self.quit_game = False
        self.paddle_a_up = False
        self.paddle_a_down = False
        self.paddle_b_up = False
        self.paddle_b_down = False
        
        self.paddle_a = None
        self.paddle_b = None
        self.ball = None
        
        self.clock = None
        self.game_display = None
        
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        
        self.font_type = None
        self.large_font = 50
        self.sys_font = False
