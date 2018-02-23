# coding: utf-8
import os
import sys
import tags
import question
import time


def generate(tag):
    res = question.get_question()
    #根据tag生成文件夹
    for t in tag:
        name = t['name']
        pwd = sys.path[0]
        path = os.path.abspath(os.path.join(pwd,os.pardir))+os.path.sep+"book"+os.path.sep+name
        isExists = os.path.exists(path)
        if not isExists:            #生成各个tag的目录
            os.mkdir(path)
        for id in t['questions']:
            for r in res:
                if r['question_id'] == id:
                    qpath = path+os.path.sep+r['question_title']
                    isExists = os.path.exists(qpath)
                    if not isExists:  # 生成各个tag的目录
                        os.mkdir(qpath)

if __name__ == "__main__":
    tag = tags.tags()
    generate(tag)