import pygame as pg
import random

WIN_WIDTH = 1000
WIN_HEIGHT = 800

window = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


class Enemy:
    def __init__(self, img, x, y):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.hp = 3

    def update(self, drawx, drawy):
        if self.hp <= 0:
            enemies.remove(enemy)

        if pg.sprite.collide_rect(self, player):
            player.hp -= 1
            enemies.remove(self)

        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed

        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed

        window.blit(self.img, (drawx, drawy))


class Bullet:
    def __init__(self, img, speedx, speedy):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.speedx = speedx
        self.speedy = speedy

    def update(self, drawx, drawy):
        for enemy in enemies:
            if pg.sprite.collide_rect(self, enemy):
                bullets.remove(self)
                enemy.hp -= 1

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x > player.rect.x+500 or self.rect.x < player.rect.x-500 or self.rect.y < player.rect.y-400 or self.rect.y > player.rect.y+400:
            bullets.remove(self)

        window.blit(self.img, (drawx, drawy))


class Object:
    def __init__(self, x, y, img, transparensy):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tr = transparensy

    def update(self, x, y):
        window.blit(self.img, (x, y))


class Player:
    def __init__(self, x, y, img):
        self.speed = 5
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0
        self.hp = 5

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed
            for wall in objects:
                if wall.tr:
                    if pg.sprite.collide_rect(self, wall):
                        self.rect.y += self.speed

        if keys[pg.K_a]:
            self.rect.x -= self.speed
            for wall in objects:
                if wall.tr:
                    if pg.sprite.collide_rect(self, wall):
                        self.rect.x += self.speed

        if keys[pg.K_s]:
            self.rect.y += self.speed
            for wall in objects:
                if wall.tr:
                    if pg.sprite.collide_rect(self, wall):
                        self.rect.y -= self.speed

        if keys[pg.K_d]:
            self.rect.x += self.speed
            for wall in objects:
                if wall.tr:
                    if pg.sprite.collide_rect(self, wall):
                        self.rect.x -= self.speed

        window.blit(self.img, (WIN_WIDTH//2, WIN_HEIGHT//2))


map = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', 't', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', 't', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', 't', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', 't', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', 't', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', 't', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', 't', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', 't', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', 't', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

player = Player(150, 150, pg.image.load('player.png'))

objects = []
enemies = []

for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == '*':
            object = Object(x * 100, y * 100, pg.image.load('floor.png'), 0)
            objects.append(object)
        elif map[y][x] == 't':
            object = Object(x * 100, y * 100, pg.image.load('terrain.png'), 0)
            objects.append(object)
        elif map[y][x] == '#':
            object = Object(x * 100, y * 100, pg.image.load('wall.png'), 1)
            objects.append(object)


clock = pg.time.Clock()
FPS = 30

bullets = []

game = True
while game:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mousepos = pg.mouse.get_pos()
            mx = mousepos[0]
            my = mousepos[1]

            xdiff = mx - WIN_WIDTH//2
            ydiff = my - WIN_HEIGHT//2

            all = abs(xdiff) + abs(ydiff)

            bulx = 10 * (xdiff / all)
            buly = 10 * (ydiff / all)

            bullet = Bullet(pg.image.load('bullet.png'), bulx, buly)
            bullets.append(bullet)

    window.fill('black')

    if len(enemies) < 20:
        for i in range(20 - len(enemies)):
            enemy = Enemy(pg.image.load('zombie.png'), random.randint(200, 4000 - 200), random.randint(200, 3200 - 200))
            enemies.append(enemy)

    playerx = player.rect.x // 100
    playery = player.rect.y // 100

    for object in objects:
        if (player.rect.x-500 <= object.rect.x+100 <= player.rect.x+500) or (player.rect.x-500 <= object.rect.x <= player.rect.x+500):
            if (player.rect.y-400 <= object.rect.y+100 <= player.rect.y + 400) or (player.rect.y-400 <= object.rect.y <= player.rect.y + 400):
                object.update(object.rect.x-(player.rect.x-500), object.rect.y-(player.rect.y-400))

    for enemy in enemies:
        if player.rect.x-500 <= enemy.rect.x <= player.rect.x+500:
            if player.rect.y-400 <= enemy.rect.y <= player.rect.y+400:
                enemy.update(enemy.rect.x-(player.rect.x-500), enemy.rect.y-(player.rect.y-400))

    for bullet in bullets:
        if player.rect.x - 500 <= bullet.rect.x <= player.rect.x + 500:
            if player.rect.y - 400 <= bullet.rect.y <= player.rect.y + 400:
                bullet.update(bullet.rect.x - (player.rect.x - 500), bullet.rect.y - (player.rect.y - 400))

    pg.draw.rect(window, (255, 0, 0), (0, 0, player.hp*20, 10))

    player.update()

    if player.hp <= 0:
        game = False

    pg.display.flip()
