# encoding=utf-8
import json
import datetime
import urllib.parse
import urllib.request
from os import environ

json_parse = lambda url:json.loads(urllib.request.urlopen(url).read().decode("utf-8"))

def get_holiday(year, country='japanese__ja'):
    """国民の祝日をGoogleカレンダーから取得する
        引数で指定された年の祝日を，(日付,名前) のタプルのイテレータで返す
    """
    calendar_id = country + "@holiday.calendar.google.com"
    url = "https://www.googleapis.com/calendar/v3/calendars/{0}/events".format(calendar_id)
    params = {
              "key" : environ["GOOGLE_CALENDAR_API_KEY"],
              "timeMin":"%d-01-01T00:00:00Z" % year,
              "timeMax":"%d-12-31T00:00:00Z" % year,
              "maxResults":100,
              "orderBy": "startTime",
              "singleEvents": "true",
              }
    url += "?" + urllib.parse.urlencode(params)
    response = json_parse(url)
    for item in response["items"]:
        date = datetime.datetime.strptime(item["start"]["date"], "%Y-%m-%d").date()
        title = item["summary"]
        yield (date,title)

