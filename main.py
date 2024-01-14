from pygame import*
back = (100, 100, 100)
win_height = 500
win_width = 600
window = display.set_mode((win_width, win_height))
window.fill(back)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_scale_x, player_scale_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_scale_x, player_scale_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[k_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[k_s] and self.rect.y< win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[k_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[k_DOWN] and self.rect.y< win_height - 80:
            self.rect.y += self.speed

rocket2 = Player('vfibyf vfplf.png', 4, 30,200,100,150)
rocket1 = Player('bmw cdth[e.png',4, 500,200,100,200)
ball = Player("pngwing.com.png",4, 200, 300 , 70,70)




clock = time.Clock()
FPS = 60
finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game= False

    if finish != True:
        rocket1.reset()
        rocket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)


















