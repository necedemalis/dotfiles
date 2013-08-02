import pygame
import chessboard

class QueenSprite:
    """ Create and initialize a queen """

    def __init__ (self, img, target_posn):
        self.image = img
        self.target_posn = target_posn
        self.posn = target_posn

    def update (self):
        return

    def draw (self,target_surface):
        target_surface.blit(self.image,self.posn)



def share_diagonal(x0,y0,x1,y1):
    dy= abs(y1-y0)
    dx= abs(x1-x0)
    return dx == dy

def col_clashes (bs,c):
    for i in range(c):
        if share_diagonal (i, bs[i],c, bs[c]):
            return True


    return False

def has_clashes(the_board):
    for col in range(1,len(the_board)):
        if col_clashes(the_board,col):
            return True
    return False

def main ():
    import random
    rng = random.Random()
    bd=list(range(8))
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries +=1
        if not has_clashes(bd):
            print ("Found solution {0} in {1} tries.".format(bd,tries))
            chessboard.draw_board(bd)
            all_tries += tries
            tries = 0
            num_found +=1
main ()
