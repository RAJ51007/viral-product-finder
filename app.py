from flask import Flask, render_template, request
import logic

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    products = []
    if request.method == 'POST':
        keyword = request.form['keyword']
        products = logic.run_bot(keyword)
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
