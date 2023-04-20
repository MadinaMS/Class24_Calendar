class DateTimeError(Exception):
    def __init__(self, component, value, message):
        self.component = component
        self.value = value
        self.message = message

    def __str__(self):
        return f"Invalid value: {self.value} for {self.component}.It should be {self.message}"


class Date:
    def __init__(self, year, month, day):
        self.validate_date(year, month, day)
        self.year = year
        self.month = month
        self.day = day

    def validate_date(self, year, month, day):
        if not isinstance(year, int) or year < 0 or year > 9999:
            raise DateTimeError("year", year, "between 0 and 9999")
        if not isinstance(month, int) or month < 1 or month > 12:
            raise DateTimeError("month", month, "between 1 and 12")
        if not isinstance(day, int) or day < 1 or day > 31:
            raise DateTimeError("day", day, "between 1 and 31")

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"


class DateTime(Date):
    def __init__(self, year, month, day, hours, minutes, seconds):
        super().__init__(year, month, day)
        self.validate_time(hours, minutes, seconds)
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def validate_time(self, hours, minutes, seconds):
        if not isinstance(hours, int) or hours < 0 or hours > 23:
            raise DateTimeError("hours", hours, "between 0 and 23")
        if not isinstance(minutes, int) or minutes < 1 or minutes > 59:
            raise DateTimeError("minutes", minutes, "between 1 and 59")
        if not isinstance(seconds, int) or seconds < 1 or seconds > 59:
            raise DateTimeError("seconds", seconds, "between 1 and 59")

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day} \n {self.hours}:{self.month}:{self.seconds}"


try:
    date = Date(2023, 12, 30)
except DateTimeError as e:
    print(e)

try:
    time = DateTime(2023, 4, 15, 5,59, 59)
except DateTimeError as e:
    print(e)
