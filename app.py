from flask import Flask, request, render_template
from scipy.stats import poisson

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Ambil input dari form
        lambda_mean = float(request.form['lambda'])
        k = int(request.form['k'])

        # Hitung probabilitas
        prob_exact = poisson.pmf(k, lambda_mean)
        prob_less = poisson.cdf(k - 1, lambda_mean)
        prob_more = 1 - poisson.cdf(k, lambda_mean)

        return render_template(
            'result.html',
            lambda_mean=lambda_mean,
            k=k,
            prob_exact=prob_exact,
            prob_less=prob_less,
            prob_more=prob_more
        )
    except ValueError:
        return "Input tidak valid. Pastikan angka dimasukkan dengan benar.", 400

if __name__ == '__main__':
    app.run(debug=True)
