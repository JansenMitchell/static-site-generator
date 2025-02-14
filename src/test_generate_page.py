import unittest

from generate_page import *

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")