# coding: utf-8
import json
import os
import sys
import requests
import time
import logging
from tomd import Tomd

logging.basicConfig(level=logging.INFO)

x_csrftoken = "OAGVxT8dthbhTowFhIJfWD4OtqiLOoaToUuOWVjz5Z4WLU1JnWqb8jynec5z2whj"
cookie = "gr_user_id=ebe856a8-1d10-46dc-834f-8f4a279c923a; a2873925c34ecbd2_gr_session_id=d09eca00-021f-4bdb-bb2d-158a304f24b6; grwng_uid=683b6b4f-28fc-4e62-84c1-3131f8ba7a0a; a2873925c34ecbd2_gr_session_id_d09eca00-021f-4bdb-bb2d-158a304f24b6=true; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1542191414,1542191440; csrftoken=OAGVxT8dthbhTowFhIJfWD4OtqiLOoaToUuOWVjz5Z4WLU1JnWqb8jynec5z2whj; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1542191800"

query = '''
query getQuestionDetail($titleSlug: String!) {
      isCurrentUserAuthenticated
      question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        questionTitle
        translatedTitle
        questionTitleSlug
        content
        translatedContent
        difficulty
        stats
        allowDiscuss
        contributors {
          username
          profileUrl
          __typename
        }
        similarQuestions
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
        langToValidPlayground
        enableRunCode
        enableSubmit
        judgerAvailable
        infoVerified
        envInfo
        urlManager
        article
        questionDetailUrl
        libraryUrl
        companyTags {
          name
          slug
          translatedName
          __typename
        }
        companyTagStats
        topicTags {
          name
          slug
          translatedName
          __typename
        }
        __typename
      }
      interviewed {
        interviewedUrl
        companies {
          id
          name
          slug
          __typename
        }
        timeOptions {
          id
          name
          __typename
        }
        stageOptions {
          id
          name
          __typename
        }
        __typename
      }
      subscribeUrl
      isPremium
      loginUrl
    }'''


class LeetCodeDownLoad(object):

    def get_question_detail(self, titleSlug):
        url = "https://leetcode-cn.com/graphql"
        headers = {
            "x-csrftoken": x_csrftoken,
            "referer": "https://leetcode-cn.com",
            "cookie": cookie,
            "Content-Type": "application/json"
        }
        payload = {
            "operationName": "getQuestionDetail",
            "variables": {"titleSlug": titleSlug},
            "query": query
        }

        try:
            r = requests.post(url, data=json.dumps(
                payload), headers=headers, timeout=5)
            r = json.loads(r.text)['data']['question']['content']
            md = Tomd(r).markdown
            return md
        except Exception as e:
            logging.error(e)
            time.sleep(1)
            return self.get_question_detail(titleSlug)

    def get_questions(self):
        # get question list from api
        url = "https://leetcode-cn.com/api/problems/all/"
        list = json.loads(requests.get(url).text)

        infos = list['stat_status_pairs']
        questions = {}
        for info in infos:
            question_id = info['stat']['question_id']
            tmp = {}
            tmp['paid_only'] = info['paid_only']  # 是否有锁
            tmp['difficulty'] = info['difficulty']['level']  # 困难等级
            tmp['question_title'] = info['stat']['question__title']  # 题目
            tmp['question_article_live'] = info['stat'][
                'question__article__live']  # 是否存在solution
            tmp['question_slug'] = info['stat']['question__title_slug']  # 连接地址
            questions[question_id] = tmp
        self.questions = questions

    def get_tags(self):
        # get question list from api
        url = "https://leetcode-cn.com/problems/api/tags/"
        list = json.loads(requests.get(url).text)

        self.tags = list["topics"]

    def generate(self):
        pwd = sys.path[0]

        summary_path = os.path.abspath(os.path.join(
            pwd, os.pardir)) + os.path.sep + "SUMMARY.md"

        book_path = os.path.abspath(os.path.join(
            pwd, os.pardir)) + os.path.sep + "book" + os.path.sep + "book.md"
        summary = open(summary_path, "w", encoding="utf-8")
        summary.write("# Summary  \n* [介绍](README.md)\n* [分类](book/book.md)")

        book = open(book_path, "w", encoding="utf-8")
        book.write("## 分类列表  \n")
        book.write("| 分类名称 | 个数 | \n")
        book.write("|:---:|:---:|  \n")

        tags_num = len(self.tags)
        tag_index = 1
        for tag in self.tags:
            tag_name = tag['name'].strip().lower().replace(" ", "-")

            logging.info('curreent tag: ' + tag_name + '\t' +
                         str(tag_index) + '/' + str(tags_num))
            tag_index += 1
            questions_num = len(tag['questions'])

            summary.write("  \n   * [{}]({})".format(tag['name'],
                                                     "book/" + tag_name.strip() + "/list.md"))

            tag_path = os.path.abspath(os.path.join(
                pwd, os.pardir)) + os.path.sep + "book" + os.path.sep + tag_name
            # 生成各个tag的目录
            if not os.path.exists(tag_path):
                os.mkdir(tag_path)

            book.write("| [{}]({})| {} |  \n".format(
                tag['name'], tag_name + "/list.md", questions_num))

            questions_path = os.path.abspath(os.path.join(
                pwd, os.pardir)) + os.path.sep + "book" + os.path.sep + tag_name + os.path.sep
            question_list = open(questions_path +
                                 "list.md", "w", encoding="utf-8")
            question_list.write("## 题目列表  \n")
            question_list.write("| 题目 | 难度 |  \n")
            question_list.write("|:---:|:---:|  \n")

            question_index = 1
            for id in tag['questions']:
                try:
                    question = self.questions[id]
                except KeyError as e:
                    logging.error('key error: ' + str(e))
                    continue
                logging.info('question: ' + question['question_title'] + '\t' + str(question_index) +
                             ' /' + str(questions_num))
                question_index += 1
                level = ""
                if question['difficulty'] == 1:
                    level = "简单"
                elif question['difficulty'] == 2:
                    level = "中等"
                elif question['difficulty'] == 3:
                    level = "困难"
                if question['paid_only'] == True:
                    question_list.write("| [{}]({}) :lock: | {} |   \n".format(
                        question['question_title'], question['question_slug'].strip() + "/question.md", level))
                else:
                    question_list.write("| [{}]({}) | {} |   \n".format(question['question_title'], question[
                        'question_slug'].strip() + "/question.md", level))

                # 生成各个题目的目录
                qpath = questions_path + question['question_slug'].strip()
                if not os.path.exists(qpath):
                    os.mkdir(qpath)
                summary.write(
                    "  \n       * [{}]({})".format(question['question_title'].strip(), qpath + "/question.md"))

                if question['paid_only'] == False:
                    md = "## " + question['question_title'] + "  \n### 链接  \nhttps://leetcode.com/problems/{}/description/".format(
                        question['question_slug']) + "  \n### 问题描述" + self.get_question_detail(question['question_slug'])
                    with open(qpath.strip() + os.path.sep + "question.md", "w", encoding='utf-8') as ff:
                        ff.write(md)
                else:
                    md = "## " + question['question_title'] + "  \n### 链接  \nhttps://leetcode.com/problems/{}/description/".format(question[
                        'question_slug'])
                    with open(qpath.strip() + os.path.sep + "question.md", "w", encoding='utf-8') as ff:
                        ff.write(md)
            question_list.close()
        book.close()
        summary.close()

    def run(self):
        self.get_questions()
        logging.info('get questions over!')
        self.get_tags()
        logging.info('get tags over!')
        self.generate()


if __name__ == "__main__":
    leetcode = LeetCodeDownLoad()
    leetcode.run()
