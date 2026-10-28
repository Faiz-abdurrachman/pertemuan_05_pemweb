from flask import Flask, render_template

app = Flask(__name__)

# Data artikel mini sederhana (Hasil pembelajaran P-04)
artikel_list = [
    {
        "id": 1,
        "judul": "Belajar Flask Pemula",
        "ringkasan": "Panduan membuat web sederhana dengan Python.",
        "konten": "Flask adalah micro-framework Python yang sangat ringan, fleksibel, dan mudah dipelajari untuk pemula."
    },
    {
        "id": 2,
        "judul": "Mengenal CSS Modern",
        "ringkasan": "Cara bikin tampilan web rapi dan responsif.",
        "konten": "CSS modern memungkinkan penataan kartu dan formulir tanpa perlu library rumit atau JavaScript tambahan."
    },
    {
        "id": 3,
        "judul": "Tips Praktikum Web 2026",
        "ringkasan": "Kiat sukses memahami backend dan frontend.",
        "konten": "Kunci utama belajar web adalah memahami bagaimana browser mengirim permintaan HTTP dan server mengembalikan respon HTML."
    }
]

@app.route("/")
def home():
    return render_template("index.html", artikel_list=artikel_list)

if __name__ == "__main__":
    app.run(debug=True)
