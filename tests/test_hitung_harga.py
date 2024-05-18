import unittest
import sys

# Adjust path according the file location
sys.path.append(
    "D:\Coding and Development\Abdiel Project\Belajar Python\laundry_unit_testing\src"
)

from laundryCode.hitungHarga import calcPayment


class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.hb1 = calcPayment(1, 2, 5)
        self.hb2 = calcPayment(2, 5, 3)
        self.hb3 = calcPayment(3, 5, 1)
        self.hb4 = calcPayment(4, 4, 1)

    def test_harga_CKL(self):
        self.assertEqual(self.hb1.countTotal(), 21000.0, "Perhitungan Salah")

    def test_harga_CKS(self):
        self.assertEqual(self.hb2.countTotal(), 50000.0, "Perhitungan Salah")

    def test_harga_LK(self):
        self.assertEqual(self.hb3.countTotal(), 75000.0, "Perhitungan Salah")

    def test_harga_EXP(self):
        self.assertEqual(self.hb4.countTotal(), 100000.0, "Perhitungan Salah")


if __name__ == "__main__":
    unittest.main(buffer=True)  # Ignore text from class
