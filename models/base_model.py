#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel():
    """ BaseModel Class """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ save method """
        updated_at = datetime.now()

    def to_dict(self):
        """ to_dict method """
        dic = self.__dict__
        dic ['__class__'] = self.__class__.__name__
        dic ['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dic ['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return dic

    def __str__(self):
        """ __str__ method """
        msg = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        return msg
        
