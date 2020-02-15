#!/usr/bin/python3
"""Contain the class FileStorage"""
from models.base_model import BaseModel
import json
import os

class FileStorage():
	""" FileStorage Class """

        __file_path = "file.json"
        __objects = {}

	def all(self):
		"""Return all objects from dictionary __objects"""
		return self.__objects

	def new(self, obj):
		"""Set in __objects with key <obj class name>.id"""
		self.__objects["{}.{}".format(obj.__class__.__name__, obj.id] = obj

	def save(self):
		"""serializes __objects to the JSON file (path: __file_path)"""
		with open(self.__file_path, "w", enconding="UTF-8") as file:
                               obj_dict = {name_attr: value.to_dict() for name_attr, value in self.__objects.items()}
                               json.dump(obj_dict, file)
	def reload(self):
                """deserialization the JSON file to __objects, only JS"""
