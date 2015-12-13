from flask import Flask, request,jsonify
from goose import Goose
from summary import Summary # from filename import Classname
import os


app = Flask(__name__)

@app.route('/api/v1/extract')
def extract():
    url = request.args.get('url')
    g = Goose({'browser_user_agent': 'Mozilla'})
    print 'url', url
    article = g.extract(url=url)
    print 'article title', article.title
    print 'article meta', article.meta_description
    print 'article text', article.cleaned_text
    # response = {'title' : article.title , 'text' : article.cleaned_text}
    # return jsonify(response)
    summarised_article = Summary({'title' : article.title , 'content' : article.cleaned_text})
    summarised_article.print_result()
    return jsonify(summarised_article.get_result())
#
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8080))
#     debug = False if port else True
#     app.run(host='0.0.0.0', port=port, debug=debug)

if __name__ == '__main__':
    from os import environ
    port=int(environ.get("PORT", 8080))
    print 'port', port
    app.run(debug=False, host='0.0.0.0', port=port)
