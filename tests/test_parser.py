import unittest

from chat_parser import ChatParser
from utils import get_test_case


class TestClient(unittest.TestCase):
    maxDiff = None

    def test_step_1(self):
        parser = ChatParser()
        test_case = get_test_case('step_1')
        output = parser.parse(test_case['input'])
        self.assertEqual(test_case['output'], output)
