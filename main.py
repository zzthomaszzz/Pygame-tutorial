import pygame

# blit function means showing pictures
# pygame.image.load() - You load the image

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Tutorial mode")
walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
              pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
              pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
             pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
             pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0

    def draw(self, win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if self.left:
            win.blit(walk_left[self.walk_count // 3], (int(self.x), int(self.y)))
            self.walk_count += 1
        elif self.right:
            win.blit(walk_right[self.walk_count // 3], (int(self.x), int(self.y)))
            self.walk_count += 1
        else:
            win.blit(char, (int(self.x), int(self.y)))


# function


def redraw():
    win.blit(bg, (0, 0))
    man.draw(win)
    pygame.display.update()


# Main
man = Player(300, 410, 64, 64)
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
    elif keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    else:
        man.right = False
        man.left = False
        man.walk_count = 0
    if not man.jump:
        if keys[pygame.K_SPACE]:
            man.jump = True
            man.right = False
            man.left = False
            man.walk_count = 0
    else:
        if man.jump_count >= -10:
            neg = 1
            if man.jump_count < 0:
                neg = -1
            man.y -= (man.jump_count ** 2) * 0.5 * neg
            man.jump_count -= 1
        else:
            man.jump = False
            man.jump_count = 10
    redraw()
pygame.quit()
