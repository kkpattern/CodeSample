# Copyright (C) 2012 Kai Zhang

import microspider.api
import microspider.robot

class BaseFetcher(object):
    def __init__(self, robot_manager=None, api=None):
        self.robot_manager = robot_manager
        if not robot_manager:
            self.robot_manager = microspider.robot.RobotManager()
        self.api = api
        if not api:
            self.api = microspider.api.WeiboAPI()

class UserTimelineFetcher(BaseFetcher):
    """Functor of fetching user timeline."""
    def __call__(self, uid_or_screen_name, since_id=0, max_id=0,
                 count=100, page=1, base_app=0, feature=0, trim_user=0):
        robot = self.robot_manager.get_available_robot()
        kargs = {"access_token": robot.access_token,
                 "since_id": since_id,
                 "max_id": max_id,
                 "count": count,
                 "page": page,
                 "base_app": base_app,
                 "feature": feature,
                 "trim_user": trim_user}
        if type(uid_or_screen_name) is int:
            kargs["uid"] = uid_or_screen_name
        else:
            kargs["screen_name"] = uid_or_screen_name
        return self.api.statuses_user_timeline(**kargs)
 

class StatusesRepostTimelineFetcher(BaseFetcher):
    """Functor of fetching status' repost timeline."""
    def __call__(self, id, since_id=0, max_id=0,
                 count=200, page=1, filter_by_author=0):
        robot = self.robot_manager.get_available_robot()
        return self.api.statuses_repost_timeline(
            access_token=robot.access_token,
            id=id, since_id=since_id, max_id=max_id,
            count=count, page=page, filter_by_author=filter_by_author)

class CommentsShowFetcher(BaseFetcher):
    """Functor of fetching comments."""
    def __call__(self, id, since_id=0, max_id=0,
                 count=200, page=1, filter_by_author=0):
        robot = self.robot_manager.get_available_robot()
        return self.api.comments_show(
            access_token=robot.access_token,
            id=id, since_id=since_id, max_id=max_id,
            count=count, page=page, filter_by_author=filter_by_author)
