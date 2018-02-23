# coding: utf-8
import json
import os
import requests
import sys
import pymongo

def tags():
    # get question list from api
    # url = "https://leetcode.com/problems/api/tags/"
    # list = json.loads(requests.get(url).text)

    # get question list from local file
    config_file = sys.path[0] + os.path.sep +"tags.json"
    with open(config_file, 'r') as f:
        list = json.load(f)

    return list["topics"]

if __name__ == "__main__":
    tags()