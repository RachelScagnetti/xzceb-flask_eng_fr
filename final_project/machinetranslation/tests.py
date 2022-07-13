import unittest
from  translator import english_to_french , french_to_english

class TestE2F(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Bonjour"),"Hello")

class test_F2E(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Hello"), "Bonjour")

unittest.main()
