from pygame import *
class GameSprite(sprite.Sprite):
    def __int__(self, player_img, x, y, speed, width, heigh):
        super().__init__()
        self.img = transform.scale(image.load(player_img),(width, heigh))
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect_x = x
        self.rect_x = y
    def reset(self):
        nw.blit(self.img, (self.rect_x, self.rect_y))

class Player(GameSprite):
    def right_player(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect_x > 5:
            self.rect_y -= self.speed
        if keys[K_DOWN] and self.rect_y (nw_width - 80):
            self.rect_y += self.speed
    def left_player(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect_x > 5:
            self.rect_y -= self.speed

        if keys[K_s] and self.rect_y (nw_width - 80):
            self.rect_y += self.speed

fon = (0, 0 , 0)
nw_wdth = 600
nw_heigh = 500
nw = display.set_mode((nw_wdth, nw_heigh))
nw.fill(fon)