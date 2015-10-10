__author__ = 'Ian'

import numbers
import decimal

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

months_abbvs = dict((m[:3].lower(), m) for m in months)


def valid_month(month):

    # Basically inside an if statement so that a None is returned automatically
    # when any argument whose first three letters are not int the dictionary
    # created by the for loop in the months_abbv declaration.

    if month:
        short_month = month[:3].lower()  # takes the first 3 letters, .lowercase()
        return months_abbvs.get(short_month)

        # uses get() on the dictionary to check for
        # the matching entry with short_month
        # if the input does not match, get()
        # automatically returns None

# print valid_month("january")
# # => "January"
# print valid_month("January")
# # => "January"
# print valid_month("feb")
# # => None
# print valid_month("")
# # => None


def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day

    # if isinstance (day, (int, float, complex)):
    #     if day >= 1 and day <= 31:
    #         return int(day)

#  print valid_day(10)


def valid_year(year):
    if isinstance(year, (int, float, complex)):
        year = int(year)
        if year >= 1900 and year <= 2020:
            return year

# String substitution!! This shit looks awesome.

a = "some bold text"

stuff = "<b>%s</b>" % a



given_string = "I think %s, and despite your opinion, %s, are perfectly normal things to do in public."


def sub1(s, d):
    return given_string % (s, d)

# print sub1("running", "shitting")
# # => "I think running is a perfectly normal thing to do in public."
# print sub1("sleeping", "drinking")
# # => "I think sleeping is a perfectly normal thing to do in public."

given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."


def sub_m(name, nickname):
    # sub_d = {'name': name,
    # 		 'nickname': nickname}
    return given_string2 % {"name": name,
                           "nickname": nickname}


print sub_m("Mike", "Goose")

