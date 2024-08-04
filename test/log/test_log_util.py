import unittest
from log_util import d4l_secret, d4l


class TestLogUtil(unittest.TestCase):
    def test_d4l(self):
        self.assertEqual(d4l("super secret password"), "'super secret password' (string, 21)")

    def test_d4l_secret(self):
        self.assertEqual(d4l_secret("super secret password"), "'su...rd' (string, 21)")

if __name__ == "__main__":
    unittest.main()
