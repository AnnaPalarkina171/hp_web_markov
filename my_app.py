from flask import Flask
from flask import url_for, render_template
import markovify
import os

app = Flask(__name__)

@app.route('/')
def index():
    urls = {'главная (эта страница)': url_for('index')}
    # Get raw text as string.
    with open('GP.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # Build the model.
        text_model = markovify.Text(text, state_size=3)

    # Print five randomly-generated sentences
    for i in range(1):
        sentence = text_model.make_sentence()

    return render_template('index.html', urls=urls, sentence=sentence)


if __name__ == '__main__':
    import os
    app.debug = False
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
