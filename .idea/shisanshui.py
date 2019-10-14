import random
class Card():
    def _init_(self, suit, rank, value):
        self.suit = suit    #花色
        self.rank = rank    #牌号
        self.value = value   #牌值
    def InitCard(self):
        self.cards = []
        for suit in ["$","&","*","#"]:
            for rank in ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]:
                self.cards.append(self.Card(suit,rank,self.Calculate(rank)))
        from random import shuffle as refresh
        refresh(self.cards)
    def Calculate(rank):
        dictionary = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
        value = dictionary[rank]
        return value
    def take_card(self, n=13):    #取牌
        your_card = []
        for i in range(n):
            your_card.append(self.cards.pop())
            return your_card













