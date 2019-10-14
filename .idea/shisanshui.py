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
class paixing():
    def san_pai(self):   #散牌
        self.three_pai.sort(key=lambda x: x.all_pokers)
        c1 = self.five_pai[0]
        c2 = self.five_pai[1]
        c3 = self.five_pai[2]
        return True if c1.value != c2.value != c3.value else False
    def dui_zi(self):   #对子
        self.three_pai.sort(key=lambda x:x.all_pokers)
        c1 = self.five_pai[0]
        c2 = self.five_pai[1]
        c3 = self.five_pai[2]
        return True if c1.value == c2.value and c1.value != c3.value else False
    def er_dui(self):   #二对
        self.five_pai.sort(key=lambda x:x.all_pokers)
        c1 = self.five_pai[0]
        c2 = self.five_pai[1]
        c3 = self.five_pai[2]
        c4 = self.five_pai[3]
        c5 = self.five_pai[4]
        return True if c1.value == c2.value and c3.value ==c4.value and c1.value != c3.value != c5.value else False
    def san_tiao(self):   #三条
        self.five_pai.sort(key=lambda x: x.all_pokers)
        c1 = self.five_pai[0]
        c2 = self.five_pai[1]
        c3 = self.five_pai[2]
        c4 = self.five_pai[3]
        c5 = self.five_pai[4]
        return True if c1.value == c2.value == c3.value != c4.value !=c5.value else False
    def shun_zi(self):   #顺子
        self.five_pai.sort(key=lambda x: x.all_pokers)
        c1 = self.five_pai[0]
        c2 = self.five_pai[1]
        c3 = self.five_pai[2]
        c4 = self.five_pai[3]
        c5 = self.five_pai[4]
        return True if c1.type != c2.type and c1.value + 1 == c2.value + 1 and c2.value + 1 == c3.value + 1 and c3.value + 1 == c4.value + 1 and c4.value + 1 == c5.value + 1 else False
    def tong_hua(self):   #同花
        self.five_pai.sort(key=lambda x: x.all_pokers)
        c1 = self.five_pai[0]
        c2 = self.five_pai[1]
        c3 = self.five_pai[2]
        c4 = self.five_pai[3]
        c5 = self.five_pai[4]
        return True if c1.type == c2.type == c3.type ==c4.type ==c5.type else False
    def hu_lu(self):   #葫芦
        self.five_pai.sort(key=lambda x: x.all_pokers)
        c1 = self.five_pai[0]
        c2 = self.five_pai[1]
        c3 = self.five_pai[2]
        c4 = self.five_pai[3]
        c5 = self.five_pai[4]
        return True if c1.value == c2.value == c3.value != c4.value == c5.value else False
    def zha_dan(self):   #炸弹
        self.five_pai.sort(key=lambda x: x.all_pokers)
        c1 = self.five_pai[0]
        c2 = self.five_pai[1]
        c3 = self.five_pai[2]
        c4 = self.five_pai[3]
        c5 = self.five_pai[4]
        return True if c1.value == c2.value == c3.value ==c4.value != c5.value else False
    def tong_hua_shun(self):   #同花顺
        self.five_pai.sort(key=lambda x: x.all_pokers)
        c1 = self.five_pai[0]
        c2 = self.five_pai[1]
        c3 = self.five_pai[2]
        c4 = self.five_pai[3]
        c5 = self.five_pai[4]
        return True if c1.type == c2.type == c3.type == c4.type == c5.type and  c1.value + 1 == c2.value + 1 and c2.value + 1 == c3.value + 1 and c3.value + 1 == c4.value + 1 and c4.value + 1 == c5.value + 1 else False
    def san_tong_hua(self):   #三同花












