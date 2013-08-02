import random
import pygame
import counter

cards_img = pygame.image.load("cards.gif")
cards_img_cov = pygame.image.load("card-back.png")
cards_w = cards_img.get_width () /13
cards_h = cards_img.get_height() /4
cards_img_cov = pygame.transform.scale(cards_img_cov, (cards_w,cards_h))

class Cards:
    """ Card gets defined and drawn """

    def __init__ (self,img,pos,which_card,cov):
        self.img = img
        self.posn = pos
        self.card_nr = which_card
        self.cov = cov
        return

    def draw (self, surface, img):
        self.img = img
        card_row=self.card_nr//13
        card_col=self.card_nr%13
        card = (card_col*cards_w, card_row*cards_h, cards_w,cards_h)
        surface.blit (self.img, self.posn, card)

    def cover (self, surface, img):
        self.img = img
        surface.blit (self.img, self.posn)

    def __str__ (self):
        return "({0},{1},{2},{3})".format(self.img,self.posn,self.card_nr,self.cov)

def blackjack(music_pos):
    #Setup
    pygame.init ()
    surface = pygame.display.set_mode((640,400))
    surface.fill ((182,88,41))
    pygame.display.set_caption("Blackjack")
    music = pygame.mixer.music.load("entertainer.mp3")
    pygame.mixer.music.play (100,music_pos)
    mouse_down= False
    finished = 0
    restart = 0

    #Font
    my_font = pygame.font.SysFont("Courier",50)
    my_font2 = pygame.font.SysFont("Courier",30)

    #Headline
    the_text = my_font.render ("Blackjack",False , (0,0,0))

    #Buttons
    button_draw = pygame.draw.rect(surface,(0,0,0),(400,100,200,50),1)
    button_pass = pygame.draw.rect(surface,(0,0,0),(400,200,200,50),1)
    button_draw_text = my_font2.render ("Draw Card", True, (0,0,0))
    button_pass_text = my_font2.render ("Pass", True, (0,0,0))

    #Get rand cards and put Cards objects in list
    rng = random.Random()
    cards_list = list(range(52))
    rng.shuffle(cards_list)

    all_cards_player = []
    all_cards_dealer = []
    card_pos_player=20
    card_pos_dealer=20
    for i in range (4):
        if i%2 == 0:
            card_pos_player = card_pos_player + (cards_w + cards_w/2)
            a_card = Cards (cards_img,(card_pos_player , 90), cards_list[i],0)
            all_cards_player.append(a_card)
        else:
            card_pos_dealer = card_pos_dealer + (cards_w + cards_w/2)
            if i == 1:
                a_card = Cards (cards_img,(card_pos_dealer , 190), cards_list[i],0)
            else:
                a_card = Cards (cards_img,(card_pos_dealer , 190), cards_list[i],1)
            all_cards_dealer.append(a_card)
    del cards_list[:4]


    while restart == 0:
        #Quit Button
        ev =pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()

        #Mouse down
        if ev.type == pygame.MOUSEBUTTONDOWN:
                posn_of_click = ev.dict["pos"]
                (mouse_x,mouse_y) = posn_of_click
                mouse_down = True

        # Player New Card
        if mouse_down == True:
            # Draw Button
            if mouse_x >400 and mouse_x <600 and mouse_y > 100 and mouse_y < 150:
                card_pos_player = card_pos_player + (cards_w + cards_w/2)
                a_card = Cards (cards_img,(card_pos_player , 90), cards_list[i],0)
                all_cards_player.append(a_card)
                del cards_list[:1]
                mouse_down = False
                if counter_dealer <= 16 and counter_player < 22:
                    card_pos_dealer = card_pos_dealer + (cards_w + cards_w/2)
                    a_card = Cards (cards_img,(card_pos_dealer , 190), cards_list[i],1)
                    all_cards_dealer.append(a_card)
                    del cards_list[:1]

        #Counter
        counter_player = counter.counter_p (all_cards_player)
        counter_dealer = counter.counter_d (all_cards_dealer)

        #Dealer New Card
        if mouse_down == True:
            #Draw Button
            if mouse_x >400 and mouse_x <600 and mouse_y > 100 and mouse_y < 150:
                mouse_down = False
                if counter_dealer <= 16 and counter_player < 22:
                    card_pos_dealer = card_pos_dealer + (cards_w + cards_w/2)
                    a_card = Cards (cards_img,(card_pos_dealer , 190), cards_list[i],1)
                    all_cards_dealer.append(a_card)
                    del cards_list[:1]
            # Pass Button
            if mouse_x >400 and mouse_x <600 and mouse_y > 200 and mouse_y < 250:
                mouse_down = False
                if counter_dealer > 16:
                    finished = 1
                elif counter_dealer <= 16:
                    while counter_dealer <= 16:
                        card_pos_dealer = card_pos_dealer + (cards_w + cards_w/2)
                        a_card = Cards (cards_img,(card_pos_dealer , 190), cards_list[i],1)
                        all_cards_dealer.append(a_card)
                        del cards_list[:1]
                        counter_dealer = counter.counter_d (all_cards_dealer)
                        finished = 1

        #Win/Lose
        if counter_player > 21 or counter_dealer > 21 or finished == 1:
            restart = 1
            if counter_player > 21:
                lose_text = my_font.render ("You lose", False, (0,0,0))
                surface.blit (lose_text, (200,300))
            elif counter_dealer > 21:
                win_text = my_font.render ("You win", False, (0,0,0))
                surface.blit (win_text, (200,300))
            elif finished == 1:
                if counter_player > counter_dealer:
                    win_text = my_font.render ("You win", False, (0,0,0))
                    surface.blit (win_text, (200,300))
                elif counter_dealer > counter_player:
                    lose_text = my_font.render ("You lose", False, (0,0,0))
                    surface.blit (lose_text, (200,300))
                elif counter_dealer == counter_player:
                    draw_text = my_font.render ("Draw", False, (0,0,0))
                    surface.blit (draw_text, (200,300))

            for (pos,card) in enumerate (all_cards_dealer):
                card.cov = 0
                del all_cards_dealer[pos]
                all_cards_dealer.insert(pos,card)

        #Slice of Cards
        for card in all_cards_player:
                card.draw (surface, cards_img)
        for card in all_cards_dealer:
            if card.cov == 0:
                card.draw (surface, cards_img)
            else:
                card.cover (surface,cards_img_cov)

        #Text
        surface.blit (the_text, (200,10))
        surface.blit (button_draw_text, (420,105))
        surface.blit (button_pass_text, (460,205))

        pygame.display.flip()

    #Buttons
    while restart == 1:
        button_restart = pygame.draw.rect(surface,(0,0,0),(400,300,200,50),1)
        button_restart_text = my_font2.render ("Restart", True, (0,0,0))
        surface.blit (button_restart_text, (460,305))

        pygame.display.flip()

        pygame.time.wait (3000)
        music_pos2 = pygame.mixer.music.get_pos()
        blackjack(music_pos2)
blackjack(0)
