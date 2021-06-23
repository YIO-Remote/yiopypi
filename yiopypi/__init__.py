import logging

import requests
from requests.structures import CaseInsensitiveDict
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError

import json

LOG = logging.getLogger(__name__)
HTTP_URL = "http://{0}:8000/rest/auth/external/homeassistant/"

class YIO(object):
    def __init__(self, host):
        self._host = host

    def sendToken(self, tokenId, name, token):

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Basic eWlvOnJlbW90ZQ=="
        headers["Content-Type"] = "application/json"

        data = {"id" : tokenId, "name" : name, "token" : token}

        url = HTTP_URL.format(self._host)

        try:
            r = requests.post(url, headers=headers, data=json.dumps(data))
            
            response = r.text
            LOG.debug("Response: %s", response)

            if (r.status_code == 200):
                return True
            
            if (r.status_code == 400):
                return False
            
            if (r.status_code == 404):
                return False

        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
            return False