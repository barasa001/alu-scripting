#!/usr/bin/python3
"""Module for making a request to an API"""
import re
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """ recursive function that queries the Reddit API and return a list
    containing the titles of all hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'Python3/requests_library/1'}
    redirects = False
    if after is None:
        request_subreddit = requests.get(url, headers=headers,
                                         allow_redirects=redirects)
        print(request_subreddit.status_code)
    else:
        data = {'after': after}
        request_subreddit = requests.get(url, headers=headers, params=data,
                                         allow_redirects=redirects)
        print(request_subreddit.status_code)
    if count_dict is None:
        count_dict = {}
        for word in word_list:
            count_dict[word] = 0
    if request_subreddit.status_code == 200:
        subreddit_json = request_subreddit.json()
        for children in subreddit_json['data']['children']:
            title = children['data']['title']
            for k, v in count_dict.items():
                if (re.findall(re.compile("({})(\s|$)".format(k)), title)):
                    v = v + len(re.findall(k, title))
                count_dict[k] = v
        end_value = subreddit_json['data']['after']
        if end_value is None:
            new_dict = {}
            for k, v in count_dict.items():
                key = new_dict.get(v, None)
                if key is None:
                    new_dict[v] = list() + [k]
                else:
                    new_dict[v].append(k)
            new_list = list(new_dict.keys())
            new_list.sort(reverse=True)
            for number in new_list:
                for word in new_dict[number]:
                    print(word + ": " + str(number))
            return
        count_words(subreddit, word_list, end_value, count_dict)
