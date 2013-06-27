from Cards import Card
from Cards import Hand
from Cards import CardGame

class OldMaidHand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches {2}".format(self.name, card, match))
                count += 1
        return count

class OldMaidGame(CardGame):
    def play(self, names):
        self.deck.remove(Card(0,12))

        self.hands = []
        
        for name in names:
            self.hands.append(OldMaidHand(name))

        self.deck.deal(self.hands)
        print("--------- Cards have been dealt.")
        self.print_hands()

        matches = self.remove_all_matches()
        print("--------- Matches discarded, play begins")
        self.print_hands()
        
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("--------- Game is Over")
        self.print_hands()

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self,i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor (i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1,num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

#game = CardGame()
#hand = OldMaidHand("frank")
#game.deck.deal([hand],13)
#print(hand)
#hand.remove_matches()
#print(hand)

game = OldMaidGame()
game.play(["Peter","Paul","Mary"])
