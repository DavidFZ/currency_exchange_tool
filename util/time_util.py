import datetime


class TimeUtil:
    @staticmethod
    def get_current_date():
        """
        get current date
        formate sample: 2023-11-23

        :return current_date: current date string
        """
        return str(datetime.datetime.now().date())
