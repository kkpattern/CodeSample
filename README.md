576DIV2
=======
These code solves problems in TopCoder algorithm competition SRM 576DIV2.
This is my first SRM room win in TopCoder. These code is not writen in Python
but C++. But I think it shows that I am capable to write correct code under
time pressure.
I added the statement of each problem at the beginning of the source code.

microspider
===========
microspider is a library for crawling data on Sina Weibo(Chinese biggest
twitter-like website).

Weibo provides RESTful API for applications to fetch data. To make a request
one needs a valid access token. Also every access token has a limited number
of requests it can make per hour.

This library is organized as follows:
- microspider.api: This module implements the http request to Weibo API.
- microspider.robot: This module manages the robots. A robot is an user account
    with an access token for making API requests. Managing the robots means you
    can save a access token through a RobotManager and get the access token
    later for API request without worrying exceed the limit.
- microspider.fetcher: This module contains helper functors for users to fetch
    data from Weibo without using microspider.robot and microspider.api
    themselves.
- microspider.urllibx: This module provides extensions for urllib and urllib2.
    For now the only "important" class in this module is URLOpener. It provides
    an easy way to do http get/post request.

QualificationRound
==================
These code solves problems in Google codejam 2013 Qualification Round.
The problem A and B are solved in Python. The problem C with the small data
is solved in Python and the first large data is solved in C++.
I added the statement of each problem at the beginning of the source code.
