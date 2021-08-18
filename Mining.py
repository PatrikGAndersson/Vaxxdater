import requests

URL="https://www.vgregion.se/ov/vaccinationstider/bokningsbara-tider/"

def get_webpage():
    resp = requests.get(URL)
    #response = parseResponse(resp)
    return resp
