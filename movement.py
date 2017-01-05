# Eric Lu

import pygame
from pygame import *
import sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Movement - Eric Lu")

    timer = pygame.time.Clock()

    left = right = False
    bg = Surface((32,32))
    bg.convert()
    bg.fill(Color("#000000"))
    entities = pygame.sprite.Group()
    player = Player(32, 32)
    platforms = []

    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "P                       P",
        "PPPPPPPPPPPPPPPPPPPPPPPPP",]
    
    # build the level
    for row in level:
        for col in row:
            if (col == "P"):
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            x += 32
        y += 32
        x = 0

    entities.add(player)

    while True:
        timer.tick(60)
        for e in pygame.event.get():
            
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

            if e.type == KEYDOWN and (e.key == K_LEFT or e.key == K_a):
                left = True
            if e.type == KEYDOWN and (e.key == K_RIGHT or e.key == K_d):
                right = True

            if e.type == KEYUP and (e.key == K_RIGHT or e.key == K_d):
                right = False
            if e.type == KEYUP and (e.key == K_LEFT or e.key == K_a):
                left = False


        # draw background
        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x * 32, y * 32))

        # update player, draw everything else
        player.update(left, right, platforms)
        entities.draw(screen)

        pygame.display.update()

class Entity(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)

class Player(Entity):
    
    def __init__(self, x, y):
        
        Entity.__init__(self)
        self.xvel = 0
        self.image = Surface((32,32))
        self.image.fill(Color("#ff0000"))
        self.image.convert()
        self.rect = Rect(32, 544, 32, 32)

    def update(self, left, right, platforms):
            
        if left:
            self.xvel = -8
            
        if right:
            self.xvel = 8
            
        if not(left or right):
            self.xvel = 0
            
        # increment in x direction
        self.rect.left += self.xvel
        
        # do x-axis collisions
        self.collide(self.xvel, platforms)
        
    def collide(self, xvel, platforms):
        
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                
                if xvel > 0: # Collide Right
                    self.rect.right = p.rect.left
                if xvel < 0: # Collide Left
                    self.rect.left = p.rect.right


class Platform(Entity):
    
    def __init__(self, x, y):
        
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#FF9900"))
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass

if __name__ == "__main__":
    main()
