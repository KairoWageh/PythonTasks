from Assign1 import websites
import unittest

class TestCases(unittest.TestCase):
    def Assign1(self):
        self.assertEqual('Google',webbrowser.open_new('https://www.google.com'))
        self.assertEqual('Yahoo',webbrowser.open_new('https://www.yahoo.com'))
        self.assertEqual('Facebook',webbrowser.open_new('https://www.facebook.com'))

if __name__ == "__main__":
    unittest.main()
