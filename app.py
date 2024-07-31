from flask import Flask, render_template, request
import classDefine as cd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    shape = request.form['shape'].lower()
    calculation = request.form['calculation'].lower()
    result = ""

    if shape == 'persegi':
        sisi = float(request.form['sisi'])
        persegi = cd.Persegi(sisi)
        if calculation == 'luas':
            result = persegi.hitungLuas()
        elif calculation == 'keliling':
            result = persegi.hitungKeliling()
    elif shape == 'persegi panjang':
        panjang = float(request.form['panjang'])
        lebar = float(request.form['lebar'])
        persegipjg = cd.PersegiPanjang(panjang, lebar)
        if calculation == 'luas':
            result = persegipjg.hitungLuas()
        elif calculation == 'keliling':
            result = persegipjg.hitungKeliling()
    elif shape == 'segitiga':
        sisi = float(request.form.get('sisi', 0))
        alas = float(request.form.get('alas', 0))
        tinggi = float(request.form.get('tinggi', 0))
        segitiga = cd.SegitigaSamaSisi(sisi, alas, tinggi)
        if calculation == 'luas':
            result = segitiga.hitungLuas()
        elif calculation == 'keliling':
            result = segitiga.hitungKeliling()
    elif shape == 'lingkaran':
        jari2 = float(request.form['jari2'])
        lingkar = cd.Lingkaran(jari2)
        if calculation == 'luas':
            result = lingkar.hitungLuas()
        elif calculation == 'keliling':
            result = lingkar.hitungKeliling()

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
