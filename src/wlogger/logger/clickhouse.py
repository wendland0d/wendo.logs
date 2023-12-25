from baselogger import BaseLogger


class ClickHouseEntity(BaseLogger):
    def __init__(self):
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


class ClickhouseLogger:
    def __call__(self, *args, **kwargs) -> ClickHouseEntity:
        pass
