#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
suits = ['Spade', 'Diamond', 'Club', 'Heart']
ranks = ['two','three','four','five','six','seven','eight','nine','ten','joker','king','queen','ace']
values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'joker':10,'king':10,'queen':10,'ace':[1,11]}
playing = True


# In[2]:


class Cards():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    
         
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    

    def add_card(self, card):
        self.cards.append(card)
        self.update_value(card)

    

    def update_value(self, card):
        if card.rank == 'ace':
            if self.value + values[card.rank][1] <= 21:
                self.value += values[card.rank][1]
            else:
                self.value += values[card.rank][0]
        else:
            self.value += values[card.rank]

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# In[3]:


class Chips():
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total +=self.bet
        self.bet=0
    
    def lose_bet(self):
        self.total-=self.bet
        self.bet=0

    def take_bet(self):
        while True:
            try:
                bet = int(input(f"available  chips{self.total}.Enter your bet:"))
                if 0<=bet<=self.total:
                    self.bet = bet
                    break
                else:
                    print ('enter valid between 0 and avilable chip')
            except ValueError:
                print('Invalid input')
                
    
    
    def hit_or_stand(self, deck, hand):
        global playing
        while True:
            player_choice = input("Do you want to hit or stand? Enter 'h' for hit or 's' for stand: ")
            if player_choice.lower() == 'h':
                new_card = deck.deal_card()
                hand.add_card(new_card)
                if new_card.rank == 'ace' and hand.value + values['ace'][1] <= 21:
                    hand.value += values['ace'][1]
                else:
                    hand.value += values[new_card.rank]
            elif player_choice.lower() == 's':
                print('Player stands. Dealer\'s turn.')
                playing = False
            else:
                print('Invalid input. Enter "h" for hit or "s" for stand.')
                continue
            break


# In[4]:


def show_some(player,dealer):
    print('player hand:')
    for card in player.cards:
        print (card)
    
    print('dealer hand:')
    print(dealer.cards[0])
    print('hidden card:')
    
def show_all(player,dealer):
    print('player hand:')
    for card in player.cards:
        print (card)
    print('dealer hand:')
    for card in dealer.cards:
        print(card)
def player_busts(player,dealer,chips):
    print('player busts! dealer win')
    chips.lose_bet()

def player_wins():
    print("player wins")
    chips.win_bet()

def dealer_busts():
    print('dealer wins! player loses')
    chips.lose_bet()
    
def dealer_wins():
    print('dealer wins')
    chips.win_bet()
    
def push():
    print("tie")    


# In[5]:


while True:
    print('Are u ready to play?')
    # Print an opening statement

    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    for _ in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    player_chips.take_bet()
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:
        # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        player_chips.hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if dealer_hand.value<17:
            dealer_hand.hit(deck)
            
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips) 
        
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()
            
    
    # Inform Player of their chips total 
    print(f"the player chip total is:{player_chips.total}")
    # Ask to play again
    play_again = input("Do you want to play again? Enter 'yes' or 'no': ")
    if play_again.lower() != 'yes':
        break
   


# In[ ]:





# In[ ]:





# In[ ]:




