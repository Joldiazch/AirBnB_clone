#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel():
    """ BaseModel Class """

    def __init__(self, *args, **kwargs):
        """  """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        self.updated_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

    def save(self):
        """ save method """
        updated_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

    def to_dict(self):  
        """ to_dict method """
        return self.__dict__

    def __str__(self):
        """ __str__ method """
        msg = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        return msg
        
