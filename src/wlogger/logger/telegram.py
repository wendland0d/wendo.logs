import urllib3

from baselogger import BaseLogger


class TelegramLoggerEntity(BaseLogger):
    def __init__(self, token, **kwargs):
        self.token: str = token
        self.web_preview: bool = True
        self.notification: bool = True
        self.parse_mode: str = 'HTML'

        if kwargs['disable_web_page_preview']:
            self.disabled_web_preview = True
        if kwargs['disable_notification']:
            self.notification = False

    def debug(self):
        pass

    def info(self):
        pass

    def warning(self):
        pass

    def error(self):
        pass

    def critical(self):
        pass


class TelegramLogger:
    def __call__(self, *args, **kwargs) -> TelegramLoggerEntity:
        return TelegramLoggerEntity()
