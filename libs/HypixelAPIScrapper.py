import requests
from libs.exceptions import WrongAPIKey, WrongInputParams, TooMuchRequests
from libs.models import *
import json


class HypixelAPIScrapper():
    def __init__(self, apiKey: str) -> None:
        self.session: requests.session = requests.session()
        self.owner: str = ''
        if type(apiKey) == str: self.headers = {'API-Key': apiKey}
        else: raise WrongAPIKey("Wrong type of API key. API key should be 'str' type.")
        response: requests.Response = self.session.get(APIKeyInfo, headers = self.headers)
        if response.status_code == 403: raise WrongAPIKey("Access is forbidden, usually due to an invalid API key being used.")
        elif response.status_code == 429: raise TooMuchRequests("A request limit has been reached, usually this is due to the limit on the key being reached but can also be triggered by a global throttle.")
        elif response.status_code != 200 raise WrongAPIKey("Undefined error.")
        self.owner = json.loads(response.content)['record']['owner']
    
    def getOwner(self) -> str:
        return self.owner
    
    def getPlayerData(self, uuid: str) -> dict:
        response: requests.Response = self.session.get(f'{Player}?uuid={uuid}', headers = self.headers)
        if response.status_code == 400: raise WrongInputParams("Some data is missing, this is usually a field.")
        elif response.status_code == 403: raise WrongAPIKey("Access is forbidden, usually due to an invalid API key being used.")
        elif response.status_code == 429: raise TooMuchRequests("A request limit has been reached, usually this is due to the limit on the key being reached but can also be triggered by a global throttle.")
        elif response.status_code != 200 raise WrongInputParams("Undefined error.")
        return json.loads(response.content)
    
    def getFriends(self, uuid: str) -> dict:
        response: requests.Response = self.session.get(f'{Friends}?uuid={uuid}', headers = self.headers)
        if response.status_code == 400: raise WrongInputParams("Some data is missing, this is usually a field.")
        elif response.status_code == 403: raise WrongAPIKey("Access is forbidden, usually due to an invalid API key being used.")
        elif response.status_code == 422: raise WrongInputParams("Some data provided is invalid.")
        elif response.status_code == 429: raise TooMuchRequests("A request limit has been reached, usually this is due to the limit on the key being reached but can also be triggered by a global throttle.")
        elif response.status_code != 200 raise WrongInputParams("Undefined error.")
        return json.loads(response.content)
        
    def getRecentGames(self, uuid: str) -> dict:
        response: requests.Response = self.session.get(f'{RecentGames}?uuid={uuid}', headers = self.headers)
        if response.status_code == 400: raise WrongInputParams("Some data is missing, this is usually a field.")
        elif response.status_code == 403: raise WrongAPIKey("Access is forbidden, usually due to an invalid API key being used.")
        elif response.status_code == 422: raise WrongInputParams("Some data provided is invalid.")
        elif response.status_code == 429: raise TooMuchRequests("A request limit has been reached, usually this is due to the limit on the key being reached but can also be triggered by a global throttle.")
        elif response.status_code != 200 raise WrongInputParams("Undefined error.")
        return json.loads(response.content)
    
    def