#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

class Handcricket():
    def __init__(self,players):
        self.players = players
        self.run = [0]*len(players)
    def play(self):
        for i in range(len(self.players)):
            for j in range(len(self.players)):
                if i == j:
                    continue
                batsmen = self.players[i]
                baller = self.players[j]

                print(f"{batsmen} turn to bat against {baller}")
                batsmen_play = int(input(f"{batsmen} predict a no between no 1-6:"))
                bowler_play = random.randint(1,6)
                print(f"{baller} shows: {batsmen_play}")

                if batsmen_play == bowler_play:
                    print(f"{batsmen}scores:{batsmen_play}")
                    self.run[i] += batsmen_play
                else:
                    print('batsmen is out ')
    def score(self):
        print('Game over')
        for i in range(len(self.players)):
            print(f"{self.players[i]} score {self.run[i]}")
            
if __name__ == "__main__":
    num_players = int(input('No of players:'))
    players=[]
    for i in range(num_players):
        name = input(f"The name of player is {i+1}:")
        players.append(name)
    game = Handcricket(players)
    game.play()
    game.score()


#  
