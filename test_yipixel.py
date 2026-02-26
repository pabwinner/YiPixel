# test_yipixel.py
"""
Tests for YiPixel module.
"""

import unittest
from yipixel import YiPixel

class TestYiPixel(unittest.TestCase):
    """Test cases for YiPixel class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = YiPixel()
        self.assertIsInstance(instance, YiPixel)
        
    def test_run_method(self):
        """Test the run method."""
        instance = YiPixel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
