# coding: utf-8
import json
import os
import sys

import requests
import tags
import question
import time
from tomd import Tomd

def get_question_detail(titleSlug):
    url = "https://leetcode.com/graphql"
    headers = {
        "x-csrftoken":"hnCRhIP9Ds7eKh79lMiX3VrrFHoXgLuSUGZ6rXd6S99WeIUF70rhPxfRhStAFXhr",
        "referer":"https://leetcode.com/problems/",
        "cookie":"csrftoken=hnCRhIP9Ds7eKh79lMiX3VrrFHoXgLuSUGZ6rXd6S99WeIUF70rhPxfRhStAFXhr; expires=Fri, 22-Feb-2019 12:36:31 GMT; Max-Age=31449600; Path=/; secure",
        "Content-Type":"application/json"
    }
    payload = {
        "operationName": "getQuestionDetail",
        "variables":{"titleSlug":titleSlug},
        "query":"""
        query getQuestionDetail($titleSlug: String!) {
  isCurrentUserAuthenticated
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    questionTitle
    questionTitleSlug
    content
    difficulty
    stats
    contributors
    companyTags
    topicTags
    similarQuestions
    discussUrl
    mysqlSchemas
    randomQuestionUrl
    sessionId
    categoryTitle
    submitUrl
    interpretUrl
    codeDefinition
    sampleTestCase
    enableTestMode
    metaData
    enableRunCode
    enableSubmit
    judgerAvailable
    infoVerified
    envInfo
    urlManager
    article
    questionDetailUrl
    discussCategoryId
    discussSolutionCategoryId
    libraryUrl
  }
  interviewed {
    interviewedUrl
    companies {
      id
      name
    }
    timeOptions {
      id
      name
    }
    stageOptions {
      id
      name
    }
  }
  subscribeUrl
  isPremium
  loginUrl
}"""
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers).text
    r = json.loads(r)['data']['question']['content']
    md = Tomd(r).markdown
    return md

def generate(tag):
    res = question.get_question()
    pwd = sys.path[0]
    md_path = os.path.abspath(os.path.join(pwd,os.pardir))+os.path.sep+"SUMMARY.md"
    f = open(md_path,"w",encoding="utf-8")
    f.write("# Summary  \n* [介绍](README.md)\n* 分类")
    #根据tag生成文件夹
    for t in tag:
        name = t['name']
        f.write("  \n   * "+name)
        path = os.path.abspath(os.path.join(pwd,os.pardir))+os.path.sep+"book"+os.path.sep+name
        isExists = os.path.exists(path)
        if not isExists:            #生成各个tag的目录
            os.mkdir(path)
        for id in t['questions']:
            for r in res:
                if r['question_id'] == id and r['paid_only'] != True:
                    qpath = path+os.path.sep+r['question_title']
                    isExists = os.path.exists(qpath)
                    if not isExists:  # 生成各个题目的目录
                        os.mkdir(qpath)
                    #print(r['question_title'])
                    #md = "## "+r['question_title']+"  \n### "+"问题描述"+get_question_detail(r['question_slug'])
                    f.write("  \n       * [" + r['question_title']+"](book/"+name+"/"+r['question_title']+"/question.md)")
                    #with open(qpath+os.path.sep+"question.md","w",encoding='utf-8') as f:
                    #    f.write(md)
    f.close()

if __name__ == "__main__":
    tag = tags.tags()
    generate(tag)