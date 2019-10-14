#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import json
import PlayCards

json_data = {}
json_data["status"] = 0
json_data["data"] = {}
json_data["data"]["id"] = 1000
json_data["data"]["card"] = ""

list = [x for x in range(52)]

cards = ["*A", "$A", "&A", "#A",
         "*2", "$2", "&2", "#2",
         "*3", "$3", "&3", "#3",
         "*4", "$4", "&4", "#4",
         "*5", "$5", "&5", "#5",
         "*6", "$6", "&6", "#6",
         "*7", "$7", "&7", "#7",
         "*8", "$8", "&8", "#8",
         "*9", "$9", "&9", "#9",
         "*10", "$10", "&10", "#10",
         "*J", "$J", "&J", "#J",
         "*Q", "$Q", "&Q", "#Q",
         "*K", "$K", "&K", "#K", ]

while (True):
    numbers = random.sample(list, 13)
    str_temp = ""
    for i in numbers:
        str_temp = str_temp + cards[i] + " "
    str_temp = str_temp[0:len(str_temp) - 1]
    json_data["data"]["card"] = str_temp
    print(json_data)
    output = PlayCards.PostCards(json_data)
    print(output)