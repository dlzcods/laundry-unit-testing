import unittest
import sys

# Sesuaikan path dengan versimu
sys.path.append(
    "D:\Coding and Development\Abdiel Project\Belajar Python\laundry_unit_testing\src"
)

from laundryCode.hitungHarga import hargaBayar


class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.hb1 = hargaBayar(1, 2, 5)
        self.hb2 = hargaBayar(2, 3, 4)
        self.hb3 = hargaBayar(3, 1, 7)

    def test_harga_CKL(self):
        self.assertEqual(self.hb1.hitungTotal(), 42500.0, "Perhitungan Salah")

    def test_harga_CKS(self):
        self.assertEqual(self.hb2.hitungTotal(), 40000.0, "Perhitungan Salah")

    def test_harga_LK(self):
        self.assertEqual(self.hb3.hitungTotal(), 105000.0, "Perhitungan Salah")


if __name__ == "__main__":
    unittest.main(buffer=True)  # Mengabaikan teks dari class
