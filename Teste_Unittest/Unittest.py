import unittest

from Main import somar

class TestCalculadora(unittest.TestCase):

 def test_somar(self):
    resultado = somar(2, 3)
    self.assertEqual(resultado, 5)
if __name__ == "__main__":
 unittest.main()