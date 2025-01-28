import unittest
from src.encoder import Encoder


class TestEncoder(unittest.TestCase): 
    def setUp(self) -> None:
        self.e: Encoder = Encoder()


    def test_encode(self) -> None:
        self.assertEqual(self.e.encode('hi'), "*&@#*&-")
        self.assertEqual(self.e.encode('hello'), '*&@#*&*#*&:#*&:#***')
        self.assertEqual(self.e.encode('tyler was gone'), '**}#*=*#*&:#*&*#**@#$=#**<#<{#**-#$=#*&$#***#**&#*&*')
        self.assertEqual(self.e.encode('WELCOME BACK'), ":{#}<#{}#}{#{<#{{#}<#$=#}}#}-#}{#{-")
        self.assertEqual(self.e.encode("", ""))


    def test_encode_to_ascii(self) -> None:
        self.assertEqual(self.e.encode_to_ascii('hello'), [104, 101, 108, 108, 111])
        self.assertEqual(self.e.encode_to_ascii('hi'), [104, 105])
        self.assertEqual(self.e.encode_to_ascii('tyler was gone'), [116, 121, 108, 101, 114, 32, 119, 97, 115, 32, 103, 111, 110, 101])
        self.assertEqual(self.e.encode_to_ascii("YES"), [89, 69, 83])
        self.assertEqual(self.e.encode_to_ascii("19 YEARS OLD"), [49, 57, 32, 89, 69, 65, 82, 83, 32, 79, 76, 68])
        self.assertEqual(self.e.encode_to_ascii(""), [])


if __name__ == '__main__':
    unittest.main()