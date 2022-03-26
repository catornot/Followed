from .block import Block
from pygame.font import Font

class Text(Block):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, (50, 50, 50))
        self.symbol = "d"
        self.font = Font("assets/fonts/oswald.ttf", 25)
        self.text:list = []
    
    def render(self, surface):
        for i, line in enumerate(self.text):
            text_surface = self.font.render(line, True, (255, 255, 255))
            text_surface_3D = self.font.render(line, True, (120, 120, 120))

            text_rect = text_surface.get_rect(center=(self.x, self.y - 16 + text_surface.get_height() * int(i)))

            text_rect_3D = text_rect.copy()
            text_rect_3D.x += 3
            text_rect_3D.y -= 3

            surface.blit(text_surface_3D, text_rect_3D)
            surface.blit(text_surface, text_rect)
    
    def SetText( self, text ):
        self.text = text.split("\n")