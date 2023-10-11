from typing import Dict, List
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
import re


tz = pytz.timezone('Europe/Samara')

def get_values_from_tag(text: str, tag_text: str) -> Dict[str, int]:
    soup = BeautifulSoup(text, 'html.parser')
    tags = soup.find_all('option')

    elements = {}
    for tag in tags:
        text = tag.get_text()
        value = int(tag[tag_text])
        elements[text] = value

    return elements


def get_current_date():
    return datetime.now(tz).strftime('%d.%m.%Y')


def get_current_hours():
    return datetime.now(tz).strftime('%H')


def get_current_minutes():
    return datetime.now(tz).strftime('%M')


def get_route_values(text: str) -> List[List[str]]:
    soup = BeautifulSoup(text, 'html.parser')
    trs = soup.find_all('tr')
    
    values = list()
    for tr in trs:
        tds = tr.find_all('td')
        values.append([re.sub(r'\s+', ' ', td.text.strip()) for td in tds])
    return values[1:]
