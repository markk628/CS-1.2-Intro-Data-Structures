from flask import Flask, render_template
from histogram import dic_histogram
from sample import read, random_word

app = Flask(__name__)


@app.route('/')
def index():
    source_text = 'test.txt'
    word_list = read(source_text)
    words_list = []
    new_list = ' '
    count = 0
    while count < 11:
        r_word  = random_word(word_list)
        words_list.append(r_word)
        count += 1
    newer_list = new_list.join(words_list)
    return render_template('index.html', newer_list=newer_list)

if __name__ == "__main__":
    app.run(debug=True)