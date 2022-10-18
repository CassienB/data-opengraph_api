# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    params = {'url':url}
    response = requests.get("https://opengraph.lewagon.com",params=params, timeout=10)
    if response.status_code < 300:
        return response.json()['data']
    return None
# To manually test, please uncomment the following lines and run `python opengraph.py`:
#import pprint
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(fetch_metadata("https://www.github.com"))
