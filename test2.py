from datetime import datetime, timedelta

datetime_str = '2021-06-04'

datetime_object = datetime.strptime(datetime_str, "%Y-%m-%d")
datetime_object += timedelta(days=1)
datetime_object = datetime_object.date()
datetime_object.strftime("%Y-%m-%d")

print(datetime_object)  # printed in default format