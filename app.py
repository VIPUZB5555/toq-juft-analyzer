from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    juftlar = []
    toqlar = []
    son = None
    if request.method == 'POST':
        try:
            son = int(request.form.get('son'))
            for i in range(1, son+1):
                if i % 2 == 0:
                    juftlar.append(i)
                else:
                    toqlar.append(i)
        except:
            son = None
    return render_template('index.html', son=son, juftlar=juftlar, toqlar=toqlar)

if __name__ == '__main__':
    app.run(debug=True)
