class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def convert(cls, date):
        values = list(map(int, date.split('-')))
        if Date.valid(*values):
            return values
        else:
            raise ValueError ('Неверный формат даты')

    @staticmethod
    def valid(day, month, year):
        if isinstance(year, int) and isinstance(month, int) and isinstance(day, int) and month > 0 and day > 0:
            if month < 13:
                if (month in [1, 3, 5, 7, 8, 10, 12] and day < 32) or \
                        (month in [4, 6, 9, 11] and day < 31) or \
                        (month == 2 and ((year % 4 == 0 and day < 30) or (day < 29))):
                    return True
        return False

print(Date.convert('31-12-2021'))
print(type(Date.convert('31-12-2021')[0]))