#!/usr/bin/python3
from .engine.file_storage import FileStorage

storage = FileStorage("./models/engine/database/storage_db.json")
storage.reload()
