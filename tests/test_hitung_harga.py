import unittest
import sys

# Adjust path according the file location
sys.path.append(
    "D:\Coding and Development\Abdiel Project\Belajar Python\laundry_unit_testing\src"
)

from laundryCode.hitungHarga import calcPayment


class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.tp1 = calcPayment(1, 2, 5)
        self.tp2 = calcPayment(2, 5, 3)
        self.tp3 = calcPayment(3, 5, 1)
        self.tp4 = calcPayment(4, 4, 1)

    def test_harga_FDC(self):
        self.assertEqual(self.tp1.countTotal(), 21000.0, "Incorrect calculation")

    def test_harga_IDC(self):
        self.assertEqual(self.tp2.countTotal(), 50000.0, "Incorrect calculation")

    def test_harga_CEP(self):
        self.assertEqual(self.tp3.countTotal(), 75000.0, "Incorrect calculation")

    def test_harga_SEP(self):
        self.assertEqual(self.tp4.countTotal(), 100000.0, "Incorrect calculation")


if __name__ == "__main__":
    unittest.main(buffer=True)  # Ignore text from class
