# coding: utf-8
import json
import os
import requests
import sys
import pymongo


def store(res):
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn.leetcode
    my_set = db.question
    my_set.insert_many(res)

if __name__ == "__main__":
    #get question list from api
    # url = "https://leetcode.com/api/problems/all/"
    # list = json.loads(requests.get(url).text)

    #get question list from local file
    config_file = sys.path[0] + os.path.sep + "list.json"
    with open(config_file, 'r') as f:
        list = json.load(f)
    infos = list['stat_status_pairs']
    res = []
    for info in infos:
        tmp = {}
        tmp['paid_only'] = info['paid_only']                                                #是否有锁
        tmp['difficulty'] = info['difficulty']['level']                                    #困难等级
        tmp['question_id'] = info['stat']['question_id']
        tmp['question_title'] = info['stat']['question__title']                          #题目
        tmp['question_article_live'] = info['stat']['question__article__live']         #是否存在solution
        tmp['question_slug'] = info['stat']['question__title_slug']                     #连接地址
        res.append(tmp)
    store(res)

