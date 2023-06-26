from time import sleep
import pygame
pygame.init()

###

class Game():
    def __init__(self):
        self.slide = 1
        self.stroka = 1

class Img():
    def __init__(self, x, y, img, w, h):
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (w, h))
        self.x = x
        self.y = y
        self.rect = self.img.get_rect()
    def show(self, win):
        win.blit(self.img, self.rect)
    def delete(self):
        del self.img

def scremer(x, y, img, w, h, win):
    img = pygame.image.load(img)
    img = pygame.transform.scale(img, (w, h))
    rect = img.get_rect()
    rect.x = x
    rect.y = y
    a = 0
    while a != 5:
        win.blit(fon4, (0, 0))
        win.blit(img, rect)
        rect.x += 5
        rect.y += 5
        w += 5
        h += 5

def settext(a, b, c, x, y):
    font = pygame.font.Font('font.ttf', a)
    text_go = font.render(b, 1, c)
    text_rect = text_go.get_rect()
    text_rect.center = (x // 2, y)
    win.blit(text_go, text_rect)

def game_begin(): #начальная  страница
    win.blit(fon1, (0, 0))
    f1 = settext(80, 'Не пейте много пива на ночь.', (150, 150, 150), 1500, 150)
    f1_1 = settext(70, 'Начать - пробел', (150, 150, 150), 1500, 400)
    f1_2 = settext(20, 'Внимание! В игре присутствуют скримеры!', (150, 150, 150), 1500, 680)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        game.slide += 1
        sleep(0.5)
        del f1
        del f1_1
        del f1_2

def slide2(): #первая развилка
    win.blit(fon2, (0,0))
    if game.stroka == 1:
        f2 = settext(30, 'Вы очнулись в страшной комнате.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f2
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 2:
        f3 = settext(30, 'Последнее что вы помните, это большая кружка вкусного пива.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f3
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 3:
        f4 = settext(30, 'Зря вы много выпили.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f4
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 4:
        shoot_music8.play()
        f5 = settext(30, 'Вы поднимаетесь с жесткой кровати.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f5
            game.stroka += 1
            shoot_music8.stop()
            sleep(0.5)
    elif game.stroka == 5:
        f6 = settext(30, 'Ваши действия: 1 - подойти к окну, 2 - проверить дверь.', (150, 150, 150), 1500, 70)
        f6_1 = settext(10, '4 - залезть под кровать.', (30, 30, 30), 2100, 550)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            game.slide += 1
        elif keys[pygame.K_2]:
            game.slide += 3
        elif keys[pygame.K_4]:
            game.slide += 13
        del f6

def slide3_1(): #развилка 1; вариант развития 1
    win.blit(fon3, (0, 0))
    if game.stroka == 5:
        shoot_music3.play()
        f7 = settext(30, 'Вы подошли к окну.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f7
            game.stroka += 1
            game.slide += 1
            shoot_music3.stop()
            sleep(0.5)

def slide3_2(): #развилка 1; вариант 1; продолжение
    win.blit(fon4, (0, 0))
    if game.stroka == 6:
        shoot_music5.play()
        f8 = settext(30, 'На улице шел дождь.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f8
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 7:
        shoot_music5.play()
        f9 = settext(30, 'Вы наблюдаете за жизнью одинокой улицы.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f9
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 8:
        shoot_music5.play()
        f10 = settext(30, 'Нормальные люди сейчас спят в своей теплой, мягкой кроватке.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f10
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 9:
        shoot_music5.play()
        f11 = settext(30, 'А вы даже не знаете, где находитесь.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f11
            game.stroka += 1
            shoot_music5.stop()
            sleep(0.5)
    elif game.stroka == 10:
        shoot_music2.play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 11:
        shoot_music5.play()
        f12 = settext(30, 'Что это было?', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f12
            win.blit(fon4, (0, 0))
            shoot_music5.stop()
            game.stroka += 1
            shoot_music1.play()
            sleep(0.5)
    elif game.stroka == 12:
        img2 = Img(0, 0, 'screemer.jpeg', 1500, 700)
        img2.show(win)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            img2.delete()
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 13:
        win.blit(fon3, (0,0))
        pygame.mixer.music.stop()
        shoot_music.play()
        f13 = settext(30, 'Вы проиграли.', (150, 150, 150), 1500, 70)

def slide4_1(): #развилка 1; вариант развития 2
    win.blit(fon3, (0, 0))
    if game.stroka == 5:
        shoot_music3.play()
        f14 = settext(30, 'Вы подошли к двери.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f14
            game.stroka += 1
            game.slide += 1
            shoot_music3.stop()
            sleep(0.5)

def slide4_2(): #развилка 1; вариант 1; продолжение
    win.blit(fon5, (0, 0))
    if game.stroka == 6:
        f15 = settext(30, 'Дверь встретила вас гробовым молчанием.', (35, 35, 35), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f15
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 7:
        f16 = settext(30, 'Казалось, её совершенно не интересовало ваше присутствие.', (35, 35, 35), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f16
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 8:
        f17 = settext(30, 'Ваши действия: 1 - посмотреть в глазок, 2 - подергать ручку.', (35, 35, 35), 1500, 70)
        f17_1 = settext(10, '9 - заорать.', (180, 180, 180), 2000, 600)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            game.slide += 1
        elif keys[pygame.K_2]:
            game.slide += 3
        elif keys[pygame.K_9]:
            game.slide += 15

def slide5_1():
    win.blit(fon3, (0, 0))
    if game.stroka == 8:
        shoot_music8.play()
        f18 = settext(30, 'Вы решили посмотреть в глазок.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f18
            game.stroka += 1
            game.slide += 1
            shoot_music8.stop()
            sleep(0.5)

def slide5_2(): #развилка 1; вариант 2; продолжение
    win.blit(fon6, (0, 0))
    if game.stroka == 9:
        shoot_music7.play()
        f19 = settext(30, 'Посмотря в глазок, вы с ужасом обнаруживаете...', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f19
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 10:
        f20 = settext(30, '...что на, как минимум, 3 кв. метра вы не одни.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f20
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 11:
        f21 = settext(30, 'Что за пиво вы выпили?', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f21
            game.stroka += 1
            shoot_music7.stop()
            shoot_music6.play()
            sleep(0.5)
    elif game.stroka == 12:
        img2 = Img(0, 0, 'scrm.jpeg', 1500, 700)
        img2.show(win)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            img2.delete()
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 13:
        win.blit(fon3, (0,0))
        pygame.mixer.music.stop()
        shoot_music.play()
        f22 = settext(30, 'Вы проиграли.', (150, 150, 150), 1500, 70)

def slide6_1():
    win.blit(fon3, (0, 0))
    if game.stroka == 8:
        shoot_music4.play()
        f18 = settext(30, 'Вы решили подергать ручку.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f18
            game.stroka += 1
            game.slide += 1
            sleep(0.5)

def slide6_2(): #развилка 1; вариант 2; продолжение
    win.blit(fon5, (0, 0))
    if game.stroka == 9:
        f19 = settext(30, 'Дверь не хотела поддаватся.', (35, 35, 35), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f19
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 10:
        f20 = settext(30, 'Видимо, она была заперта. Но где ключ?', (35, 35, 35), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f20
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 11:
        f21 = settext(30, 'Может под ковриком?', (35, 35, 35), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f21
            game.stroka += 1
            game.slide += 1
            sleep(0.5)

def slide6_3():
    win.blit(fon3, (0, 0))
    if game.stroka == 12:
        f22 = settext(30, 'Вы посмотрели вниз.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f22
            game.stroka += 1
            game.slide += 1
            sleep(0.5)

def slide6_4(): #развилка 1; вариант 2; продолжение
    win.blit(fon7, (0, 0))
    if game.stroka == 13:
        f23 = settext(30, 'Какой безвкусный, пыльный и липкий ковёр.', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f23
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 14:
        shoot_music8.play()
        f23 = settext(30, 'Но под ним действительно оказался ключ.', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f23
            game.stroka += 1
            game.slide += 1
            shoot_music8.stop()
            sleep(0.5)

def slide6_5():
    win.blit(fon3, (0, 0))
    if game.stroka == 15:
        shoot_music9.play()
        f24 = settext(30, 'Вы вставили ключ в замок и покрутили несколько раз.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f24
            game.stroka += 1
            shoot_music9.stop()
            sleep(0.5)
    elif game.stroka == 16:
        shoot_music10.play()
        f25 = settext(30, 'Дверь медленно открылась...', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f25
            game.stroka += 1
            game.slide += 1
            shoot_music10.stop()
            sleep(0.5)

def slide6_6():
    win.blit(fon8, (0, 0))
    if game.stroka == 17:
        shoot_music7.play()
        f26 = settext(30, 'За ней никого?..', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f26
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 18:
        f27 = settext(30, 'Серьезно?', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f27
            game.stroka += 1
            shoot_music7.stop()
            shoot_music1.play()
            sleep(0.5)
    elif game.stroka == 19:
        img2 = Img(0, 0, 'screemer.jpeg', 1500, 700)
        img2.show(win)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            img2.delete()
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 20:
        win.blit(fon3, (0,0))
        pygame.mixer.music.stop()
        shoot_music.play()
        f28 = settext(30, 'Вы проиграли.', (150, 150, 150), 1500, 70)

def slide7_1():
    win.blit(fon3, (0, 0))
    if game.stroka == 5:
        shoot_music8.play()
        f29 = settext(30, 'Вы решили залезть под кровать.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f29
            game.stroka += 1
            game.slide += 1
            shoot_music8.stop()
            sleep(0.5)

def slide7_2(): #развилка 1; вариант 2; продолжение
    win.blit(fon9, (0, 0))
    if game.stroka == 6:
        f100 = settext(30, 'Тут было очень пыльно и грязно.', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f100
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 7:
        f100 = settext(30, 'Мысленно вы посочувствовали всем подкроватным монстрам.', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f100
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 8:
        f100 = settext(30, 'Вопрос, зачем вы сюда залезли?', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f100
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 9:
        f100 = settext(30, 'Во-первых, вы же ведь уже не ребенок, иначе бы здесь не оказались.', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f100
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 10:
        shoot_music7.play()
        f100 = settext(30, 'Во-вторых, а вдруг здесь есть подкроватный монстр?', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f100
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 11:
        f100 = settext(30, 'Тогда вы попали к нему прямо в лапы.', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f100
            game.stroka += 1
            shoot_music7.stop()
            sleep(0.5)
    elif game.stroka == 12:
        shoot_music10.play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game.stroka += 1
            shoot_music10.stop()
            sleep(0.5)
    elif game.stroka == 13:
        shoot_music11.play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game.stroka += 1
            shoot_music11.stop()
            sleep(0.5)
    elif game.stroka == 14:
        shoot_music7.play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game.stroka += 1
            shoot_music7.stop()
            sleep(0.5)
    elif game.stroka == 15:
        shoot_music3.play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game.stroka += 1
            shoot_music3.stop()
            sleep(0.5)
    elif game.stroka == 16:
        shoot_music10.play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game.stroka += 1
            shoot_music10.stop()
            sleep(0.5)
    elif game.stroka == 17:
        shoot_music7.play()
        f100 = settext(30, 'В комнату кто-то зашел.', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f100
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 18:
        shoot_music7.play()
        f100 = settext(30, 'И вышел.', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f100
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 19:
        shoot_music7.play()
        f100 = settext(30, 'А вдруг вы в чужой квартире?', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f100
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 20:
        shoot_music7.play()
        f100 = settext(30, 'Хотя, что значит "вдруг"?', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f100
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 21:
        shoot_music7.play()
        f100 = settext(30, 'Скорее всего это был хозяин квартиры.', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f100
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 22:
        shoot_music7.play()
        f100 = settext(30, 'Ваши действия: 1 - вылезти из под кровати, 2 - подождать', (250, 250, 250), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            game.slide += 1
            del f100
            shoot_music7.stop()
        elif keys[pygame.K_2]:
            game.slide += 3
            del f100
            shoot_music7.stop()

def slide7_3():
    win.blit(fon3, (0, 0))
    if game.stroka == 22:
        shoot_music8.play()
        f29 = settext(30, 'Вы решили вылезти из под кровати.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f29
            game.stroka += 1
            game.slide += 1
            shoot_music8.stop()
            sleep(0.5)

def slide7_4():
    win.blit(fon2, (0, 0))
    if game.stroka == 23:
        f21 = settext(30, 'Вроде никого нет.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f21
            game.stroka += 1
            shoot_music6.play()
            sleep(0.5)
    elif game.stroka == 24:
        img2 = Img(0, 0, 'scrm.jpeg', 1500, 700)
        img2.show(win)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            img2.delete()
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 25:
        win.blit(fon3, (0,0))
        pygame.mixer.music.stop()
        shoot_music.play()
        f22 = settext(30, 'Вы проиграли.', (150, 150, 150), 1500, 70)

def slide8_1():
    win.blit(fon3, (0, 0))
    if game.stroka == 22:
        f29 = settext(30, 'Вы решили остаться под кроватью.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f29
            game.stroka += 1
            shoot_music12.play()
            sleep(0.5)
    elif game.stroka == 23:
        f29 = settext(30, 'Это музыкальная шкатулка играет?..', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f29
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 24:
        f29 = settext(30, '...', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f29
            game.stroka += 1
            game.slide +=1
            shoot_music12.stop()
            sleep(0.5)

def slide8_2():
    win.blit(fon10, (0, 0))
    if game.stroka == 25:
        pygame.mixer.music.stop()
        shoot_music13.play()
        f29 = settext(30, '...', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f29
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 26:
        f29 = settext(30, 'Кажется вы уснули..', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f29
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 27:
        f29 = settext(30, 'Но вы же уснули под кроватью, а не на ней.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f29
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 28:
        f29 = settext(30, 'Кто-то вас перетащил? Владелец квартиры?', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f29
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 29:
        f29 = settext(30, 'Но вы точно знаете одну вещь:..', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f29
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 30:
        f29 = settext(30, '... вы больше не будете пить много пива на ночь.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f29
            game.stroka += 1
            shoot_music13.stop()
            sleep(0.5)
    elif game.stroka == 31:
        win.blit(fon11, (0, 0))
        shoot_music14.play()

def slide9_1():
    win.blit(fon3, (0, 0))
    if game.stroka == 8:
        shoot_music15.play()
        f29 = settext(30, 'Вы решили заорать на весь дом.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f29
            game.stroka += 1
            shoot_music15.stop()
            sleep(0.5)
    elif game.stroka == 9:
        shoot_music11.play()
        f29 = settext(30, 'За дверью что-то зашевелилось...', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            shoot_music11.stop()
            del f29
            shoot_music1.play()
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 10:
        img2 = Img(0, 0, 's.jpg', 1500, 700)
        img2.show(win)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            img2.delete()
            shoot_music1.stop()
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 11:
        win.blit(fon3, (0,0))
        pygame.mixer.music.stop()
        shoot_music.play()
        f28 = settext(30, 'Вы проиграли, но вы открыли секретную концовку.', (150, 150, 150), 1500, 70)
###

game = Game()
run = True
fps = 30
clock = pygame.time.Clock()
win = pygame.display.set_mode((1500, 700))
slaide = 1
fon1 = pygame.image.load('b.jpeg')
fon1 = pygame.transform.scale(fon1, (1500, 700))
fon2 = pygame.image.load('po.jpg')
fon2 = pygame.transform.scale(fon2, (1500, 700))
fon3 = pygame.image.load('ch.png')
fon3 = pygame.transform.scale(fon3, (1500, 700))
fon4 = pygame.image.load('okno.jpg')
fon4 = pygame.transform.scale(fon4, (1500, 700))
fon5 = pygame.image.load('dver.jpeg')
fon5 = pygame.transform.scale(fon5, (1500, 700))
fon6 = pygame.image.load('glaz.jpeg')
fon6 = pygame.transform.scale(fon6, (1500, 700))
fon7 = pygame.image.load('kover.jpg')
fon7 = pygame.transform.scale(fon7, (1500, 700))
fon8 = pygame.image.load('dv.jpg')
fon8 = pygame.transform.scale(fon8, (1500, 700))
fon9 = pygame.image.load('krov.jpg')
fon9 = pygame.transform.scale(fon9, (1500, 700))
fon10 = pygame.image.load('po2.jpg')
fon10 = pygame.transform.scale(fon10, (1500, 700))
fon11 = pygame.image.load('win.jpeg')
fon11 = pygame.transform.scale(fon11, (1500, 700))


pygame.mixer.music.load('osnov.mp3')
pygame.mixer.music.play(-1)
shoot_music = pygame.mixer.Sound('proig.ogg')
shoot_music1 = pygame.mixer.Sound('screm1.ogg')
shoot_music2 = pygame.mixer.Sound('stuk.ogg')
shoot_music3 = pygame.mixer.Sound('zvukshagov.ogg')
shoot_music4 = pygame.mixer.Sound('zakryitoydveri.ogg')
shoot_music5 = pygame.mixer.Sound('zvykd.ogg')
shoot_music6 = pygame.mixer.Sound('krik.ogg')
shoot_music7 = pygame.mixer.Sound('heartbeat.ogg')
shoot_music8 = pygame.mixer.Sound('ostorojnoe-shurshanie-v-poiskah-nujnoy-veschi.ogg')
shoot_music9 = pygame.mixer.Sound('zvuk-kljuchej-v-zamochnoj-skvazhine.ogg')
shoot_music10 = pygame.mixer.Sound('scrip.ogg')
shoot_music11 = pygame.mixer.Sound('post.ogg')
shoot_music12 = pygame.mixer.Sound('muzykalnaya-shkatulka-z_uk.ogg')
shoot_music13 = pygame.mixer.Sound('morning_birds_insects.ogg')
shoot_music14 = pygame.mixer.Sound('kirya-pomedorkas-adventures-ost-z_uk-pobedy.ogg')
shoot_music15 = pygame.mixer.Sound('3.ogg')



###

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if game.slide == 1:
        game_begin()
    elif game.slide == 2:
        slide2()
    elif game.slide == 3:
        slide3_1()
    elif game.slide == 4:
        slide3_2()
    elif game.slide == 5:
        slide4_1()
    elif game.slide == 6:
        slide4_2()
    elif game.slide == 7:
        slide5_1()
    elif game.slide == 8:
        slide5_2()
    elif game.slide == 9:
        slide6_1()
    elif game.slide == 10:
        slide6_2()
    elif game.slide == 11:
        slide6_3()
    elif game.slide == 12:
        slide6_4()
    elif game.slide == 13:
        slide6_5()
    elif game.slide == 14:
        slide6_6()
    elif game.slide == 15:
        slide7_1()
    elif game.slide == 16:
        slide7_2()
    elif game.slide == 17:
        slide7_3()
    elif game.slide == 18:
        slide7_4()
    elif game.slide == 19:
        slide8_1()
    elif game.slide == 20:
        slide8_2()
    elif game.slide == 21:
        slide9_1()


    pygame.display.update()
    clock.tick(fps)