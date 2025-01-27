import unittest
from src.encoder import Encoder


class TestEncoder(unittest.TestCase): 
    def test_encode(self) -> None:
        e: Encoder = Encoder()

        self.assertEqual(e.encode('hi'), "*&@#*&-")
        self.assertEqual(e.encode('hello'), '*&@#*&*#*&:#*&:#***')
        self.assertEqual(e.encode('tyler was gone'), '**}#*=*#*&:#*&*#**@#$=#**<#<{#**-#$=#*&$#***#**&#*&*')
        self.assertEqual(e.encode('WELCOME BACK'), ":{#}<#{}#}{#{<#{{#}<#$=#}}#}-#}{#{-")
        self.assertEqual(e.encode("", ""))



if __name__ == '__main__':
    unittest.main()