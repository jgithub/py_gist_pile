import unittest
from datetime import datetime
from date_util import get_milliseconds_since_date
from time import sleep

class TestDateUtil(unittest.TestCase):
    def test_get_milliseconds_since_date(self):
        before_at: datetime = datetime.now()
        sleep(0.01)
        self.assertTrue(get_milliseconds_since_date(before_at) > 0)
        self.assertTrue(get_milliseconds_since_date(before_at) < 100)

if __name__ == "__main__":
    unittest.main()
