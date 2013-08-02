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
