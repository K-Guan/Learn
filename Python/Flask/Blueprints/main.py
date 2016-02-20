#!/usr/bin/env python3
from flask import Flask
from tree_workshop import tree_mold

app = Flask(__name__)

app.register_blueprint(tree_mold, url_prefix="/oak")
app.register_blueprint(tree_mold, url_prefix="/fir")
app.register_blueprint(tree_mold, url_prefix="/ash")


if __name__ == '__main__':
    app.run(debug=True)
