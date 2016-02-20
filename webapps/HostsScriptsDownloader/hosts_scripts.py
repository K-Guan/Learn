#!/usr/bin/env python3
import requests
from io import BytesIO
from flask import Blueprint, send_file

hosts_scripts = Blueprint("hosts_scripts", __name__)


@hosts_scripts.route('/script_tool_for_linux.sh')
def linux_version():
    link = 'https://raw.githubusercontent.com/racaljk/hosts' +\
        '/master/hosts_tools/scripts/script_tool_for_linux.sh'

    return send_file(BytesIO(requests.get(link).content))


@hosts_scripts.route('/script_tool_for_windows.bat')
def windows_version():
    link = 'https://raw.githubusercontent.com/racaljk/hosts' +\
        '/master/hosts_tools/scripts/script_tool_for_windows.bat'

    return send_file(BytesIO(requests.get(link).content))
