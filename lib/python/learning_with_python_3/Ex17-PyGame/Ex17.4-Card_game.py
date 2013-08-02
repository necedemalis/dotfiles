import random
import pygame

cards_img = pygame.image.load("cards.gif")
cards_w = cards_img.get_width () /13
cards_h = cards_img.get_height() /4

class Cards:
    """ Card gets defined and drawn """

    def __init__ (self,img,pos, which_card):
        self.img = img
        self.posn = pos
        self.card_nr = which_card
        return

    def draw (self, surface):
        card_row=self.card_nr//13
        card_col=self.card_nr%13


        card = (card_col*cards_w, card_row*cards_h, cards_w,cards_h)
        surface.blit (self.img, self.posn, card)

    def shuffle (self):
        return

    def __str__ (self):
        return "({0},{1},{2})".format(self.img,self.posn,self.card_nr)

def poker (r):
    #Setup
    pygame.init () 
    surface = pygame.display.set_mode((640,400))
    surface.fill ((182,88,41))

    #Font
    my_font = pygame.font.SysFont("Courier",50)

    #Get 5 rand cards and put Cards objects in list
    card_list = []
    rng = random.Random ()
    for i in range (r):
        i = rng.randrange (0,52)
        card_list.append(i)

    all_cards =[]
    x=20
    for i in range (len(card_list)):
        x = x + (cards_w + cards_w/2)
        a_card = Cards (cards_img,(x , 90), card_list[i])
        all_cards.append(a_card)

    while True:
        #Quit Button
        ev =pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        #Shuffle Button

        #Reset Button

        #Slice of Cards
        for card in all_cards:
            card.draw (surface)

        #Text
        the_text = my_font.render ("Poker Cards", False , (0,0,0))
        surface.blit (the_text, (50,10))
        pygame.display.flip()

    pygame.quit()

poker(9)
