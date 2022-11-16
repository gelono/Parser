from datetime import datetime

def date_format(self, string):
    string = string.split()
    month_dict = {
        'січ': 1,
        'лют': 2,
        'бер': 3,
        'квіт': 4,
        'трав': 5,
        'черв': 6,
        'лип': 7,
        'серп': 8,
        'верес': 9,
        'жовт': 10,
        'лист': 11,
        'груд': 12,
    }
    for month in month_dict:
        if string[1].lower().find(month) != -1:
            string[1] = str(month_dict[month])

    string = string[0] + '.' + string[1] + '.' + string[2]
    date_formatter = '%d.%m.%Y'
    date = datetime.strptime(string, date_formatter)
    date = date.date()
    return date
