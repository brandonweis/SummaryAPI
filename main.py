from flask import Flask, request,jsonify
from goose import Goose
from summary import Summary # from filename import Classname
import os
from newspaper import Article


app = Flask(__name__)

@app.route('/api/v1/extract')
def extract():
    url = request.args.get('url')
    # g = Goose({'browser_user_agent': 'Mozilla'})
    # print 'url', url
    # article = g.extract(url=url)
    # summarised_article = Summary({'title' : article.title , 'content' : article.cleaned_text})
    #
    article = Article(url)
    article.download()
    article.parse()
    # print article.title
    # print article.text
    summarised_article = Summary({'title' : article.title , 'content' : article.text})
    # summarised_article.print_result() if article.text else {}
    return jsonify(**summarised_article.get_result())
    # return article.text
#
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8080))
#     debug = False if port else True
#     app.run(host='0.0.0.0', port=port, debug=debug)

if __name__ == '__main__':
    from os import environ
    port=int(environ.get("PORT", 8080))
    print port
    app.run(debug=True, host='0.0.0.0', port=port)
    # port = int(os.environ.get('PORT', 5000)) app.run(host='0.0.0.0', port=port)
