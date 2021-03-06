import pygame
import random

pygame.init()

COLORS = (
    (255, 255, 255),    # white
    (255, 165, 0),  # orange
    (0, 0, 0),   # black
    (174, 178, 178)     # gray
)

screen = width, height = 600, 800
display = pygame.display.set_mode(screen)
pygame.display.set_caption("Race!")


class Car:
    def __init__(self):
        self.x = (width * 0.45)
        self.x_change = 0
        self.y = (height * 0.8)
        self.carImg = pygame.image.load('Front_view_Car_clipart.png')    # load works

    def car(self, x, y):
        display.blit(self.carImg, (x, y))


class Cones:
    def __init__(self):
        self.cones = [
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
            [random.randint(620, 780), -50],
        ]

    def draw(self):
        pygame.draw.lines(screen, COLORS[1], True, [self.cones[0], self.cones[0][0] + 15, self.cones[0][1] + 10, self.cones[0][0] - 15, self.cones[0][1] + 15], 3)

    def change(self):
        pass


def background():
    pygame.draw.rect(display, COLORS[3], (0, -1000, 20, 2000))
    pygame.draw.rect(display, COLORS[3], (580, -1000, 20, 2000))

car = Car()
cones = Cones()

clock = pygame.time.Clock()
FPS = 60

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car.x_change += 3
            if event.key == pygame.K_LEFT:
                car.x_change += -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                car.x_change += -3
            elif event.key == pygame.K_LEFT:
                car.x_change += 3

    car.x += car.x_change
    cones.cones[0][1] -= 1

    display.fill(COLORS[0])
    background()
    car.car(car.x, car.y)
    cones.draw()
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()
