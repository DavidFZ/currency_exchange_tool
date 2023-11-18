import datetime as dt


class DateUtil:
    @staticmethod
    def global_date_format():
        return '%Y-%m-%d'

    @staticmethod
    def convert_timestamp_to_date(timestamp):
        date = dt.datetime.fromtimestamp(timestamp)
        return date.strftime(DateUtil.global_date_format())


if __name__ == '__main__':
    print(DateUtil.convert_timestamp_to_date(1700272623))
