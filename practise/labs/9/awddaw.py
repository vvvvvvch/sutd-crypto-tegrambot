import pygame


WIDTH = 1000
HEIGHT = 1000

running = True
FPS = 24
clock = pygame.time.Clock()



a = [1, 2, 3, 4, 5, 6, 7]
b = [1, 2, 3, 4, 5, 6, 7]
# 1 взвешивание
# d = random.randrange(1,7)
try:
    d = int(input('введите вес недостающей гирьки(от 1 до 7) \n')) - 1
except ValueError:
    print('ТЫ КРИТИН? извини')
    quit()
try:
    b.pop(d)
    if d < 0:
        print('не оно мужик')
        quit()
except IndexError:
    print('не оно мужик')
    quit()
sum1 = sum(a)
sum2 = sum(b)


def first():
    if (sum1 - 4) == sum2: #ne hvataet 4
        return 1
    elif (sum1 - 4) < sum2: #ne hvataet 1-3
        return 2
    elif (sum1 - 4) > sum2: # ne hvataet 5-7
        return 3
if first() == 1:
    def second():
        return 1
elif first() == 2:
    def second():
        if (sum1 - 2) == sum2: #ne hvataet 2
            return 1
        elif (sum1 - 2) < sum2: # ne hvataet 1
            return 2
        else: # ne hvataet 3
            return 3
elif first() == 3:
    def second():
        if (sum1-6) == sum2: #ne hvataet 6
            return 1
        elif (sum1-6) < sum2: #ne hvataet 5
            return 2
        else:
            return 3
print ('\n','\n',first(),'\n',second())



pygame.init()
font = pygame.font.Font('arial_bold.ttf', 40)
text1  = font.render('НЕ ХВАТАЕТ 1 ГРАММ ', False, 'white')
text2  = font.render('НЕ ХВАТАЕТ 2 ГРАММ ', False, 'white')
text3  = font.render('НЕ ХВАТАЕТ 3 ГРАММ ', False, 'white')
text4  = font.render('НЕ ХВАТАЕТ 4 ГРАММ ', False, 'white')
text5  = font.render('НЕ ХВАТАЕТ 5 ГРАММ ', False, 'white')
text6  = font.render('НЕ ХВАТАЕТ 6 ГРАММ ', False, 'white')
text7  = font.render('НЕ ХВАТАЕТ 7 ГРАММ ', False, 'white')
hz = 500
hz2 = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bg = screen.fill((66, 170, 255))
girya_right = pygame.Surface((70, 100))
girya_right.fill((190, 190, 190))
girya_right.set_colorkey((0, 0, 0))
girya_left = pygame.Surface((70, 100))
girya_left.fill((190, 190, 190))
girya_left.set_colorkey((0, 0, 0))
vesi_rigth = pygame.Surface((200, 10))
vesi_rigth.fill((235, 104, 163))
vesi_rigth.set_colorkey((0, 0, 0))
vesi_left = pygame.Surface((200, 10))
vesi_left.fill((235, 104, 163))
square = pygame.Surface((50, 650))
square.fill((135, 70, 42))
vesi = pygame.Surface((700, 30))
vesi.fill((135, 70, 42))
vesi.set_colorkey((0, 0, 0))
angle = 0
vesich = pygame.image.load('1.jpg')
vesich_small = pygame.transform.scale(vesich, (170, 170))
pygame.display.set_caption("ВЕСЫЧ")


while running:

    clock.tick(FPS)
    screen.fill((66, 170, 255))
    pygame.draw.ellipse(screen, (135, 70, 42), (260, 850, 480, 200))
    pygame.draw.ellipse(screen, (112, 60, 42), (300, 850, 400, 120))
    vesi_rotate = pygame.transform.rotate(vesi, angle)
    screen.blit(vesi_rotate, (WIDTH / 2 - int(vesi_rotate.get_width() / 2), HEIGHT / 2 - 130 - int(vesi_rotate.get_height() / 2)))
    screen.blit(square, (475, 250))
    pygame.draw.circle(screen, (235, 104, 163), (500, 200), 120)
    screen.blit(vesich_small, (415, 130))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    if first() == 1 and second() == 1:
        angle = 0
        if angle == 0:
            screen.blit(text4, (260, 10))
            screen.blit(vesi_rigth, (750, 500))
            screen.blit(vesi_left, (20, 500))
            screen.blit(girya_right, (820, hz - 100))
            screen.blit(girya_left, (80, hz - 100))
    elif first() == 2 and second() == 1:
        angle -= 1
        if angle == -35:
            angle = -34
            screen.blit(text2, (260, 10))
        hz += 5
        screen.blit(vesi_rigth, (750, hz))
        if hz == 700:
            hz = 695
        hz2 -= 5
        screen.blit(vesi_rigth, (20, hz2))
        if hz2 == 305:
            hz2 = 310
        screen.blit(girya_right, (820, hz - 95))
        screen.blit(girya_left, (80, hz2 - 105))
    elif first() == 2 and second() == 2:
        angle = 0
        if angle == 0:
            screen.blit(text1, (260, 10))
            screen.blit(vesi_rigth, (750, 500))
            screen.blit(vesi_left, (20, 500))
            screen.blit(girya_right, (820, hz - 100))
            screen.blit(girya_left, (80, hz - 100))
    elif first() == 2 and second() == 3:
        angle -= 1
        if angle == -35:
            angle = -34
            screen.blit(text3, (260, 10))
        hz += 5
        screen.blit(vesi_rigth, (750, hz))
        if hz == 700:
            hz = 695
        hz2 -= 5
        screen.blit(vesi_rigth, (20, hz2))
        if hz2 == 305:
            hz2 = 310
        screen.blit(girya_right, (820, hz - 95))
        screen.blit(girya_left, (80, hz2 - 105))
    elif first() == 3 and second() == 1:
        angle += 1
        if angle == 35:
            angle = 34
            screen.blit(text6, (260, 10))
        hz -= 5
        screen.blit(vesi_rigth, (750, hz))
        if hz == 305:
            hz = 310
        hz2 += 5
        screen.blit(vesi_rigth, (20, hz2))
        if hz2 == 700:
            hz2 = 695
        screen.blit(girya_right, (820, hz - 105))
        screen.blit(girya_left, (80, hz2 - 95))
    elif first() == 3 and second() == 2:
        angle += 1
        if angle == 35:
            angle = 34
            screen.blit(text5, (260, 10))
        hz += 5
        screen.blit(vesi_rigth, (750, hz2))
        if hz == 700:
            hz = 695
        hz2 -= 5
        screen.blit(vesi_rigth, (20, hz))
        if hz2 == 305:
            hz2 = 310
        screen.blit(girya_right, (820, hz2 - 95))
        screen.blit(girya_left, (80, hz - 105))
    elif first() == 3 and second() == 3:
        angle = 0
        if angle == 0:
            screen.blit(text7, (260, 10))
            screen.blit(vesi_rigth, (750, 500))
            screen.blit(vesi_left, (20, 500))
            screen.blit(girya_right, (820, hz - 100))
            screen.blit(girya_left, (80, hz - 100))
    pygame.display.update()