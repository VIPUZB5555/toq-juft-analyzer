from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    natija = None
    if request.method == 'POST':
        try:
            son = int(request.form['son'])
            juft_sonlar = [i for i in range(1, son + 1) if i % 2 == 0]
            toq_sonlar = [i for i in range(1, son + 1) if i % 2 != 0]
            info = {
                'kiritilgan': son,
                'toq_sonlar': toq_sonlar,
                'juft_sonlar': juft_sonlar,
                'toq_soni': len(toq_sonlar),
                'juft_soni': len(juft_sonlar),
                'eng_katta_juft': juft_sonlar[-1] if juft_sonlar else None,
                'eng_katta_toq': toq_sonlar[-1] if toq_sonlar else None,
            }
            natija = info
        except:
            natija = {'xato': 'Faqat butun son kiriting!'}
    return render_template("index.html", natija=natija)

if __name__ == '__main__':
    app.run(debug=True)
