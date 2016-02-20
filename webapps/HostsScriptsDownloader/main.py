#!/usr/bin/env python3
import requests
from io import BytesIO
from flask import Flask, send_file

app = Flask(__name__)


@app.route('/script_tool_for_linux.sh')
def linux_version():
    link = 'https://raw.githubusercontent.com/racaljk/hosts' +\
        '/master/hosts_tools/scripts/script_tool_for_linux.sh'

    return send_file(BytesIO(requests.get(link).content))


@app.route('/script_tool_for_windows.bat')
def windows_version():
    link = 'https://raw.githubusercontent.com/racaljk/hosts' +\
        '/master/hosts_tools/scripts/script_tool_for_windows.bat'

    return send_file(BytesIO(requests.get(link).content))


if __name__ == '__main__':
    app.run(debug=True)
