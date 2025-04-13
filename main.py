from pygame import *

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
FPS = 60

class Background:
    def __init__(self, file_path, width, height, start_x):
        self.background = transform.scale(image.load(file_path), (width, height))
        self.rect = self.background.get_rect()
        self.rect.x = start_x

    def update(self):
        self.rect.x -= 5
        if self.rect.width + self.rect.x <= 0:
            self.rect.x = self.rect.width

    def draw(self, screen):
        screen.blit(self.background, (self.rect.x, self.rect.y))


window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

background1 = Background("assets/background.png", WINDOW_WIDTH, WINDOW_HEIGHT, 0)
background2 = Background("assets/background.png", WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH)


clock = time.Clock()

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill((0, 0, 0))

    background1.update()
    background1.draw(window)
    background2.update()
    background2.draw(window)


    display.update()
    clock.tick(FPS)