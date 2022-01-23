"""
The cURL request creating method of the tool object of the API
"""

import json

from api.lib import BaseType, validate


class Type(BaseType):
    method: str = 'GET'
    url: str = None
    params: list = []
    data: str = ''
    headers: list = []

@validate(Type)
async def handle(_, data):
    """ cURL converter """

    curl_params = '&'.join(
        f"{param}={param_data}"
        for param, param_data in data.params
        if param
    )
    if curl_params:
        curl_params = "?" + curl_params

    curl_headers = ''.join(
        f" -H '{header}: {header_data}'"
        for header, header_data in data.headers
        if header
    )

    if data.data:
        try:
            curl_data = json.loads(data.data)
        except TypeError:
            curl_data = ""
        else:
            curl_data = f" -d '{json.dumps(curl_data, ensure_ascii=False)}'"
    else:
        curl_data = ""

    curl = (
        f"curl -v -X {data.method}"
        f"{curl_headers}{curl_data}"
        f" {data.url}{curl_params}"
    )

    # Response
    return {
        'curl': curl,
        'py': "",
        'js': "",
    }
