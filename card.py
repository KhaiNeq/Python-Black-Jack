import random


cardfaces = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
royals = ["Jack", "Queen", "King"]
ace = ["Ace"]
deck = []


for i in range (2,11):
	cardfaces.append(str(i))

for j in range(3):
	cardfaces.append(royals[j])

for p in range(1):
        cardfaces.append(ace[p])

for k in range(4):
	for l in range(13):
		card = (cardfaces[l] + " of " + suits[k])
		deck.append(card)

random.shuffle(deck)

def show_deck():
        for m in range(len(deck)):
                print(deck[m])

def deal():
        # Deal one card from the deck
#        show_deck()
#        print('******')
        # Remove one card from the deck
        card = deck.pop()
 #       show_deck()
        # Return that card
        return(card)

def hand_value(hand):
        # Given a hand (list), work out its value
        print(hand)
        # Set hand_total (initially 0)
        hand_total = 0
        aces = []

        for card in hand:
                # Add value of card to hand_total
                face_value = card.split(' ')[0]
                print (face_value)
                if face_value.isdigit():
                        hand_total += int(face_value)
                elif face_value in ['Jack', 'Queen','King']:
                        hand_total += 10
                else: #It's an Ace!!
                        aces.extend([card])
                        print(aces)
        for card in aces:
                if hand_total >=11:
                        hand_total += 1
                else:
                        hand_total += 11
        # and return it
        return hand_total

