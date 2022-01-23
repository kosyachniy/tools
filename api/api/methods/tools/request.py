"""
The request method of the tool object of the API

https://ru.wikipedia.org/wiki/HTTP
"""

import re
import requests

from api.lib import BaseType, validate, report
from api.methods.tools.curl import convert_py


class Type(BaseType):
    method: str = 'GET'
    url: str = None
    params: list = []
    data: str = None
    headers: list = []

@validate(Type)
async def handle(request, data):
    """ Request """

    await report.important("Request", {
        'method': data.method,
        'url': data.url,
        'params': data.params,
        'data': data.data,
        'headers': data.headers,
        'user': request.user.id or request.token,
    })

    base_url = re.search(r'http.*://[^/]*/', data.url)
    if base_url:
        base_url = base_url[0]

    if not data.url:
        return {
            'response': "",
            'url': base_url,
        }

    method, url, params, body, headers = convert_py(
        data.method, data.url, data.params, data.data, data.headers
    )

    handler = getattr(requests, method)
    res = handler(url, headers=headers, params=params, data=body).text

    # Response
    return {
        'response': res,
        'url': base_url,
    }
