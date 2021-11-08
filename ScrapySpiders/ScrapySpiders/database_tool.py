# -*- coding: utf-8 -*-
# @Author  : CharesFuns
# @Time    : 2020/6/21 0:38
# @Function: 

import pymongo
from scrapy.utils.project import get_project_settings


class DBConnector:
    def __init__(self):
        settings = get_project_settings()
        self.mongo_host = settings.get("MONGO_HOST")
        self.mongo_port = settings.get("MONGO_PORT")
        self.mongo_database = settings.get("DB_NAME")

    def create_mongo_connection(self):
        client = pymongo.MongoClient(self.mongo_host, self.mongo_port)
        database = client[self.mongo_database]
        return database, client
