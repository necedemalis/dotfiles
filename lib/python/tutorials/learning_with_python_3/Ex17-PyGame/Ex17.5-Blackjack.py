import random
import pygame

cards_img = pygame.image.load("cards.gif")
cards_img_cov = pygame.image.load("card-back.png")
cards_w = cards_img.get_width () /13
cards_h = cards_img.get_height() /4
cards_img_cov = pygame.transform.scale(cards_img_cov, (cards_w,cards_h))
title_img = pygame.image.load("Blackjack.png")
bg_img = pygame.image.load ("background.jpg")

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

def counter_p (all_cards_player,):
    counter_player = 0
    acp = []
    for card in all_cards_player:
        a = card.card_nr
        a = a%13
        acp.append (a)
    acp.sort()
    acp.reverse()
    for a in acp:
        if a > 0 and a <= 8: #2-9
            counter_player += (a+1)
        elif a >= 9: #10 und Bilder
            counter_player += 10
        elif a == 0: #Ass
            if counter_player <= 10:
                counter_player += 11
            else:
                counter_player += 1

    return counter_player

def counter_d (all_cards_dealer):
    counter_dealer = 0
    acd = []
    for card in all_cards_dealer:
        a = card.card_nr
        a = a%13
        acd.append (a)
    acd.sort()
    acd.reverse()
    for a in acd:
        if a > 0 and a <= 8: #2-9
            counter_dealer += (a+1)
        elif a >= 9: #10 und Bilder
            counter_dealer += 10
        elif a == 0: #Ass
            if counter_dealer <= 10:
                counter_dealer += 11
            else:
                counter_dealer += 1

    return counter_dealer

def blackjack():

    pygame.init ()
    pygame.display.set_caption("Black Jack")
    pygame.mixer.music.load("entertainer.mp3")
    pygame.mixer.music.set_volume(0.09)
    pygame.mixer.music.play (-1)

    def main (pl_w,dl_w):
        surface = pygame.display.set_mode((640,400))
        surface.blit (bg_img, (0,0))
        shuffle_sound = pygame.mixer.Sound ("shuffling-cards2.mp3")

        #Font
        my_font = pygame.font.SysFont("Georgia",40)
        my_font2 = pygame.font.SysFont("Georgia",30)

        #Integers
        mouse_down= False
        finished = 0
        restart = 0
        player_wins = pl_w
        dealer_wins = dl_w

        #Buttons
        button_draw = pygame.draw.rect(surface,(0,100,255),(450,100,150,50),)
        button_pass = pygame.draw.rect(surface,(0,100,255),(450,180,150,50),)
        button_draw_text = my_font2.render ("Card", True, (0,0,0))
        button_pass_text = my_font2.render ("Pass", True, (0,0,0))

        bottom = pygame.draw.rect(surface,(0,100,255),(0,350,640,50,),0)

        #Text
        you_text = my_font2.render ("You:", True, (255,255,255))
        bank_text = my_font2.render ("Bank:", True, (255,255,255))
        lose_text = my_font.render ("You lose!", True, (204,5,5))
        win_text = my_font.render ("You win!", True, (204,5,5))
        draw_text = my_font.render ("Draw!", True, (204,5,5))
        blackjack_text = my_font.render ("Black Jack!", True, (204,5,5))

        #Get rand cards and put Cards objects in list
        rng = random.Random()
        cards_list = list(range(52))
        rng.shuffle(cards_list)

        all_cards_player = []
        all_cards_dealer = []
        card_pos_player=35
        card_pos_dealer=35
        for i in range (4):
            if i%2 == 0:
                card_pos_player = card_pos_player + (cards_w + cards_w/2)
                a_card = Cards (cards_img,(card_pos_player , 110), cards_list[i],0)
                all_cards_player.append(a_card)
            else:
                card_pos_dealer = card_pos_dealer + (cards_w + cards_w/2)
                if i == 1:
                    a_card = Cards (cards_img,(card_pos_dealer , 220), cards_list[i],0)
                else:
                    a_card = Cards (cards_img,(card_pos_dealer , 220), cards_list[i],1)
                all_cards_dealer.append(a_card)
        del cards_list[:4]

        #Main game
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

            #Player New Card
            if mouse_down == True:
                # Draw Button
                if mouse_x >450 and mouse_x <600 and mouse_y > 100 and mouse_y < 150:
                    card_pos_player = card_pos_player + (cards_w + cards_w/2)
                    a_card = Cards (cards_img,(card_pos_player , 110), cards_list[i],0)
                    all_cards_player.append(a_card)
                    del cards_list[:1]
                    mouse_down = False
                    if counter_dealer <= 16 and counter_player < 22:
                        card_pos_dealer = card_pos_dealer + (cards_w + cards_w/2)
                        a_card = Cards (cards_img,(card_pos_dealer , 220), cards_list[i],1)
                        all_cards_dealer.append(a_card)
                        del cards_list[:1]

            #Counter
            counter_player = counter_p (all_cards_player)
            counter_dealer = counter_d (all_cards_dealer)

            #Dealer New Card
            if mouse_down == True:
                #Draw Button
                if mouse_x >450 and mouse_x <600 and mouse_y > 100 and mouse_y < 150:
                    mouse_down = False
                    if counter_dealer <= 16 and counter_player < 22:
                        card_pos_dealer = card_pos_dealer + (cards_w + cards_w/2)
                        a_card = Cards (cards_img,(card_pos_dealer , 220), cards_list[i],1)
                        all_cards_dealer.append(a_card)
                        del cards_list[:1]
                # Pass Button
                if mouse_x >450 and mouse_x <600 and mouse_y > 180 and mouse_y < 230:
                    mouse_down = False
                    if counter_dealer > 16:
                        finished = 1
                    elif counter_dealer <= 16 and counter_player <= 21:
                        while counter_dealer <= 16:
                            card_pos_dealer = card_pos_dealer + (cards_w + cards_w/2)
                            a_card = Cards (cards_img,(card_pos_dealer , 220), cards_list[i],1)
                            all_cards_dealer.append(a_card)
                            del cards_list[:1]
                            counter_dealer = counter_d (all_cards_dealer)
                            finished = 1

            #Win/Lose
            if counter_player > 21 or counter_dealer > 21 or finished == 1:
                restart = 1
                if counter_player > 21:
                    surface.blit (lose_text, (150,300))
                    dealer_wins += 1
                elif counter_dealer > 21:
                    if counter_player == 21 and len(all_cards_player) == 2:
                        surface.blit (blackjack_text, (150,300))
                    else:
                        surface.blit (win_text, (150,300))
                    player_wins += 1
                elif finished == 1:
                    if counter_player > counter_dealer:
                        if counter_player == 21 and len(all_cards_player) == 2:
                            surface.blit (blackjack_text, (150,300))
                        else:
                            surface.blit (win_text, (150,300))
                        player_wins += 1
                    elif counter_dealer > counter_player:
                        surface.blit (lose_text, (150,300))
                        dealer_wins += 1
                    elif counter_dealer == counter_player:
                        surface.blit (draw_text, (150,300))

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

            #Win-Counter
            if restart == 0:
                win_counter_text = my_font2.render ("You: {0} Wins | Bank: {1} Wins".format(player_wins, dealer_wins),True,(255,255,255))
            else:
                win_counter_text = my_font2.render ("".format(player_wins, dealer_wins),True,(255,255,255))

            #Blit
            surface.blit (button_draw_text, (494,107))
            surface.blit (button_pass_text, (494,187))
            surface.blit (title_img,(0,0))
            surface.blit (win_counter_text,(20,360))
            surface.blit (you_text, (10,120))
            surface.blit (bank_text, (10,230))

            pygame.display.flip()
            #my_clock.tick(60)

        #result display/ restart
        while restart == 1:
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
                if mouse_x >450 and mouse_x <600 and mouse_y > 260 and mouse_y < 310:
                    shuffle_sound.play ()
                    main (player_wins,dealer_wins)

            button_restart = pygame.draw.rect(surface,(0,100,255),(450,260,150,50),0)
            button_restart_text = my_font2.render ("Restart", True, (0,0,0))
            surface.blit (button_restart_text, (478,267))
            surface.blit (win_counter_text,(20,360))

            pygame.display.flip()

    main (0,0)
blackjack()
