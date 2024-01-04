from datetime import datetime

class TimeConverter:
    def __init__(self, date_format="%Y-%m-%d %H:%M:%S"):
        self.date_format = date_format

    def string_to_unix_timestamp(self, date_time_string):
        """Convert a date and time string to Unix timestamp."""
        date_time_object = datetime.strptime(date_time_string, self.date_format)
        return int(date_time_object.timestamp())

    def unix_timestamp_to_string(self, unix_timestamp):
        """Convert Unix timestamp to date and time string."""
        date_time_object = datetime.utcfromtimestamp(unix_timestamp)
        return date_time_object.strftime(self.date_format)


converter = TimeConverter()

unix_timestamp_result = converter.string_to_unix_timestamp("2023-12-30 12:00:00")
print(f"Unix timestamp: {unix_timestamp_result}")

date_time_string_result = converter.unix_timestamp_to_string(unix_timestamp_result)
print(f"Date and time: {date_time_string_result}")
