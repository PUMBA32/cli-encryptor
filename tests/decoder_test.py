import unittest
from src.decoder import Decoder


class TestDecoder(unittest.TestCase): 
    def setUp(self) -> None:
        self.d: Decoder = Decoder()


    def test_decoder(self) -> None:        
        self.assertEqual(self.d.decode('*&@#*&-'), "hi")
        self.assertEqual(self.d.decode('*&@#*&*#*&:#*&:#***'), 'hello')
        self.assertEqual(self.d.decode('**}#*=*#*&:#*&*#**@#$=#**<#<{#**-#$=#*&$#***#**&#*&*'), 'tyler was gone')
        self.assertEqual(self.d.decode(':{#}<#{}#}{#{<#{{#}<#$=#}}#}-#}{#{-'), "WELCOME BACK")
        self.assertEqual(self.d.decode(""), "")



if __name__ == '__main__':
    unittest.main()