import unittest
import sys
import os
from dotenv import load_dotenv

# Load test environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env.test'))

# Ensure the src directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

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
