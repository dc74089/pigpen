import random
import string

import requests
from ics import Calendar


def gen_token():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(50))


def time_to_string(time):
    try:
        if "day" in str(time):
            days = str(time).split(" day")[0]
            rest = str(time).split(", ")[1]
            total = str(rest).split(":")
            return "{}h {}m".format(int(total[0]) + (24 * int(days)), int(total[1]))
        else:
            total = str(time).split(":")
            return "{}h {}m".format(total[0], int(total[1]))
    except IndexError:
        return "0m"


def get_calendar():
    url = "https://calendar.google.com/calendar/ical/explodingbacon.team1902%40gmail.com/public/basic.ics"
    return Calendar(requests.get(url).text)
