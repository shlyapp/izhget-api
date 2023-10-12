from datetime import datetime
from unittest import TestCase, main

from src.utils import get_current_date, get_current_hours, get_current_minutes, tz


class DateConverterTest(TestCase):
    def test_convert_date(self):
        day = datetime.now(tz).day 
        month = datetime.now(tz).month
        year = datetime.now(tz).year
        self.assertEqual(get_current_date(), f'{day}.{month}.{year}')

    def test_convert_hours(self):
        hour = datetime.now(tz).hour
        self.assertEqual(get_current_hours(), f'{hour}')

    def test_convert_minutes(self):
        minutes = datetime.now(tz).minute
        self.assertEqual(get_current_minutes(), f'{minutes}')


if __name__ == "__main__":
    main()
