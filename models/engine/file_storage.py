#!/usr/bin/python3
"""Contain the class FileStorage"""
from models.base_model import BaseModel
import json

class FileStorage():
	""" FileStorage Class """
	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""Return all objects from dictionary __objects"""
		return self.__objects

	def new(self, obj):
		"""Set in __objects with key <obj class name>.id"""
		self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

	def save(self):
		"""serializes __objects to the JSON file (path: __file_path)"""
		with open(self.__file_path, mode='w', encoding='utf-8') as f:
			obj_dict = {key_obj: obj.to_dict() for key_obj, obj in self.__objects.items()}
			json.dump(obj_dict, f)

	def reload(self):
		"""deserialization the JSON file to __objects, only JS"""
		try:
			with open(self.__file_path, mode='r', encoding='utf-8') as f:
				all_objs = json.loads(f.read())
			for obj_id in all_objs.keys():
				obj = all_objs[obj_id]
				self.new(BaseModel(**obj))
		except:
			pass


