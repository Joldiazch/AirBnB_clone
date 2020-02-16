#!/usr/bin/python3
""" import FileStorage module"""
from .engine.file_storage import FileStorage

""" Create storage instance for reload objets"""
storage = FileStorage()
storage.reload()
