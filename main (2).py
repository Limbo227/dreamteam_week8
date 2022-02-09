from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    def generate_insult(lang):
        import requests
        evil = requests.get(url='https://evilinsult.com/generate_insult.php?lang=' + lang + '&type=json')
        data = evil.json()
        insult = data['insult']
        return insult

    name = generate_insult('ru')
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)