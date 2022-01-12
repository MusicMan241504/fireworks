import pygame as p
import random as rand
import classes as w
p.init()


def setup():
    global all_sprites_list, rects, clock, background
    i = p.display.Info()                                        #get resolution of display
    background = p.display.set_mode([i.current_w,i.current_h],p.HWSURFACE)  #Create pygame window
    all_sprites_list = p.sprite.Group()
    rects = p.sprite.Group()
    
    background.fill([0,0,50])
    all_sprites_list.draw(background)
    p.display.flip()
    clock = p.time.Clock()

def create_rect(x,y):
    r = rand.randint(0,255)
    g = rand.randint(0,255)
    b = rand.randint(0,255)
    rect = w.Rect((r,g,b))
    rect.x = x
    rect.y = y
    rect.rect.x = rect.x
    rect.rect.y = rect.y
    all_sprites_list.add(rect)
    rects.add(rect)

def events():
    global present_wait
    for event in p.event.get():
        if event.type == p.QUIT:
            close()
        if event.type == p.KEYDOWN:
            if event.key == p.K_ESCAPE:
                close()

def close():
    print(clock)
    p.display.quit()
    raise SystemExit

def update_sprites():
    rects.update()

def update_screen():
    background.fill([0,0,50])
    all_sprites_list.draw(background)
    p.display.flip()
    clock.tick(60)

def delete_sprites():
    for sprite in all_sprites_list:
        if sprite.x < 0-20 or sprite.x > background.get_rect().w:
            sprite.kill()
        if sprite.y < 0-20 or sprite.y > background.get_rect().h:
            sprite.kill()

def change_coord():        #change place where rects are created
    x = rand.randint(0,background.get_rect().w)
    y = rand.randint(0,background.get_rect().h)
    return x, y

def loop():
    count = 0
    new_rect = count
    change_coord_int = count
    while True:
        events()
        delete_sprites()
        if count == change_coord_int:
            rect_x, rect_y = change_coord()
            change_coord_int = change_coord_int + 10
        if count == new_rect:
            for i in range(100):
                create_rect(rect_x, rect_y)
            new_rect = count + 5
        update_sprites()
        update_screen()
        #game_over()
        count = count + 1



if __name__ == '__main__':
    setup()
    p.time.wait(2000)
    loop()
