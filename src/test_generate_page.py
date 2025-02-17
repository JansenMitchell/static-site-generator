import unittest

from generate_page import *

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")
        
        # Test basic title
        assert extract_title("# Hello") == "Hello"
        
        # Test with extra spaces
        assert extract_title("# Title with spaces   ") == "Title with spaces"
        
        try:
            extract_title("Not a title\nStill not a title")
            assert False, "Should have raised an exception"
        except Exception:
            assert True
            
        text = """
        Some text
        # The Title
        More text
        """
        assert extract_title(text) == "The Title"