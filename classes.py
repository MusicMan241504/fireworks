import pygame as p
import random as rand
class Rect(p.sprite.Sprite):
    def __init__(self,colour,name = ''):
        self.name = name
        p.sprite.Sprite.__init__(self)
        self.size = rand.randint(2,5)
        self.image = p.Surface([self.size,self.size], p.HWSURFACE)

        self.alpha = 255
        self.image.set_alpha(self.alpha)         #enable rect to be transparent
        
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        
        self.vec = p.math.Vector2()
        
        self.vec.x = rand.uniform(-1,1)
        self.vec.y = rand.uniform(-1,1)
        self.vec = self.vec.normalize()
        self.vec = self.vec*rand.uniform(1,5)
        
    def update(self):
        self.x = self.x - self.vec.x
        self.rect.x = round(self.x)
        
        self.y = self.y - self.vec.y
        self.rect.y = round(self.y)

        self.alpha = self.alpha - 1

        if self.alpha == 0:                     #if invisible kill
            self.kill()
        self.image.set_alpha(self.alpha)
