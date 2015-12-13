from flask import Flask, request,jsonify
from goose import Goose
from summary import Summary # from filename import Classname


app = Flask(__name__)

@app.route('/api/v1/extract')
def extract():
    url = request.args.get('url')
    g = Goose()
    article = g.extract(url=url)
    print article
    # response = {'title' : article.title , 'text' : article.cleaned_text}
    # return jsonify(response)
    summarised_article = Summary({'title' : article.title , 'content' : article.cleaned_text})
    summarised_article.print_result()
    return jsonify(summarised_article.get_result())

if __name__ == "__main__":
    app.run(debug=True)
