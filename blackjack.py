import random

dealer = []

player = []

while len(dealer) != 2:
    dealer.append(random.randint(1, 11))
    if len(dealer) == 2:
        print("Dealer: ? ,", dealer[1])

while len(player) != 2:
    player.append(random.randint(1, 11))
    if len(player) == 2:
        print("You have ", player)
 
if sum(dealer) == 21:
    print("BLACKJACK dealer wins.")
elif sum(dealer) > 21:
    print("BUST you win.")

while sum(player) < 21:
    action = str(input("Hit or stay? "))
    if action == "hit":
        player.append(random.randint(1, 11))
        print("You: " + str(sum(player)) + "", player)
    else:
        print("Dealer: " + str(sum(dealer)) + "", dealer)
        print("You: " + str(sum(player)) + "", player)
        if sum(dealer) <= 16:
        	dealer.append(random.randint(1,11))
        	print("Dealer: " + str(sum(dealer)) + "", dealer)
        if sum(dealer) > 21:
            print("BUST you win.")
            break
        if sum(dealer) > sum(player):
            print("Dealer wins.")
            break
        else:
            print("You win.")
            break

if sum(player) > 21:
    print("BUST Dealer wins.")
elif sum(player) == 21:
    print("BLACKJACK you win.")
