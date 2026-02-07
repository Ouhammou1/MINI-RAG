from .BaseController import BaseController
from fastapi import UploadFile


class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 104876

    def validate_upload_file(self  , file: UploadFile):
        if file.content_type not in self.app_setting.FIILE_ALLOWED_TYPE:
            return False

        if  file.size > self.app_setting.FILE_MAX_SIZE * self.size_scale :
            return False
        return True
    