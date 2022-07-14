import unittest
from  translator import english_to_french , french_to_english

class TestE2F(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("Street") , "Rue")
        self.assertEqual(english_to_french(" ") , " ")
        self.assertNotEqual(english_to_french("Hello") ," ")

class test_F2E(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Rue") , "Street")
        self.assertEqual(french_to_english(" ") , " ")
        self.assertNotEqual(french_to_english("Bonjour") ," ")

unittest.main()
