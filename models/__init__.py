#!/usr/bin/python3
"""call filestorage class"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
