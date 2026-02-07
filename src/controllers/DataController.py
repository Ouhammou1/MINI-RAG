from .BaseController import BaseController
from fastapi import UploadFile


class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576

    def validate_upload_file(self, file: UploadFile):
        allowed_types = self.app_setting.FILE_ALLOWED_TYPE.split(",")

        if file.content_type not in allowed_types:
            return False

        contents = file.file.read()
        size = len(contents)
        file.file.seek(0)

        if size > self.app_setting.FILE_MAX_SIZE * self.size_scale:
            return False

        return True
