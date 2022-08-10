import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french('0').get('translations')[0].get('translation'), 0)
        self.assertEqual(english_to_french('Hello').get('translations')[0].get('translation'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english(0).get('translations')[0].get('translation'), 0)
        self.assertEqual(french_to_english('Bonjour').get('translations')[0].get('translation'), 'Hello')
unittest.main()
