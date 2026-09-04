import random as r
print('-----------------------------------------------------------------------------')
print('==Welcome to Blackjack==')
print('-----------------------------------------------------------------------------')
pm=int(input('Enter Money to Gamble(2x on win) :$'))
print('Dealing cards')
pl=[r.randint(1,10)]
dl=[r.randint(1,10)]
print("Player's Hand:",sum(pl))
print("Dealers's Hand:",sum(dl))
print('-----------------------------------------------------------------------------')
while (sum(pl) or sum(dl))<=21:
    x=input("Enter 'hit' or 'stand':")
    print('-----------------------------------------------------------------------------')

    suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    c = r.randint(1, 10)
    suit = r.choice(suits)

    if c == 1 or c==11:
        while c<=10:
            print(f"Ace of {suit}-(Value:1)")
        value = 1
    elif 2 <= c <= 10:
        print(f"{c} of {suit}-(Value:{c})")
        value = c
    elif c == 11:
        print(f"Jack of {suit}-(Value:10)")
        value = 10
    elif c == 12:
        print(f"Queen of {suit}-(Value:10)")
        value = 10
    elif c == 13:
        print(f"King of {suit}-(Value:10)")
        value = 10

    if x=='hit':
       pl.append(value)
    if x=='stand':
       dl.append(value)
    elif x!='hit' and x!='stand':
         print('enter valid input')
         break

    plt=sum(pl)
    dlt=sum(dl)

    print('Player total:',plt)
    print('Dealer total:',dlt)
    print('-----------------------------------------------------------------------------')
    if plt==21 or dlt>21:
        print("Player wins")
        print('You have won :$',pm)
        print('Total Winnings :$',pm*2)
        break
    if dlt==21 or plt>21:
        print("Dealer wins")
        print('You have lost :-$',pm)
        break