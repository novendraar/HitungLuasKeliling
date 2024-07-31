document.getElementById('shape').addEventListener('change', function() {
    const shape = this.value;
    const inputs = document.getElementById('inputs');
    const calculation = document.getElementById('calculation').value; // Ambil jenis hitungan yang dipilih

    inputs.innerHTML = '';

    if (shape === 'persegi') {
        inputs.innerHTML = `
            <label for="sisi">Sisi:</label>
            <input type="number" name="sisi" id="sisi" required><br><br>
        `;
    } else if (shape === 'persegi panjang') {
        inputs.innerHTML = `
            <label for="panjang">Panjang:</label>
            <input type="number" name="panjang" id="panjang" required><br><br>
            <label for="lebar">Lebar:</label>
            <input type="number" name="lebar" id="lebar" required><br><br>
        `;
    } else if (shape === 'segitiga') {
        if (calculation === 'luas') {
            inputs.innerHTML = `
                <label for="alas">Alas:</label>
                <input type="number" name="alas" id="alas" required><br><br>
                <label for="tinggi">Tinggi:</label>
                <input type="number" name="tinggi" id="tinggi" required><br><br>
            `;
        } else if (calculation === 'keliling') {
            inputs.innerHTML = `
                <label for="sisi">Sisi:</label>
                <input type="number" name="sisi" id="sisi" required><br><br>
                <input type="hidden" name="alas" id="alas" value="0">
                <input type="hidden" name="tinggi" id="tinggi" value="0">
            `;
        }
    } else if (shape === 'lingkaran') {
        inputs.innerHTML = `
            <label for="jari2">Jari-jari:</label>
            <input type="number" name="jari2" id="jari2" required><br><br>
        `;
    }
});

// Tambahkan event listener untuk mengupdate input ketika jenis hitungan berubah
document.getElementById('calculation').addEventListener('change', function() {
    document.getElementById('shape').dispatchEvent(new Event('change'));
});
