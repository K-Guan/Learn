#!/usr/bin/env python3
from flask import Flask
from HostsScriptsDownloader.hosts_scripts import hosts_scripts

app = Flask(__name__)

app.register_blueprint(hosts_scripts, url_prefix="/hosts_scripts")


if __name__ == '__main__':
    app.run(debug=True)
