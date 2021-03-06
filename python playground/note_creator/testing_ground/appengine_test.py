#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# import webapp2

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
    if month:
        short_month = month[:3].lower()  # takes the first 3 letters, .lowercase()
        return months_abbvs.get(short_month)


def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if 0 < day <= 31:  # Simplified to a chained comparison
            return day


def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year >= 1900 and year <= 2020:
            return year


form = '''<form method="post">
    What is your birthday?
    <br>

    <label>Month<input type="text" name="month"></label>
    <label>Day<input type="text" name="day"><label>
    <label>Year<input type="text" name="year"></label>
    <div style="color": red>%(error)s</div>


    <br>
    <br>
    <input type="submit">
    </form>
'''


# class MainPage(webapp2.RequestHandler):

def write_form(self, error=""):
    #  lf.response.out.write(form % {"error": error})
    print(form % {"error": error})


def get(self):
    self.write_form()


def post(self):
    user_month = valid_month(self.request.get('month'))
    user_day = valid_day(self.request.get('day'))
    user_year = valid_year(self.request.get('year'))

    if not (user_month and user_day and user_year):
        self.write_form("This is not valid dood.")
    else:
        self.response.out.write("Thank you that is a valid day.")


# app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

write_form("Whoah bro")
