#!/usr/bin/python3
"""
module: db_storage
"""
from os import getenv

class DBStorage:
    """
    New database engine
    """

    __engine = None
    __sission = None


    def __init__(self):
        """
        Initializes the value and links to database
        """

        self.__engine = create_engine('mysql + mysqldb://{}:{}@{}/{}'.format(user, password, host, db), pull_pre_ping=True)

