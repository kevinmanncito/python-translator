import requests
import json
import os
from xml.etree import ElementTree

client_id = os.environ.get('TRANSLATE_CLIENT_ID', '')

client_secret = os.environ.get('TRANSLATE_CLIENT_SECRET', '')

translator_access_uri = "https://datamarket.accesscontrol.windows.net/v2/OAuth2-13"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'http://api.microsofttranslator.com',
    'grant_type': 'client_credentials'
}

response = requests.post(translator_access_uri, data, headers=headers)


headers = {
    'Authorization' : "Bearer {0}".format(response.json().get('access_token', ''))
}

translate_text = raw_input("What do you want to translate to spanish?")

translate_uri = """http://api.microsofttranslator.com/v2/Http.svc/Translate?text={0}&from=en&to=es""".format(translate_text)

response = requests.get(translate_uri, headers=headers)


tree = ElementTree.fromstring(response.content)
print tree.text

