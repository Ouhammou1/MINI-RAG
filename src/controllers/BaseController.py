from  helpers.config import  get_settings, Settings

class BaseController:

    def __ini__(self):
        self.app_setting = get_settings()

