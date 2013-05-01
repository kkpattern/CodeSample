# Copyright (C) 2012 Kai Zhang

"""
API for Sina Weibo.
"""

import json
import logging
import time
import urllib

import microspider.log
import microspider.proxy
import microspider.robot
import microspider.urllibx

API_HOST = "api.weibo.com"

class WeiboAPI(object):
    """API for sina Weibo."""
    def __init__(self):
        self.robot_manager = microspider.robot.RobotManager()
        self.proxy_manager = microspider.proxy.ProxyManager()
        self.url_opener = microspider.urllibx.URLOpener(redirect=False)

    def auth(self, username, password, app_key, app_secret, auth_callback):
        """
        Make user auth request.

        @param username: The user's name.
        @type username: C{str}.

        @param password: The user's password.
        @type password: C{str}.

        @param app_key: The key of the Weibo app.
        @type app_key: C{str}.

        @param app_secret: The secret of the Weibo app.
        @type app_secret: C{str}.

        @param auth_callback: The url which the user will be redirected to
            after the auth.
        @type auth_callback: C{str}.
        """
        params = {
            'action':'submit', 'withOfficalFlag':'0',
            'ticket':'', 'isLoginSina':'',
            'response_type':'code', 'regCallback':'',
            'redirect_uri': auth_callback, 
            'client_id':app_key, 'state':'', 'from':'',
            'userId':username,
            'passwd':password,}

        login_url = 'https://api.weibo.com/oauth2/authorize'  
        auth_param = urllib.urlencode({
            "client_id": app_key,
            "response_type": "code",
            "redirect_uri": auth_callback})
        auth_url = login_url+'?'+auth_param
        self.url_opener.http_get(auth_url)

        headers = {'Referer': auth_url}
        try:
            self.url_opener.http_post(login_url, params, headers)
        except microspider.urllibx.RedirectError as e:
            newurl = e.new_url()
            code = newurl.split('=')[-1]
            data = self.get_access_token(code, app_key, app_secret, auth_callback)
            return data


    def get_access_token(self, code, key, secret, auth_callback):
        """
        Use the code returned from Weibo to get the access token.

        @param code: The code returned from Weibo.
        @type code: C{str}.

        @param key: The key of the Weibo app.
        @type key: C{str}.

        @param secret: The secret of the Weibo app.
        @type secret: C{str}.

        @param auth_callback: The url which the user will be redirected to
            after the auth.
        @type auth_callback: C{str}.
        """
        params = urllib.urlencode({
            "client_id" : key,
            "client_secret" : secret,
            "grant_type" : "authorization_code",
            "redirect_uri" : auth_callback,
            "code": code})
        url = "https://api.weibo.com/oauth2/access_token?" + params
        data = self.url_opener.http_post(url)
        return json.loads(data)

    def make_api_request(self, url, method="GET", **kargs):
        """
        Make an API requset.

        @param url: The requested API url.
        @type url: C{str}.

        @param method: The method that used to request. Should be "GET" or
            "POST"
        @param method: C{str}.

        @param kargs: The arguments required by the API.
        """
        parameters = {}
        for key in kargs:
            parameters[key] = kargs[key]
            method = method.upper()
            if method == "GET":
                raw_data = self.url_opener.http_get(url, parameters)
            elif method == "POST":
                raw_data = self.url_opener.http_post(url, parameters)
            else:
                raise ValueError("Method should be GET or POST")
        try:
            return json.loads(raw_data)
        except ValueError:
            raise IOError("Invalid json data")

    def statuses_public_timeline(self, **kargs):
        """Call the /2/statuses/public_timeline.json api."""
        return self.make_api_request(
            "https://"+API_HOST+"/2/statuses/public_timeline.json",
            method="GET",
            **kargs)

    def statuses_user_timeline(self, **kargs):
        """Call the /2/statuses/user_timeline.json api."""
        return self.make_api_request(
            "https://"+API_HOST+"/2/statuses/user_timeline.json",
            method="GET",
            **kargs)

    def statuses_repost_timeline(self, **kargs):
        """Call the /2/statuses/repost_timeline.json api."""
        return self.make_api_request(
            "https://"+API_HOST+"/2/statuses/repost_timeline.json",
            method="GET",
            **kargs)

    def comments_show(self, **kargs):
        """Call the /2/comments/show.json api."""
        return self.make_api_request(
            "https://"+API_HOST+"/2/comments/show.json",
            method="GET",
            **kargs)

    def statuses_count(self, access_token, ids):
        """Call the /2/statuses/countjson."""
        ids_string = ""
        for one in ids:
            ids_string += (str(one)+',')
            return self.make_api_request(
                "https://"+API_HOST+"/2/statuses/count.json",
                method="GET",
                access_token=access_token, ids=ids_string)

    def friendships_friends_json(self, **kargs):
        """Call the /2/friendships/friends.json api."""
        return self.url_opener.http_get(
            "https://"+API_HOST+"/2/friendships/friends.json",
            kargs)
