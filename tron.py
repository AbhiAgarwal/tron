import pygame

pygame.init()
screen = pygame.display.set_mode((1000,1003))

class LightBike(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('light3.gif')
        self.rect = self.image.get_rect()
        self.prev_pos = []
        self.speed = 12
        
    def update(self):
        self.x = 100
        self.y = 100
        self.prev_pos.append(self.rect.center)
        if len(self.prev_pos) > 1:
            pygame.draw.aalines(screen,(238,89,0),False,self.prev_pos)
        if len(self.prev_pos) > 100:
            self.prev_pos.pop(0)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.moveright()
                self.image = pygame.image.load('light3.gif')
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
                self.movedown()
                
                self.image = pygame.image.load('light4.gif')
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
                self.moveleft()
                
                self.image = pygame.image.load('light2.gif')
        elif pygame.key.get_pressed()[pygame.K_UP]:
                self.moveup()
                
                self.image = pygame.image.load('light1.gif')
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
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    while True:
        clock.tick(40)
        pygame.mouse.set_visible(False)
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
        bgi = pygame.image.load('BlackBackground.gif')
        screen.blit(bgi,(0,0))
        Sprites.update()
        Sprites.draw(screen)
        pygame.display.flip()
    #return mouse cursor
    pygame.mouse.set_visible(True)
if __name__ == "__main__":
    main()
