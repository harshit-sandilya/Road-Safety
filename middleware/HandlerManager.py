from core.Handler import Handler
from fastapi import HTTPException
from datetime import datetime, timedelta
import time


class HandlerManager:
    def __init__(self, ttl_seconds: int):
        self.handlers = {}
        self.ttl_seconds = ttl_seconds

    def add_handler(self, language: str, handler_id: int = None):
        if handler_id is None:
            handler_id = int(datetime.now().timestamp() * 1000)
        self.handlers[handler_id] = {
            "handler": Handler(language),
            "created_at": datetime.now(),
            "last_accessed": datetime.now(),
            "language": language,
        }
        return handler_id

    def get_handler(self, handler_id: int):
        if handler_id in self.handlers:
            handler_info = self.handlers[handler_id]
            if datetime.now() - handler_info["last_accessed"] < timedelta(
                seconds=self.ttl_seconds
            ):
                handler_info["last_accessed"] = datetime.now()
                return handler_info["handler"]
            else:
                self.add_handler(handler_info["language"], handler_id)
                return handler_info["handler"]
        else:
            raise HTTPException(status_code=404, detail="Handler not found")

    def garbage_collect(self):
        for handler_id in list(self.handlers.keys()):
            handler_info = self.handlers[handler_id]
            if datetime.now() - handler_info["last_accessed"] > timedelta(
                seconds=self.ttl_seconds
            ):
                print(f"Removing handler {handler_id}")
                del self.handlers[handler_id]
        return len(self.handlers)

    def get_live_handlers(self):
        return len(self.handlers)
