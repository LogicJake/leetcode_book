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
    try:
        r = requests.post(url, data=json.dumps(payload), headers=headers,timeout=5)
        r = r.text
        r = json.loads(r)['data']['question']['content']
        md = Tomd(r).markdown
        return md
    except:
        time.sleep(1)
        return get_question_detail(titleSlug)


def generate(tag):
    res = question.get_question()
    pwd = sys.path[0]
    md_path = os.path.abspath(os.path.join(pwd,os.pardir))+os.path.sep+"SUMMARY.md"
    f = open(md_path,"w",encoding="utf-8")
    f.write("# Summary  \n* [介绍](README.md)\n* [分类](book/book.md)")

    fp = open(os.path.abspath(os.path.join(pwd,os.pardir))+os.path.sep+"book"+os.path.sep+"book.md","w",encoding="utf-8")
    fp.write("## 分类列表  \n")
    fp.write("| 分类名称 | 个数 | \n")
    fp.write("|:---:|:---:|  \n")
    #根据tag生成文件夹
    for t in tag:
        name = t['name']
        ft = open(os.path.abspath(os.path.join(pwd,os.pardir))+os.path.sep+"book"+os.path.sep+name.strip()+os.path.sep+"list.md","w",encoding="utf-8")
        ft.write("## 题目列表  \n")
        ft.write("| 题目 | 难度 |  \n")
        ft.write("|:---:|:---:|  \n")

        f.write("  \n   * [{}]({})".format(name,"book/"+name+"/list.md"))
        path = os.path.abspath(os.path.join(pwd,os.pardir))+os.path.sep+"book"+os.path.sep+name
        isExists = os.path.exists(path)
        fp.write("| [{}]({})| {} |  \n".format(name,name.strip()+"/list.md",t['questions'].__len__()))
        if not isExists:            #生成各个tag的目录
            os.mkdir(path)
        for id in t['questions']:
            for r in res:
                if r['question_id'] == id:
                    level = ""
                    if r['difficulty'] == 1:
                        level = "简单"
                    elif r['difficulty'] == 2:
                        level = "中等"
                    elif r['difficulty'] == 3:
                        level = "困难"
                    if r['paid_only'] == True:
                        ft.write("| [{}]({}) :lock: | {} |   \n".format(r['question_title'],r['question_title'].strip()+"/question.md",level))
                    else:
                        ft.write("| [{}]({}) | {} |   \n".format(r['question_title'],r['question_title'].strip()+"/question.md",level))
                    qpath = path+os.path.sep+r['question_title'].strip()
                    isExists = os.path.exists(qpath)
                    f.write("  \n       * [" + r['question_title'].strip()+"](book/"+name.strip()+"/"+r['question_title'].strip()+"/question.md)")
                    if not isExists:  # 生成各个题目的目录
                        os.mkdir(qpath)
                    if r['paid_only'] != True:
                        pass
                        #md = "## " + r['question_title'] + "  \n### 链接  \nhttps://leetcode.com/problems/{}/description/".format(r['question_slug'])+"  \n### 问题描述" + get_question_detail(r['question_slug'])
                        # with open(qpath.strip()+os.path.sep+"question.md","w",encoding='utf-8') as ff:
                        #   ff.write(md)
                    else:
                        md = "## " + r['question_title'] + "  \n### 链接  \nhttps://leetcode.com/problems/{}/description/".format(r['question_slug'])
                        with open(qpath.strip() + os.path.sep + "question.md", "w", encoding='utf-8') as ff:
                            ff.write(md)
        ft.close()
    fp.close()
    f.close()

if __name__ == "__main__":
    tag = tags.tags()
    generate(tag)