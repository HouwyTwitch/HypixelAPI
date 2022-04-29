from libs.HypixelAPIScrapper import HypixelAPIScrapper
from libs.exceptions import *
from libs.models import *
import json


def checkStatusCode(status_code: int, messages: list = ErrorMessages) -> None:
    if status_code == 400: raise WrongInputParams(messages[0])
    elif status_code == 403: raise WrongAPIKey(messages[1])
    elif status_code == 404: raise WrongInputParams(messages[2])
    elif status_code == 422: raise WrongInputParams(messages[3])
    elif status_code == 429: raise TooMuchRequests(messages[4])
    elif status_code == 503: raise DataIsNotPublic(messages[5])
    elif status_code != 200 raise WrongInputParams(messages[-1])

def simpleGetRequest(url: str, session: requests.Session, headers: dict) -> dict:
    response: requests.Response = session.get(url, headers = headers)
    checkStatusCode(response.status_code)
    return json.loads(response.content)

def oneParamRequest(url: str, param: str, value: str, session: requests.Session, headers: dict) -> dict:
    return simpleGetRequest(f'{url}?{param}={value}', session, headers)

def threeParamsRequest(url, p1: str, p2: str, p3: str, v1: str, v2: str, v3: str, session: requests.Session, headers: dict) -> dict:
    if v1 != None: return oneParamRequest(url, p1, v1, session, headers)
    elif v2 != None: return oneParamRequest(url, p2, v2, session, headers)
    elif v3 != None: return oneParamRequest(url, p3, v3, session, headers)
    else: raise WrongInputParams(ErrorMessages[0])

def authorize(apiKey: str) -> HypixelAPIScrapper:
    return HypixelAPIScrapper(apiKey)

def loadSettings(filename: str = 'settings.json') -> dict:
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    return json.loads(content)
        