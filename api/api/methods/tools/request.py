"""
The request method of the tool object of the API

https://ru.wikipedia.org/wiki/HTTP
"""

import re
import json
import requests

from api.lib import BaseType, validate
from api.methods.tools.curl import convert_py


class Type(BaseType):
    method: str = 'GET'
    url: str = None
    params: list = []
    data: str = None
    headers: list = []

@validate(Type)
async def handle(_, data):
    """ Request """

    method, url, params, body, headers = convert_py(
        data.method, data.url, data.params, data.data, data.headers
    )

    base_url = re.search(r'http.*://[^/]*/', data.url)
    if base_url:
        base_url = base_url[0]

    handler = getattr(requests, method)
    res = handler(url, headers=headers, params=params, data=body).text

    # Response
    return {
        'response': res,
        'url': base_url,
    }
