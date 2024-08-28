from flask import Flask,render_template

app = Flask(__name__)

@app.route("/index")
def anasayfa():
    return render_template("index.html")

@app.route("/iletisim")
def iletisim():
    return render_template("iletisim.html")

@app.route("/hakkimizda")
def hakkimizda():
    return render_template("hakkimizda.html")

@app.route("/ayarlar")
def ayarlar():
    return "Ayarlar sayfasına girdiniz."

@app.route("/resimler")
def resimler():
    return "Resimler sayfasına girdiniz."


# Dinamik url yapısı
@app.route('/yazar/<string:id>')
def yazar(id):
    return "Kitap ID si:" + id



if __name__ == "__main__":
    app.run(debug=True)