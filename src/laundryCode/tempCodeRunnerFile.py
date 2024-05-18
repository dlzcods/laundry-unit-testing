"""
descerangan
mko = Minimum Kilo
prk = Harga Per Kilo
dy = Hari
tpy =  Total Bayar
pkg = Padesc

Pilihan padesc:
1. Folded Dry Cleaning
2. Iron Dry Cleaning
3. Lengkap Kilat
4. Express
"""


class calcPayment:
    def __init__(self, pkg, dy, ko):
        self.pkg = pkg
        self.dy = dy
        self.ko = ko
        self.desc = None

    def countTotal(self):
        mko = 3.00
        prk = 0.00
        tpy = 0.00

        ## Perhitungan padesc (1) Folded Dry Cleaning
        if self.pkg == 1:
            self.desc = "Folded Dry Cleaning"
            prk = 7000.00

            if self.dy < 3:
                if self.dy > 1:
                    prk = 8500.00
                    if self.ko < mko:
                        self.ko = mko
                elif self.dy < 2:
                    raise ValueError("Pengerjaan paling cepat 2 hari")
            else:
                if self.ko <= 3:
                    self.ko = mko
            
            tpy = prk * self.ko

        ## Perhitungan pdesc (2) Iron Dry Cleaning
        elif self.pkg == 2:
            self.desc = "Iron Dry Cleaning"
            prk = 10000.00

            if self.dy < 3:
                if self.dy > 1:
                    prk = 12000.00
                    if self.ko < mko:
                        self.ko = mko
                elif self.dy < 2:
                    raise ValueError("Pengerjaan paling cepat 2 hari")
            else:
                if self.ko <= 3:
                    self.ko = mko
            
            tpy = prk * self.ko

        ## Perhitungan padesc (3) LENGKAP KILAT 1 HARI
        elif self.pkg == 3:
            self.desc = "Iron Dry Cleaning KILAT 1 HARI"
            self.dy = 1
            prk = 15000.00

            if self.ko < mko:
                self.ko = mko
            
            tpy = prk * self.ko
            
        ## Perhitungan padesc (4) EXPRESS 5 Jam
        elif self.pkg == 4:
            self.desc = "Iron Dry Cleaning EXPRESS 5 Jam"
            prk = 25000.00
            self.dy = 1

            tpy = prk * self.ko

        print(f"Layanan: {self.desc}")
        print(f"Kuantitas: {self.ko} Kilogram")
        print(f"Waktu pengerjaan: {self.dy} Hari")
        print("Total Bayar:")
        return tpy
