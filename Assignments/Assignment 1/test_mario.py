from mario import stars
import unittest
class TestMario(unittest.TestCase):
    def star(self):
        self.assertequal(stars(4),"""*
                                  **
                                 ***
                                ****""")

        #self.assertequal(stars(4),"*\
        #                          **\
        #                         ***\
        #                        ****")

if __name__ == "__main__":
    unittest.main()
