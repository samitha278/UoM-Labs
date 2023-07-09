#not completed yet




def main():

    dealer = input().split()
    player = input().split()

    dealer_value = get_score(dealer)
    player_value = get_score(player)

    

    if (player_value == 21) and (not dealer_value==21):
        print("Win")
    elif (player_value<21) and (dealer_value<player_value): 
        print("Win")
    elif player_value==dealer_value:
        print("Hit")
    else:
        print("Lost")
    

def get_score(cards):
    card_lst = [c[1] for c in cards]

    value = sum(card_value(card) for card in card_lst)

    return value

    
def card_value(card):
    value_10 = ['10','J','Q','K']
    if card=='A':
        return 11
    elif card in value_10:
        return 10
    else:
        return int(card)
    
main()

    
