import unittest

# sys.path.append(path)
# from ../../py_gist_pile2/date/date_provider_service import DateProviderService
from datetime import datetime

from py_gist_pile.date.date_provider_service_impl import DateProviderServiceImpl


class TestDateProvider(unittest.TestCase):
    def test_does_this_work(self):
        date_provider_service = DateProviderServiceImpl()
        self.assertEqual(date_provider_service.get_now(), datetime.now())


if __name__ == "__main__":
    unittest.main()
