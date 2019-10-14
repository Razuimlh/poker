#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import SpecialCardsType
import CommonCardsType
import flask

server = flask.Flask(__name__)

json_data = {
    "status": 0,
    "data": {
        "id": 1000,
        "card": "$3 $4 $5 $6 $7 *6 &8 *8 *9 *10 #J #Q #K"
    }
}

Sanpai_Value_1 = [0, 0, 0, 0, 0, 289, 1158, 2895, 5791, 10135, 16217, 24325, 34751, 47782, 63710]
# 散牌出现在前墩时各种牌面的权值
Sanpai_Value_2 = [0, 0, 0, 0, 0, 0, 0, 0, 156, 706, 2040, 4748, 9654, 17857, 30769]
# 散牌出现在中墩是各种牌面的权值
Duizi_Value_1 = [0, 0, 82823, 84126, 85429, 86733, 88036, 89339, 90642, 91945, 93248, 94552, 95855, 97158, 98461]
# 对子出现在前墩时各种牌面的权值
Duizi_Value_2 = [0, 0, 50156, 53407, 56658, 59908, 63159, 66409, 69660, 72910, 76161, 79411, 82662, 85912, 89163]
# 对子出现在中墩时各种牌面的权值
Duizi_Value_3 = [0, 0, 0, 6521, 13043, 19564, 26086, 32607, 39129, 45650, 52172, 58693, 65215, 71736, 78258]
# 对子出现在后墩时各种牌面的权值
Erdui_Value_2 = [0, 0, 0, 0, 92413, 92474, 92596, 92779, 93023, 93328, 93693, 94120, 94607, 95156, 95765]
# 二对出现在中墩时各种牌面的权值
Erdui_Value_3 = [0, 0, 0, 0, 84779, 84902, 85146, 85513, 86002, 86614, 87347, 88203, 89182, 90282, 91505]
# 二对出现在后墩时各种牌面的权值
Liandui_Value_2 = [0, 0, 0, 96436, 96497, 96558, 96619, 96680, 96741, 96802, 96863, 96924, 96984, 97045, 97106]
# 连对出现在中墩时各种牌面的权值
Liandui_Value_3 = [0, 0, 0, 92850, 92972, 93094, 93217, 93339, 93461, 93584, 93706, 93828, 93950, 94073, 94195]
# 连对出现在后墩时各种牌面的权值
Santiao_Value_1 = [0, 0, 99764, 99782, 99800, 99819, 99837, 99855, 99873, 99891, 99909, 99927, 99945, 99963, 99981]
# 三条出现在前墩时各种牌面的权值
Santiao_Value_2 = [0, 0, 97167, 97330, 97492, 97655, 97817, 97980, 98142, 98305, 98468, 98630, 98793, 98955, 99118]
# 三条出现在中墩时各种牌面的权值
Santiao_Value_3 = [0, 0, 94317, 94643, 94969, 95295, 95622, 95948, 96274, 96600, 96926, 97252, 97578, 97904, 98230]
# 三条出现在后墩时各种牌面的权值
Shunzi_Value_2 = [0, 0, 0, 0, 0, 0, 99280, 99319, 99359, 99398, 99437, 99476, 99516, 99555, 99594]
# 顺子出现在中墩时各种牌面的权值
Shunzi_Value_3 = [0, 0, 0, 0, 0, 0, 98556, 98635, 98714, 98792, 98871, 98950, 99029, 99107, 99186]
# 顺子出现在后墩时各种牌面的权值
Tonghua_Value_2 = [0, 0, 0, 0, 0, 0, 0, 99633, 99634, 99636, 99641, 99652, 99671, 99703, 99754]
# 同花出现在中墩时各种牌面的权值
Tonghua_Value_3 = [0, 0, 0, 0, 0, 0, 0, 99265, 99266, 99270, 99281, 99302, 99341, 99405, 99507]
# 同花出现在后墩时各种牌面的权值
Hulu_Value_2 = [0, 0, 99830, 99841, 99852, 99863, 99874, 99885, 99897, 99908, 99919, 99930, 99941, 99952, 99963]
# 葫芦出现在中墩时各种牌面的权值
Hulu_Value_3 = [0, 0, 99660, 99682, 99704, 99726, 99748, 99771, 99793, 99815, 99837, 99860, 99882, 99904, 99926]
# 葫芦出现在后墩时各种牌面的权值
Zhadan_Value_2 = [0, 0, 99974, 99976, 99978, 99980, 99981, 99983, 99985, 99987, 99989, 99991, 99993, 99994, 99996]
# 炸弹出现在后墩时各种牌面的权值
Zhadan_Value_3 = [0, 0, 99949, 99952, 99956, 99960, 99963, 99967, 99971, 99974, 99978, 99982, 99986, 99989, 99993]
# 炸弹出现在后墩时各种牌面的权值
Tonghuashun_Value_2 = [0, 0, 0, 0, 0, 0, 99998, 99998, 99998, 99999, 99999, 99999, 99999, 99999, 99999]
# 同花顺出现在中墩时各种牌面的权值
Tonghuashun_Value_3 = [0, 0, 0, 0, 0, 0, 99997, 99997, 99997, 99998, 99998, 99998, 99999, 99999, 99999]
# 同花顺出现在后墩时各种牌面的权值


# 获取后墩牌的权值
def GetValue_Houdun(Cardlist=[]):
    value = 0  # 权值
    flag = Judge(Cardlist)
    if flag == 9:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Tonghuashun_Value_3[number]
    elif flag == 8:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Zhadan_Value_3[number]
    elif flag == 7:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Hulu_Value_3[number]
    elif flag == 6:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Tonghua_Value_3[number]
    elif flag == 5:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Shunzi_Value_3[number]
    elif flag == 4:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Santiao_Value_3[number]
    elif flag == 3:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Liandui_Value_3[number]
    elif flag == 2:
        Cardlist.sort()
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Erdui_Value_3[number]
    elif flag == 1:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Duizi_Value_3[number]
    else:
        print("error")
    return value


# 获取中墩牌的权值
def GetValue_Zhongdun(Cardlist=[]):
    value = 0  # 权值
    flag = Judge(Cardlist)
    if flag == 9:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Tonghuashun_Value_2[number]
    elif flag == 8:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Zhadan_Value_2[number]
    elif flag == 7:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Hulu_Value_2[number]
    elif flag == 6:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Tonghua_Value_2[number]
    elif flag == 5:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Shunzi_Value_2[number]
    elif flag == 4:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Santiao_Value_2[number]
    elif flag == 3:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Liandui_Value_2[number]
    elif flag == 2:
        Cardlist.sort()
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Erdui_Value_2[number]
    elif flag == 1:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Duizi_Value_2[number]
    elif flag == 0:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Sanpai_Value_2[number]
    else:
        print("error")
    return value


def GetValue_Qiandun(Cardlist=[]):
    value = 0  # 权值
    if len(Cardlist) == 1:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Sanpai_Value_1[number]
    elif len(Cardlist) == 2:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Duizi_Value_1[number]
    elif len(Cardlist) == 3:
        temp_card = FindBiggestCard(Cardlist)
        number = temp_card[0] - 2
        value = Santiao_Value_1[number]
    else:
        print("error")
    return value


# 这个函数用于列表的差集运算，返回Cardlist1-Cardlist2,要求Cardlist2是Cardlist1的子集
def CalculateSub(Cardlist1=[], Cardlist2=[]):
    chaji = list.copy(Cardlist1)  # 最后要返回的差集
    for item in Cardlist2:
        if item in Cardlist1:
            chaji.remove(item)
        else:
            print(item)
            print("error in fun CalculateSub")
    return chaji

def FindBiggestCard(Cardslist=[]):
    Cardslist.sort()
    lenth = len(Cardslist)
    temp_card = Cardslist[lenth - 1]
    return temp_card


def GetCardlist(json_data):
    str_data = json_data['data']['card']  # 获取原始卡牌字符串
    list_list = []
    list_str = str_data.split(' ')

    for item in list_str:
        symbol = item[0]
        number = item[1:]
        if number == 'J':
            number = '11'
        elif number == 'Q':
            number = '12'
        elif number == 'K':
            number = '13'
        elif number == 'A':
            number = '14'

        number = int(number)
        list_temp = [number, symbol]
        list_list.append(list_temp)
    list_list.sort()
    return list_list


def cardsCombination(Cardlist=[]):
    temp_Cardlist = list.copy(Cardlist)
    AllCardsCombination = []
    temp_list = Common.Tonghuashun(temp_Cardlist)
    if temp_list != []:
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = Common.Zhadan(temp_Cardlist)
    if temp_list != []:
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = Common.Hulu(temp_Cardlist)
    if temp_list != []:
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = Common.Tonghua(temp_Cardlist)
    if temp_list != []:
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = Common.Shunzi(temp_Cardlist)
    if temp_list != []:
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = Common.Santiao(temp_Cardlist)
    if temp_list != []:
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = Common.Liandui(temp_Cardlist)
    if temp_list != []:
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = Common.Erdui(temp_Cardlist)
    if temp_list != []:
        for item in temp_list:
            AllCardsCombination.append(item)
    temp_list = Common.Duizi(temp_Cardlist)
    if temp_list != []:
        for item in temp_list:
            AllCardsCombination.append(item)
    return AllCardsCombination


def Judge(Cardlist=[]):
    temp_Cardlist = list.copy(Cardlist)
    if Common.Tonghuashun(temp_Cardlist) != []:
        return 9
    elif Common.Zhadan(temp_Cardlist) != []:
        return 8
    elif Common.Hulu(temp_Cardlist) != []:
        return 7
    elif Common.Tonghua(temp_Cardlist) != []:
        return 6
    elif Common.Shunzi(temp_Cardlist) != []:
        return 5
    elif Common.Santiao(temp_Cardlist) != []:
        return 4
    elif Common.Liandui(temp_Cardlist) != []:
        return 3
    elif Common.Erdui(temp_Cardlist) != []:
        return 2
    elif Common.Duizi(temp_Cardlist) != []:
        return 1
    else:
        return 0


def Compare(Cardlist1=[], Cardlist2=[]):
    flag1 = Judge(Cardlist1)
    flag2 = Judge(Cardlist2)
    list_count1 = Common.GetList_count(Cardlist1)
    list_count2 = Common.GetList_count(Cardlist2)
    bigCard1 = -1
    bigCard2 = -2
    if flag2 > flag1:
        return True
    elif flag1 == flag2:
        if flag1 == flag2 == 7:
            for i in range(15):
                if list_count1[i] == 3:
                    bigCard1 = i
                if list_count2[i] == 3:
                    bigCard2 = i
            if bigCard2 >= bigCard1:
                return True
            else:
                return False
        else:
            bigCard1 = FindBiggestCard(Cardlist1)
            bigCard2 = FindBiggestCard(Cardlist2)
            if bigCard2 >= bigCard1:
                return True
            else:
                return False
    else:
        return False

@server.route('/PostCards', methods=['post'])
def PostCards(data):
    Cardlist = GetCardlist(data)
    temp_Cardlist = list.copy(Cardlist)

    if Special.IsZhizunqinglong(temp_Cardlist):
        print("至尊清龙")
        return temp_Cardlist
    elif Special.IsYitiaolong(temp_Cardlist):
        print("一条龙")
        return temp_Cardlist
    elif Special.IsShierhuangzu(temp_Cardlist):
        print("十二皇族")
        return temp_Cardlist
    elif Special.IsSantonghuashun(temp_Cardlist):
        print("三同花顺")
        return temp_Cardlist
    elif Special.IsSanfentianxia(temp_Cardlist):
        print("三分天下")
        return temp_Cardlist
    elif Special.IsQuanda(temp_Cardlist):
        print("全大")
        return temp_Cardlist
    elif Special.IsQuanxiao(temp_Cardlist):
        print("全小")
        return temp_Cardlist
    elif Special.IsCouyise(temp_Cardlist):
        print("凑一色")
        return temp_Cardlist
    elif Special.IsShuangguaichongsan(temp_Cardlist):
        print("双怪冲三")
        return temp_Cardlist
    elif Special.IsSitaosantiao(temp_Cardlist):
        print("四套三条")
        return temp_Cardlist
    elif Special.IsWuduisantiao(temp_Cardlist):
        print("五对三条")
        return temp_Cardlist
    elif Special.IsLiuduiban(temp_Cardlist):
        print("六对半")
        return temp_Cardlist
    elif Special.IsSanshunzi(temp_Cardlist):
        print("三顺子")
        return temp_Cardlist
    elif Special.IsSantonghua(temp_Cardlist):
        print("三同花")
        return temp_Cardlist
    # 接下来开始按权值最大原则墩牌
    value_all = 0  # 某一种出牌方式的权值
    cards_Qiandun = []  # 前墩的牌
    cards_Zhongdun = []  # 中墩的牌
    cards_Houdun = []  # 后墩的牌
    AllCardsCombination_all = CardsCombination(temp_Cardlist)
    for item1 in AllCardsCombination_all:  # 先拿出后墩
        Cardlist_AfterTakeHoudun = CalculateSub(temp_Cardlist, item1)
        AllCardsCombination_AfterTakeHoudun = CardsCombination(Cardlist_AfterTakeHoudun)
        if AllCardsCombination_AfterTakeHoudun != []:
            for item2 in AllCardsCombination_AfterTakeHoudun:
                Cardlist_AfterTakeZhongdun = CalculateSub(Cardlist_AfterTakeHoudun, item2)
                AllCardsCombination_AfterTakeZhongdun = Common.Duizi(
                    Cardlist_AfterTakeZhongdun) + Common.Santiao(Cardlist_AfterTakeZhongdun)
                if AllCardsCombination_AfterTakeZhongdun != []:
                    for item3 in AllCardsCombination_AfterTakeZhongdun:
                        Cardlist_AfterTakeQiandun = CalculateSub(Cardlist_AfterTakeZhongdun, item3)
                        cards_Qiandun = item3
                        cards_Zhongdun = item2
                        cards_Houdun = item1
                        value_qiandun = GetValue_Qiandun(cards_Qiandun)
                        value_zhongdun = GetValue_Zhongdun(cards_Zhongdun)
                        value_houdun = GetValue_Houdun(cards_Houdun)
                        if (value_qiandun + value_zhongdun + value_houdun > value_all
                                and Compare(cards_Qiandun, cards_Zhongdun) and Compare(cards_Zhongdun, cards_Houdun)):
                            value_all = value_qiandun + value_zhongdun + value_houdun
                            if Cardlist_AfterTakeQiandun != []:
                                for card in Cardlist_AfterTakeQiandun:
                                    if len(cards_Qiandun) < 3:
                                        cards_Qiandun.append(card)
                                    elif len(cards_Zhongdun) < 5:
                                        cards_Zhongdun.append(card)
                                    else:
                                        cards_Houdun.append(card)
                            post_cards = []
                            post_cards.append(cards_Qiandun)
                            post_cards.append(cards_Zhongdun)
                            post_cards.append(cards_Houdun)
                        cards_Qiandun = []
                        cards_Zhongdun = []
                        cards_Houdun = []
                else:
                    cards_Qiandun.append(FindBiggestCard(Cardlist_AfterTakeZhongdun))
                    Cardlist_AfterTakeQiandun = CalculateSub(Cardlist_AfterTakeZhongdun, cards_Qiandun)
                    cards_Houdun = item1
                    cards_Zhongdun = item2
                    value_houdun = GetValue_Houdun(cards_Houdun)
                    value_zhongdun = GetValue_Zhongdun(cards_Zhongdun)
                    value_qiandun = GetValue_Qiandun(cards_Qiandun)
                    if (value_qiandun + value_zhongdun + value_houdun > value_all
                            and Compare(cards_Qiandun, cards_Zhongdun) and Compare(cards_Zhongdun, cards_zoudun)):
                        value_all = value_qiandun + value_zhongdun + value_houdun
                        if Cardlist_AfterTakeQiandun != []:
                            for card in Cardlist_AfterTakeQiandun:
                                if len(cards_Qiandun) < 3:
                                    cards_Qiandun.append(card)
                                elif len(cards_Zhongdun) < 5:
                                    cards_Zhongdun.append(card)
                                else:
                                    cards_Houdun.append(card)
                        post_cards = []
                        post_cards.append(cards_Qiandun)
                        post_cards.append(cards_Zhongdun)
                        post_cards.append(cards_Houdun)
                    cards_Qiandun = []
                    cards_Zhongdun = []
                    cards_Houdun = []

        else:
            cards_Zhongdun.append(FindBiggestCard(Cardlist_AfterTakeHoudun))
            value_zhongdun = GetValue_Zhongdun(cards_Zhongdun)
            Cardlist_AfterTakeZhongdun = CalculateSub(Cardlist_AfterTakeHoudun, cards_Zhongdun)
            cards_Qiandun.append(FindBiggestCard(Cardlist_AfterTakeZhongdun))
            value_qiandun = GetValue_Qiandun(cards_Qiandun)
            Cardlist_AfterTakeQiandun = CalculateSub(Cardlist_AfterTakeZhongdun, cards_Qiandun)
            cards_Houdun = item1
            value_houdun = GetValue_Houdun(cards_Houdun)
            if (value_qiandun + value_zhongdun + value_houdun > value_all
                    and Compare(cards_Qiandun, cards_Zhongdun) and Compare(cards_Zhongdun, cards_Houdun)):
                value_all = value_qiandun + value_zhongdun + value_houdun
                if Cardlist_AfterTakeQiandun != []:
                    for card in Cardlist_AfterTakeQiandun:
                        if len(cards_Qiandun) < 3:
                            cards_Qiandun.append(card)
                        elif len(cards_Zhongdun) < 5:
                            cards_Zhongdun.append(card)
                        else:
                            cards_Houdun.append(card)
                post_cards = []
                post_cards.append(cards_Qiandun)
                post_cards.append(cards_Zhongdun)
                post_cards.append(cards_Houdun)
            cards_Qiandun = []
            cards_Zhongdun = []
            cards_Houdun = []
    return Post_Cards


if __name__ == '__main__':
    cards = PostCards(json_data)
    print(cards)