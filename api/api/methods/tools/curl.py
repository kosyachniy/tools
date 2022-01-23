"""
The cURL request creating method of the tool object of the API
"""

import json

from api.lib import BaseType, validate


def convert_curl(method, url, params, data, headers):
    params = '&'.join(
        f"{param}={param_data}"
        for param, param_data in params
        if param
    )
    if params:
        params = "?" + params

    headers = ''.join(
        f" -H '{header}: {header_data}'"
        for header, header_data in headers
        if header
    )

    if data:
        try:
            data = json.loads(data)
        except TypeError:
            data = f" -d '{data}'"
        else:
            data = f" -d '{json.dumps(data, ensure_ascii=False)}'"
    else:
        data = ""

    return method.upper(), url, params, data, headers

def convert_py(method, url, params, data, headers):
    params = {
        param: param_data
        for param, param_data in params
        if param
    }

    headers = {
        header: header_data
        for header, header_data in headers
        if header
    }

    if data:
        try:
            data = json.loads(data)
        except TypeError:
            pass
    else:
        data = None

    return method.lower(), url, params, data, headers


class Type(BaseType):
    method: str = 'GET'
    url: str = None
    params: list = []
    data: str = ''
    headers: list = []

@validate(Type)
async def handle(_, data):
    """ cURL converter """

    method, url, params, body, headers = convert_curl(
        data.method, data.url, data.params, data.data, data.headers
    )
    curl = (
        f"curl -v -X {method}"
        f"{headers}{body}"
        f" {url}{params}"
    )

    method, url, params, body, headers = convert_py(
        data.method, data.url, data.params, data.data, data.headers
    )
    py = (
        f"import requests\n\n"
        f"res = requests.{method}('{url}',\n"
    )
    if headers:
        py += f"    headers={headers},\n"
    if params:
        py += f"    params={params},\n"
    if body:
        py += f"    data='{body}',\n"
    py += ").text\n\nprint(res)\n"

    # Response
    return {
        'curl': curl,
        'py': py,
        'js': "",
    }
