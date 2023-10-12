from unittest import TestCase, main

from src.station import get_stations, get_destinations


class StationTest(TestCase):
    def test_counter(self):
        self.assertEqual(len(get_stations(0)), 65)


class DestinationTest(TestCase):
    def test_counter(self):
        self.assertEqual(len(get_destinations(0, 0)), 65)


if __name__ == "__main__":
    main()


