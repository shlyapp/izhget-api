from unittest import TestCase, main

from src.tram import get_trams


class TramTest(TestCase):
    def test_counter(self):
        self.assertEqual(len(get_trams()), 17)

    def test_name(self):
        tram = get_trams()[0]
        self.assertEqual(tram.name, "Для всех")

    def test_id(self):
        tram = get_trams()[0]
        self.assertEqual(tram.id, 0)


if __name__ == "__main__":
    main()
