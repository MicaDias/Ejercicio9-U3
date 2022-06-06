import unittest
from Palindromo import Palindromo
class TestPalindromo(unittest.TestCase):
    __palindromo=None
    def setUp(self):
        self.__palindromo=Palindromo('anana')
    def test_palindromo(self):
        self.assertEqual(self.__palindromo.esPalindromo(),True)
    def test_palindromo_2(self):
        self.__palindromo.setPalabra('ana')
        self.assertEqual(self.__palindromo.esPalindromo(),True)
    def test_palindromo_3(self):
        self.__palindromo.setPalabra('ANA')
        self.assertEqual(self.__palindromo.esPalindromo(),True)
    def test_palindromo_par(self):
        self.__palindromo.setPalabra('otto')
        self.assertEqual(self.__palindromo.esPalindromo(),True)
    def test_no_palindromo(self):
        self.__palindromo.setPalabra('test')
        self.assertEqual(self.__palindromo.esPalindromo(),False)
    def test_no_palindromo_2(self):
        self.__palindromo.setPalabra('gol')
        self.assertEqual(self.__palindromo.esPalindromo(),False)