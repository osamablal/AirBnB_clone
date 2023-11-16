#!/usr/bin/python3
"""
Creating unique file storage at instanc for our app.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

