#!/usr/bin/env python
# coding: utf-8

# In[305]:


import requests
import matplotlib.pyplot as plt
import json
class StackOverflowAPI:
    def __init__(self):
        self.main = 'https://api.stackexchange.com/'
        self.everything = '2.3/questions?order=desc&sort=activity&site=stackoverflow'

    def get_data(self, endpoint):
        response = requests.get(self.main + endpoint)
        return json.loads(response.text)

    def get_everything(self):
        response_json = self.get_data(self.everything)
        return response_json

    def get_tag_count(self, parse_json):
        count = 0
        set1 = set()
        list1 = []
        for i in range(len(parse_json['items'])):
            for j in range(len(parse_json['items'][i]['tags'])):
                set1.add(parse_json['items'][i]['tags'][j])
                list1.append(parse_json['items'][i]['tags'][j])
        m = {}
        for i in range(len(set1)):
            m[list(set1)[i]] = list1.count(list(set1)[i])
        print('Plot of first 5 tags with count')
        plt.plot(list(m.keys())[:5], list(m.values())[:5])
        return m

    def plot_top_tags(self, dict_count_tags, number):
        dict_count_tags = dict(sorted(dict_count_tags.items(), key=lambda x: x[1], reverse=True))
        print("The plot of top " + str(number) + " tags")
        plt.plot(list(dict_count_tags.keys())[:number], list(dict_count_tags.values())[:number])

    def get_is_answered_true(self, parse_json):
        count = 0
        print('The account_ids are')
        for i in range(len(parse_json['items'])):
            if parse_json['items'][i]['is_answered'] == True:
                print(parse_json['items'][i]['owner']['account_id'])
                count += 1
        print('The count of answered true is ' + str(count))

    def get_question_answers(self, id1):
        get_with_id = "/2.3/questions/" + str(id1) + "/answers?order=desc&sort=activity&site=stackoverflow"
        response_API_id = requests.get(self.main+get_with_id)
        parse_json1 = json.loads(response_API_id.text)
        print(parse_json1)
        return parse_json1


# In[306]:


api = StackOverflowAPI()
data = api.get_everything()

tag_count = api.get_tag_count(data)

api.get_is_answered_true(data)

api.plot_top_tags(tag_count, 5)
#This gives the top 5 tags used

question_answers = api.get_question_answers(76633777)
#this gives answer based on question id
