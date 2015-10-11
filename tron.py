import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1003))

class LightBike(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/light3.gif')
        self.rect = self.image.get_rect()
        self.prev_pos = []
        self.speed = 12
        self.direction = -2
        self.images = [pygame.image.load('./images/light1.gif'),
                        pygame.image.load('./images/light2.gif'),
                        pygame.image.load('./images/light3.gif'),
                        pygame.image.load('./images/light4.gif')
                        ]
        self.dead = 0
        self.acceleration = 0

    def update(self):

        self.x = self.rect.center[0]
        self.y = self.rect.center[1]

        if (self.x, self.y) in self.prev_pos and self.direction is not -2:
            self.x = 100
            self.y = 100
            self.rect.center = (self.x, self.y)
            self.prev_pos = []
            self.direction = -2

        self.prev_pos.append(self.rect.center)
        if len(self.prev_pos) > 1:
            pygame.draw.aalines(screen, (238, 89, 0), False, self.prev_pos)
        if len(self.prev_pos) > 100:
            self.prev_pos.pop(0)

        pressed_keys = pygame.key.get_pressed()
        left_key = pressed_keys[pygame.K_LEFT]
        right_key = pressed_keys[pygame.K_RIGHT]
        down_key = pressed_keys[pygame.K_DOWN]
        up_key = pressed_keys[pygame.K_UP]

        if (left_key is 0 and
            right_key is 0 and
            down_key is 0 and
            up_key is 0
            ):
                print 'same direction'

        if left_key:
            self.direction = pygame.K_LEFT
        elif right_key:
            self.direction = pygame.K_RIGHT
        elif down_key:
            self.direction = pygame.K_DOWN
        elif up_key:
            self.direction = pygame.K_UP

        if self.direction is pygame.K_RIGHT:
            self.moveright()
            self.image = self.images[2]
        elif self.direction is pygame.K_DOWN:
            self.movedown()
            self.image = self.images[3]
        elif self.direction is pygame.K_LEFT:
            self.moveleft()
            self.image = self.images[1]
        elif self.direction is pygame.K_UP:
            self.moveup()
            self.image = self.images[0]

    def movedown(self):
        self.rect.centery += self.speed
    def moveup(self):
        self.rect.centery -= self.speed
    def moveleft(self):
        self.rect.centerx -= self.speed
    def moveright(self):
        self.rect.centerx += self.speed

def main():
    lb = LightBike()
    Sprites = pygame.sprite.Group(lb)
    pygame.mixer.music.load('./music/music.mp3')
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    while True:
        clock.tick(40)
        pygame.mouse.set_visible(False)

        if lb.dead:
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        if lb.rect.centery >= screen.get_width():
            lb.rect.centery = screen.get_width()
        if lb.rect.centerx >= screen.get_width():
            lb.rect.centerx = screen.get_width()
        if lb.rect.centery <= 0:
            lb.rect.centery = 0
        if lb.rect.centerx <= 0:
            lb.rect.centerx = 0
        bgi = pygame.image.load('./images/bg.gif')
        screen.blit(bgi, (0, 0))
        Sprites.update()
        Sprites.draw(screen)
        pygame.display.flip()
    # return mouse cursor
    pygame.mouse.set_visible(True)
if __name__ == "__main__":
    main()
