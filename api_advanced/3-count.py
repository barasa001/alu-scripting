#!/usr/bin/python3
""" 3. Count it! """
from requests import get


def count_words(subreddit, word_list):
    """ recursive function that queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords. """
        headers = {"User-Agent": "javierandresgp"}
