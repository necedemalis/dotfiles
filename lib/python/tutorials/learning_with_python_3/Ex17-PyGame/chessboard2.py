import pygame

gravity = 0.0001

class QueenSprite:
    """ Create and initialize a queen """

    def __init__ (self, img, target_posn):
        self.image = img
        self.target_posn = target_posn
        (x,y) = target_posn
        self.posn = (x,0)
        self.y_velocity = 0

    def update (self):
        self.y_velocity += gravity
        (x,y) = self.posn
        new_y_pos = y + self.y_velocity
        (target_x,target_y) = self.target_posn
        dist_to_go= target_y - new_y_pos
        if dist_to_go < 0:
            self.y_velocity = -0.65 * self.y_velocity
            new_y_pos = target_y + dist_to_go
        self.posn = (x,new_y_pos)

    def draw (self,target_surface):
        target_surface.blit(self.image,self.posn)

    def contains_point(self,pt):
        "Return True if my sprite contain point pt """
        (my_x,my_y) = self.posn
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x,y)= pt
        return (x >= my_x and x < my_x + my_width and
                y >= my_y and y < my_y + my_height)

    def handle_click(self):
        self.y_velocity += -0.3

def draw_board(the_board):
    """ Draw a Chessboard """
    ###Setup
    pygame.init()

    colors = [(255,255,255),(0,0,0)]

    n = len(the_board)
    surface_sz = 480
    sq_sz = surface_sz //n
    surface_sz = n * sq_sz

    queen = pygame.image.load("/home/joecool/lib/python/tutorial/Ex17-PyGame/queen.png")
    queen = pygame.transform.scale(queen, (sq_sz - sq_sz//3,sq_sz-sq_sz//3))
    queen_offset = (sq_sz - queen.get_width())//2

    surface = pygame.display.set_mode((surface_sz, surface_sz))

    all_sprites = []
    #Draw queens
    for (col, row) in enumerate (the_board):
        a_queen = QueenSprite (queen,(col* sq_sz + queen_offset, row * sq_sz + queen_offset))
        all_sprites.append(a_queen)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            if key == 27:
                break
            if key ==ord("r"):
                colors[0] = (255,0,0)
            elif key ==ord("g"):
                colors[0] = (0,255,0)
            elif key ==ord("b"):
                colors[0] = (0,0,255)
        if ev.type == pygame.MOUSEBUTTONDOWN:
                posn_of_click = ev.dict["pos"]
                for sprite in all_sprites:
                    if sprite.contains_point(posn_of_click):
                        sprite.handle_click()
                        break

        #Draw board
        for row in range (n):
            c_indx = row % 2     #Change color of row
            for col in range (n):
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                c_indx = (c_indx +1) % 2

        #Ask sprite to update itself:
        for sprite in all_sprites:
            sprite.update()

        #Ask every sprite to draw itself:
        for sprite in all_sprites:
            sprite.draw(surface)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    draw_board([0, 5, 3, 1, 6, 4, 2])    # 7 x 7 to test window size
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])

