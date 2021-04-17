from pygame import*


run=True
lost=0
finish=False



font.init()
font1=font.SysFont('Arial', 80)
font2=font.SysFont('Arial', 36)
lose=font1.render('YOU LOSE!', 1,(180,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()

        self.image=transform.scale(image.load(player_image), (size_x, size_y))
        self.speed=player_speed

        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):                        
    def update(self):
        keys=key.get_pressed()
        if keys[K_SPACE] and self.rect.y<20:
            self.rect.y-=20

        if self.rect.y<500:
            self.rect.y-=1

class Enemy(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        global lost
        if self.rect.x> 0:
            lost=lost+1
            self.x=650
            self.rect.y = 500

player=Player('krug.png',10, 30,30,30,5)
enemy=Enemy('kyb.png',650,20,30,30,5)
enemies=sprite.Group()
enemies.add(enemy)





window=display.set_mode((700, 500))


while run==True:
    for e in event.get():
        if e.type == QUIT:
            run=False
    if finish != True:
        enemies.draw(window)
        player.reset()

        enemies.update()
        player.update()

        floor.draw()
        
        if sprite.collide_rect(player, enemies):
            window.blit(lose)
            finish=True


            


    display.update()
    