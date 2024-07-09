import unittest
from scraper.retry_utils import retry_on_exception

class TestRetryUtils(unittest.TestCase):

    def test_retry_on_exception(self):
        @retry_on_exception
        def might_fail():
            if not hasattr(might_fail, "counter"):
                might_fail.counter = 0
            might_fail.counter += 1
            if might_fail.counter < 3:
                raise Exception("Fail")
            return "Success"

        result = might_fail()
        self.assertEqual(result, "Success")

if __name__ == '__main__':
    unittest.main()
