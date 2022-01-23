"""
The request method of the tool object of the API
"""

import json
import requests

from api.lib import BaseType, validate


class Type(BaseType):
    method: str = 'GET'
    url: str = None
    data: str = None
    headers: list = []

@validate(Type)
async def handle(_, data):
    """ Request """

    headers = {
        header: header_data
        for header, header_data in data.headers
        if header
    }

    if data.data:
        try:
            body = json.loads(data.data)
        except TypeError:
            body = None
    else:
        body = None

    handler = getattr(requests, data.method.lower())
    res = handler(data.url, headers=headers, json=body).text

    # Response
    return res
