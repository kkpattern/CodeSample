# Copyright (c) 2012 zhangkai

"""
Robot is an Weibo account used to make the API requests.
"""

import datetime
import logging
import pymongo
import time

import microspider.settings

TASK_BUFFER_LENGTH = 10

class NoRobotAvailable(Exception):
    pass

class Robot(object):
    """
    Robot class.

    uid: the uid of the robot account.
    access_token: the access_token of the robot account.
    auth_datetime: when the access_token is granted.
    last_request: the datetime of the last request.
    """
    def __init__(self, robot):
        self.uid = robot["_id"]
        self.access_token = robot["access_token"]
        self.expires_at = robot["expires_at"]
        # self.auth_datetime = robot["auth_datetime"]
        self.limit_per_hour = robot["limit_per_hour"]
        self.next_avaiable_time = robot["next_avaiable_time"]

class RobotManager(object):
    """Manage robot accounts."""
    def __init__(self, database_server=None, database_name=None):
        if not database_server:
            database_server = microspider.settings.DATABASE_SERVER
        db_connection = pymongo.Connection(database_server)
        if not database_name:
            database_name = "weibo_spider"
        db = db_connection[database_name]
        self.robots = db.robots
        self.__logger = logging.getLogger(__name__)

    def get_robots(self):
        """Get all the robots."""
        for robot in self.robots.find():
            yield Robot(robot)

    def save_robot(self, robot_id, access_token,
                   expires_at, limit_per_hour, next_avaiable_time=None):
        """Save a robot in database.

        @param robot_id: The id of the robot account.
        @type robot_id: C{int}

        @param access_token: The access token of the robot account.
        @type access_token: C{str}

        @param expires_at: The datetime when the access token expires.
        @type expires_at: C{datetime.datetime}.

        @param limit_per_hour: The requests this robot can make per hour.
        @type limit_per_hour: C{int}

        @param next_avaiable_time: The datetime this robot is available. If
            supplied None the C{next_avaiable_time} will be
            C{datetime.datetime.utcnow()}
        @type next_avaiable_time: C{datetime.datetime}
        """
        if not next_avaiable_time:
            next_avaiable_time = datetime.datetime.utcnow()
        self.robots.save({"_id": robot_id,
                          "access_token": access_token,
                          "expires_at": expires_at,
                          "limit_per_hour": limit_per_hour,
                          "next_avaiable_time": next_avaiable_time,
                          "processing": False})

    def get_available_robot(self, block=True):
        """Get an available robot.
        
        @param block: Whether or not the function will block if there is no
            available robot now.
    
        @return: A L{Robot} instance or None if there is no robot available.
        """
        now = datetime.datetime.utcnow()
        # get a robot which is not expired.
        robot = self.robots.find_and_modify(
                query={
                    "processing": False,
                    "expires_at": {"$gt" : now}},
                update={"$set": {"processing" : True}},
                sort={"next_avaiable_time": 1},
                new=True)
        if not robot:
            return None
        # update the next_avaiable_time.
        cooldown = datetime.timedelta(seconds=60.0*60.0/robot["limit_per_hour"])
        if robot["next_avaiable_time"] > now:
            time_to_sleep = robot["next_avaiable_time"]-now
            # NOTE:
	    robot["next_avaiable_time"] += cooldown
            # time to sleep in seconds
            time_to_sleep = time_to_sleep.seconds + time_to_sleep.days*24*3600
        else:
	    robot["next_avaiable_time"] = now+cooldown
            time_to_sleep = 0
        robot["processing"] = False
        self.robots.save(robot)
        # wait untill it's available.
        self.__logger.info("access_token:{0}, time_to_sleep:{1}".format(
            robot["access_token"], time_to_sleep))
        if block:
            time.sleep(time_to_sleep)
        return Robot(robot)
