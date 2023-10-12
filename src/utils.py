from typing import Dict, List
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
import re


tz = pytz.timezone('Europe/Samara')

def get_values_from_tag(text: str, tag_text: str) -> Dict[str, int]:
    """Return a dict value, where the key is the name and the value is the id"""
    soup = BeautifulSoup(text, 'html.parser')
    tags = soup.find_all('option')

    elements = {}
    for tag in tags:
        text = tag.get_text()
        value = int(tag[tag_text])
        elements[text] = value

    return elements


def get_current_date() -> str:
    """Return the date in the format 'day.month.year'"""
    return datetime.now(tz).strftime('%d.%m.%Y')


def get_current_hours() -> str:
    """Return the current hour"""
    return datetime.now(tz).strftime('%H')


def get_current_minutes() -> str:
    """Return current minutes"""
    return datetime.now(tz).strftime('%M')


def get_route_values(text: str) -> List[List[str]]:
    """Parse and return list value: [tram, name, departure time, arrival time]"""
    soup = BeautifulSoup(text, 'html.parser')
    trs = soup.find_all('tr')
    
    values = list()
    for tr in trs:
        tds = tr.find_all('td')
        values.append([re.sub(r'\s+', ' ', td.text.strip()) for td in tds])
    return values[1:]
