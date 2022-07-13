import unittest
from  translator import frenchToEnglish , englishToFrench

class TestF2E(unittest.TestCase):
    def test_F2E(self):
        self.assertEqual(frenchToEnglish("Hello"),"Hello")

class TestE2F(unittest.TestCase):
    def test_E2F(self):
        self.assertEqual(englishToFrench("Bonjour"), "Bonjour")

unittest.main()