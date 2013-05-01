# Copyright (c) 2012 zhangkai

"""
Utility functions for microspider.
"""

import datetime

import pymongo

import microspider.settings

DATETIME_FORMAT = "%a %b %d %H:%M:%S %Y"

def parse_weibo_datetime(datetime_string):
    datetime_list = datetime_string.split(' ')
    utc_offset_string = datetime_list[-2]
    datetime_list.remove(utc_offset_string)

    datetime_string_without_timezone = ""
    for one in datetime_list:
        datetime_string_without_timezone += (one+' ')
        weibo_datetime = datetime.datetime.strptime(
            datetime_string_without_timezone.strip(),
            DATETIME_FORMAT)
        return weibo_datetime

def get_weibo_spider_db():
    return pymongo.Connection(
        microspider.settings.DATABASE_SERVER)["weibo_spider"]
