"""
Keterangan
mko = Minimum Kilo
hpk = Harga Per Kilo
hr = Hari
tb =  Total Bayar
pkt = Paket

Pilihan paket:
1. Cuci Kering Lipat
2. Cuci Kering Setrika
3. Lengkap Kilat
4. Express
"""


class hargaBayar:
    def __init__(self, pkt, hr, ko):
        self.pkt = pkt
        self.hr = hr
        self.ko = ko
        self.ket = None

    def hitungTotal(self):
        mko = 3.00
        hpk = 0.00
        tb = 0.00

        ## Perhitungan paket (1) Cuci Kering Lipat
        if self.pkt == 1:
            self.ket = "Cuci Kering Lipat"
            hpk = 7000.00

            if self.hr < 3:
                if self.hr > 1:
                    hpk = 8500.00
                    if self.ko < mko:
                        self.ko = mko
                elif self.hr < 2:
                    raise ValueError("Pengerjaan paling cepat 2 hari")
            else:
                if self.ko <= 3:
                    self.ko = mko
            
            tb = hpk * self.ko

        ## Perhitungan pket (2) Cuci Kering Setrika
        elif self.pkt == 2:
            self.ket = "Cuci Kering Setrika"
            hpk = 10000.00

            if self.hr < 3:
                if self.hr > 1:
                    hpk = 12000.00
                    if self.ko < mko:
                        self.ko = mko
                elif self.hr < 2:
                    raise ValueError("Pengerjaan paling cepat 2 hari")
            else:
                if self.ko <= 3:
                    self.ko = mko
            
            tb = hpk * self.ko

        ## Perhitungan paket (3) LENGKAP KILAT 1 HARI
        elif self.pkt == 3:
            self.ket = "Cuci Kering Setrika KILAT 1 HARI"
            self.hr = 1
            hpk = 15000.00

            if self.ko < mko:
                self.ko = mko
            
            tb = hpk * self.ko
            
        ## Perhitungan paket (4) EXPRESS 5 Jam
        elif self.pkt == 4:
            self.ket = "Cuci Kering Setrika EXPRESS 5 Jam"
            hpk = 25000.00
            self.hr = 1

            tb = hpk * self.ko

        print(f"Layanan: {self.ket}")
        print(f"Kuantitas: {self.ko} Kilogram")
        print(f"Waktu pengerjaan: {self.hr} Hari")
        print("Total Bayar:")
        return tb
