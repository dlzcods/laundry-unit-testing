"""
Description
mko = Minimum Kilogram
prk = Price Per Kilogram
dy = Day
tpy = Total Pay
pkg = Package
desc = Package Name

Package options:
1. Folded Dry Cleaning
2. Iron Dry Cleaning
3. Complete Express
4. Speedy Express
"""


class calcPayment:
    def __init__(self, pkg, ko, dy):
        self.pkg = pkg
        self.ko = ko
        self.dy = dy
        self.desc = None

    def countTotal(self):
        mko = 3.00
        prk = 0.00
        tpy = 0.00

        ## Package calculations (1) Folded Dry Cleaning
        if self.pkg == 1:
            self.desc = "Folded Dry Cleaning"
            prk = 7000.00

            if self.dy < 3:
                if self.dy > 1:
                    prk = 8500.00
                    if self.ko < mko:
                        self.ko = mko
                elif self.dy < 2:
                    raise ValueError("Folded Dry Cleaning at the earliest 2 days")
            else:
                if self.ko <= 3:
                    self.ko = mko

            tpy = prk * self.ko

        ## Package calculations (2) Iron Dry Cleaning
        elif self.pkg == 2:
            self.desc = "Iron Dry Cleaning"
            prk = 10000.00

            if self.dy < 3:
                if self.dy > 1:
                    prk = 12000.00
                    if self.ko < mko:
                        self.ko = mko
                elif self.dy < 2:
                    raise ValueError("Iron Dry Cleaning at the earliest 2 days")
            else:
                if self.ko <= 3:
                    self.ko = mko

            tpy = prk * self.ko

        ## Package calculations (3) Complete Express in 1 day
        elif self.pkg == 3:
            self.desc = "Complete Express"
            self.dy = 1
            prk = 15000.00

            if self.ko < mko:
                self.ko = mko

            tpy = prk * self.ko

        ## Package calculations (4) Speedy Express in 5 hours
        elif self.pkg == 4:
            self.desc = "Speedy Express"
            prk = 25000.00
            self.dy = 0.2083

            tpy = prk * self.ko

        print("Note:")
        print("1. Orders under 3 kilograms will be counted as a minimum order (3kg).")
        print(
            "2. Only Complete Express and Speedy Express packages are available for orders under or equal to 1 day."
        )
        print("\nHere is Your Payment")
        print(f"Package: {self.desc}")
        print(f"Quantity: {self.ko} Kilogram")
        print(f"Processing time: {self.dy} Day")
        print(f"Total Payment: Rp{tpy}")
        print("\nThank You for Ordering")
        return (
            tpy  # You can change this to a blank string when you not doing unit testing
        )


# Test the calculation
order = calcPayment(4, 4, 1)  # calcPayment(package, quantity, processing time(day))
print(order.countTotal())
