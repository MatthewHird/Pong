class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def hover(self, mouse_x, mouse_y):
        if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
            return True
        else:
            return False
