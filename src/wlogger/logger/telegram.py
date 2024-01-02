from src.wlogger.logger.baselogger import BaseLogger


class TelegramLoggerEntity(BaseLogger):
    def __init__(self, token, **kwargs):
        self.token: str = token
        self._web_preview: bool = True
        self._notification: bool = True
        self._parse_mode: str = 'HTML'
        self._custom_message: bool = False
        self._message = '[{0}]\n{1}\n\n{2}'
        print('TG created')

    @property
    def message(self) -> str:
        return self._message

    @property
    def web_preview(self):
        return self._web_preview

    @property
    def notification(self):
        return self._notification

    @property
    def parse_mode(self):
        return self._parse_mode

    @web_preview.setter
    def web_preview(self, value: bool):
        if not isinstance(value, bool):
            # TODO: Заменить на кастомное исключение
            raise TypeError()
        self._web_preview = value

    @notification.setter
    def notification(self, value: bool):
        if isinstance(value, bool):
            self._notification = value
        else:
            # TODO: Заменить на кастомное исключение
            raise TypeError()


    @parse_mode.setter
    def parse_mode(self, value: str):
        if not isinstance(value, str):
            # TODO: Заменить на кастомное исключение
            raise TypeError()
        if value not in ('HTML', 'MarkdownV2'):
            # TODO: Заменить на кастомное исключение
            raise ValueError()
        self._parse_mode = value

    @message.setter
    def message(self, value):
        self._custom_message: bool = True
        self._message = value

    def _send_message(self):
        pass

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
    @classmethod
    def create(cls, **kwargs) -> TelegramLoggerEntity:
        return TelegramLoggerEntity(token=kwargs['token'])
