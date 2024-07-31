class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    def hitungLuas(self):
        return self.sisi * self.sisi
    def hitungKeliling(self):
        return 4 * self.sisi

class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def hitungLuas(self):
        return self.panjang * self.lebar
    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar)

class SegitigaSamaSisi:
    def __init__(self, sisi, alas, tinggi):
        self.alas = alas
        self.sisi = sisi
        self.tinggi = tinggi
    def hitungLuas(self):
        return 0.5 * (self.alas * self.tinggi)
    def hitungKeliling(self):
        return 3 * self.sisi
    
class Lingkaran:
    def __init__(self, jari2):
        self.r = jari2
        self.phi = 3.14
    def hitungLuas(self):
        return self.phi * self.r ** 2
    def hitungKeliling(self):
        return 2 * self.phi * self.r