from area import triangle
from area import rectangle
from area import circle
from area import square

from characterLocator import location

from dictionary import dic

from mario import stars

from multiplicationTable import multiplication

from vowels import vowels

import unittest

class TestCases(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle(3,2),3.0)
        self.assertEqual(rectangle(2,3),6.0)
        self.assertEqual(circle(5),78.53981633974483)
        self.assertEqual(square(4),16)

    def test_character_location(self):
        self.assertEqual(location("kairo is a clever girl","i"),[2,6,19])

    def dictionary(self):
        self.assertEqual(dic(['kairo','wageh','koko']),{'w': ['wageh'], 'k': ['kairo', 'koko']})

    def test_mario(self):
        self.assertEqual(stars(4),"""*
                                  **
                                 ***
                                ****""")

        #self.assertequal(stars(4),"*\
        #                          **\
        #                         ***\
        #                        ****")


    def test_multiplication_table(self):
        self.assertEqual(multiplication(2),[[1], [2, 4]])

    def test_vowels(self):
        self.assertEqual(vowels("mobile"),"mbl")
        self.assertEqual(vowels("MoBIle"),"MBl")
if __name__ == "__main__":
    unittest.main()
