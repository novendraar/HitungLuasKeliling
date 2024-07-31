import classDefine as cd

lanjut = True
while lanjut:
    rumus = input("Masukkan bangunan (Persegi / Persegi Panjang / Segitiga Sama Sisi / Lingkaran), jenis hitungan (Luas / Keliling)=\n ").lower()
    if "persegi panjang" in rumus:
        panjang = int(input("Masukkan Panjang= "))
        lebar = int(input("Masukkan Lebar= "))
        persegipjg = cd.PersegiPanjang(panjang, lebar)
        if "luas" in rumus:
            print(9 * "-")
            print(f"Luas = {persegipjg.hitungLuas()}")
        elif "keliling" in rumus:
            print(9 * "-")
            print(f"Keliling = \n{persegipjg.hitungKeliling()}")    
    elif "persegi" in rumus:
        sisi = int(input("Masukkan sisi= "))
        persegi = cd.Persegi(sisi)
        if "luas" in rumus:
            print(9 * "-")
            print(f"Luas = {persegi.hitungLuas()}")
        elif "keliling" in rumus:
            print(9 * "-")
            print(f"Keliling = {persegi.hitungKeliling()}")    
    elif "segitiga" in rumus:
        if "luas" in rumus:
            alas = int(input("Masukkan alas= "))
            tinggi = int(input("Masukkan tinggi= "))
            segitiga = cd.SegitigaSamaSisi(alas=alas, tinggi=tinggi, sisi=0)
            print(9 * "-")
            print(f"Luas = {segitiga.hitungLuas()}")
        elif "keliling" in rumus:
            sisi = int(input("Masukkan panjang sisi= "))
            segitiga = cd.SegitigaSamaSisi(sisi=sisi, alas=0, tinggi=0)
            print(9 * "-")
            print(f"Keliling = {segitiga.hitungKeliling()}")
    elif "lingkaran" in rumus:
        jari2 = int(input("Masukkan panjang jari - jari= "))
        lingkar = cd.Lingkaran(jari2)
        if "luas" in rumus:
            print(9 * "-")
            print(f"Luas = {lingkar.hitungLuas()}")
        elif "keliling" in rumus:
            print(9 * "-")
            print(f"Keliling = {lingkar.hitungKeliling()}")
    else:
        print("Perintah Tidak ditemukan")
    
    print(10 * "_")
    stop = input("Lanjut Menghitung? Y/N\n").upper()
    if "N" in stop:
        lanjut = False   