class MenuState:
    def __init__(self, display_width, display_height):
        self.menu_title = 'PONG'

        self.medium_font = 50
        self.large_font = 60
        self.title_font = 200
        self.font_type = None
        self.sys_font = False

        self.margin_width = 0.05 * display_width
        self.margin_height = 0.03 * display_width
        self.title_width = display_width - 2 * self.margin_width
        self.title_height = display_height / 2 - self.margin_height * 2
        self.button_width = 0.5 * display_width
        self.button_height = 0.1 * display_height

        self.bar_width = self.title_width
        self.bar_height = 0.016 * display_width

        self.title_x = self.margin_width
        self.title_y = self.margin_height
        self.button_menu_x = display_width / 2 - self.button_width / 2
        self.button_quit_y = display_height - self.button_height - self.margin_height * 2
        self.button_start_y = self.button_quit_y - self.button_height - self.margin_height
        self.bar_x = self.margin_width
        self.bar_y = display_height / 2 - self.bar_height / 2

        self.mouse_x = 0
        self.mouse_y = 0
        self.button_start = None
        self.button_quit = None
        self.button_list = []
        self.quit_game = False
