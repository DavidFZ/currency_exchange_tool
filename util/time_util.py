import datetime


class TimeUtil:
    @staticmethod
    def get_current_date():
        return str(datetime.datetime.now().date())
