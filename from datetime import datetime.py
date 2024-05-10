from datetime import datetime
from abc import ABC, abstractmethod

class Szoba (ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam
    
    @abstractmethod
    
    def szolgaltatasok(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, kilatas):
        super().__init__(ar, szobaszam)
        self.kilatas = kilatas
    
    def szolgaltatasok(self):
        return f"Wifi, TV, zuhanyzó, kilátás: {self.kilatas}"

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, erkely):
        super().__init__(ar, szobaszam)
        self.erkely = erkely
    
    def szolgaltatasok(self):
        return f"Wifi, TV, zuhanyzó, erkély: {self.erkely}"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = {'szobaszam': szobaszam, 'datum': datum, 'ar': szoba.ar}
                self.foglalasok.append(foglalas)
                return f"A(z) {szobaszam} szoba foglalva a(z) {datum} dátumra. Ár: {szoba.ar}"
        return "Nem található ilyen szoba."

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas['szobaszam'] == szobaszam and foglalas['datum'] == datum:
                self.foglalasok.remove(foglalas)
                return f"A(z) {szobaszam} szoba foglalása törölve a(z) {datum} dátumra."
        return "Nem található ilyen foglalás."

    def osszes_foglalas(self):
        return self.foglalasok

def main():
    szalloda = Szalloda("Példa Szálloda")

    szoba1 = EgyagyasSzoba(ar=50, szobaszam="101", kilatas="hegyekre")
    szoba2 = EgyagyasSzoba(ar=60, szobaszam="102", kilatas="tengerre")
    szoba3 = KetagyasSzoba(ar=100, szobaszam="201", erkely=True)

    szalloda.uj_szoba(szoba1)
    szalloda.uj_szoba(szoba2)
    szalloda.uj_szoba(szoba3)

    szalloda.foglalas(szobaszam="101", datum=datetime(2024, 5, 11))
    szalloda.foglalas(szobaszam="201", datum=datetime(2024, 5, 12))
    szalloda.foglalas(szobaszam="102", datum=datetime(2024, 5, 13))
    szalloda.foglalas(szobaszam="101", datum=datetime(2024, 5, 14))
    szalloda.foglalas(szobaszam="201", datum=datetime(2024, 5, 15))

    print("Üdvözöljük a", szalloda.nev, "szállodában!")
    while True:
        print("\nVálasszon egy műveletet:")
        print("1. Szoba foglalás")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("0. Kilépés")

        valasztas = input("Adja meg a kívánt művelet számát: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
            datum = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.strptime(datum, "%Y-%m-%d")
                print(szalloda.foglalas(szobaszam, datum))
            except ValueError:
                print("Hibás dátum formátum!")

        elif valasztas == "2":
            szobaszam = input("Adja meg a lemondani kívánt foglalás szoba számát: ")
            datum = input("Adja meg a lemondani kívánt foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.strptime(datum, "%Y-%m-%d")
                print(szalloda.lemondas(szobaszam, datum))
            except ValueError:
                print("Hibás dátum formátum!")

        elif valasztas == "3":
            foglalasok = szalloda.osszes_foglalas()
            print("Összes foglalás:")
            for foglalas in foglalasok:
                print(f"Foglalás a(z) {foglalas['szobaszam']} szobára a(z) {foglalas['datum']} dátumra. Ár: {foglalas['ar']}")

        elif valasztas == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()