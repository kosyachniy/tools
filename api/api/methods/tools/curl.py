"""
The cURL request creating method of the tool object of the API
"""

import json

from api.lib import BaseType, validate


class Type(BaseType):
    method: str = 'GET'
    url: str = None
    data: str = ''
    headers: list = []

@validate(Type)
async def handle(_, data):
    """ cURL converter """

    curl_headers = ''.join(
        f" -H '{header}: {header_data}'"
        for header, header_data in data.headers
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

    curl = f"curl -v -X {data.method}{curl_headers}{curl_data} {data.url}"

    # Response
    return {
        'curl': curl,
        'py': "",
        'js': "",
    }
