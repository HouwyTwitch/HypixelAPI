import requests
from libs.exceptions import *
from libs.models import *
import json

def checkStatusCode(status_code: int, messages = ["Some data is missing, this is usually a field.",
                                                  "Access is forbidden, usually due to an invalid API key being used.",
                                                  "No data could be found for the requested player.",
                                                  "Some data provided is invalid.",
                                                  "A request limit has been reached, usually this is due to the limit on the key being reached but can also be triggered by a global throttle.",
                                                  "The data is not yet populated and should be available shortly.",
                                                  "Undefined error."]) -> None:
    if status_code == 400: raise WrongInputParams(messages[0])
    elif status_code == 403: raise WrongAPIKey(messages[1])
    elif status_code == 404: raise WrongInputParams(messages[2])
    elif status_code == 422: raise WrongInputParams(messages[3])
    elif status_code == 429: raise TooMuchRequests(messages[4])
    elif status_code == 503: raise DataIsNotPublic(messages[5])
    elif status_code != 200 raise WrongInputParams(messages[6])

class HypixelAPIScrapper():
    def __init__(self, apiKey: str) -> None:
        self.session: requests.session = requests.session()
        self.owner: str = ''
        if type(apiKey) == str: self.headers = {'API-Key': apiKey}
        else: raise WrongAPIKey("Wrong type of API key. API key should be 'str' type.")
        response: requests.Response = self.session.get(APIKeyInfo, headers = self.headers)
        checkStatusCode(response.status_code)
        self.owner = json.loads(response.content)['record']['owner']
    
    def getOwner(self) -> str:
        return self.owner
    
    def getPlayerData(self, uuid: str) -> dict:
        response: requests.Response = self.session.get(f'{Player}?uuid={uuid}', headers = self.headers)
        if response.status_code == 400: raise WrongInputParams("Some data is missing, this is usually a field.")
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getFriends(self, uuid: str) -> dict:
        response: requests.Response = self.session.get(f'{Friends}?uuid={uuid}', headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
        
    def getRecentGames(self, uuid: str) -> dict:
        response: requests.Response = self.session.get(f'{RecentGames}?uuid={uuid}', headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getStatus(self, uuid: str) -> dict:
        response: requests.Response = self.session.get(f'{Status}?uuid={uuid}', headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getGuild(self, id = None, player = None, name = None) -> dict:
        if id != None: response: requests.Response = self.session.get(f'{Guild}?id={id}', headers = self.headers)
        elif player != None: response: requests.Response = self.session.get(f'{Guild}?player={player}', headers = self.headers)
        elif name != None: response: requests.Response = self.session.get(f'{Guild}?name={name}', headers = self.headers)
        else: raise WrongInputParams("Some data is missing, this is usually a field.")
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getStatus(self, uuid: str) -> dict:
        response: requests.Response = self.session.get(f'{RankedSkywars}?uuid={uuid}', headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getResourcesGames(self) -> dict:
        response: requests.Response = self.session.get(ResourcesGames, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
        
    def getResourcesAchievements(self) -> dict:
        response: requests.Response = self.session.get(ResourcesAchievements, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getResourcesChallenges(self) -> dict:
        response: requests.Response = self.session.get(ResourcesChallenges, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getResourcesQuests(self) -> dict:
        response: requests.Response = self.session.get(ResourcesQuests, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getResourcesGuildsAchievements(self) -> dict:
        response: requests.Response = self.session.get(ResourcesGuildsAchievements, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
        
    def getResourcesVanityPets(self) -> dict:
        response: requests.Response = self.session.get(ResourcesVanityPets, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getResourcesVanityCompanions(self) -> dict:
        response: requests.Response = self.session.get(ResourcesVanityCompanions, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getResourcesSkyblockCollections(self) -> dict:
        response: requests.Response = self.session.get(ResourcesSkyblockCollections, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
        
    def getResourcesSkyblockSkills(self) -> dict:
        response: requests.Response = self.session.get(ResourcesSkyblockSkills, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getResourcesSkyblockItems(self) -> dict:
        response: requests.Response = self.session.get(ResourcesSkyblockItems, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getResourcesSkyblockElection(self) -> dict:
        response: requests.Response = self.session.get(ResourcesSkyblockElection, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getResourcesSkyblockBingo(self) -> dict:
        response: requests.Response = self.session.get(ResourcesSkyblockBingo, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getSkyblockNews(self) -> dict:
        response: requests.Response = self.session.get(SkyblockNews, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getSkyblockAuction(self, uuid = None, player = None, profile = None) -> dict:
        if uuid != None: response: requests.Response = self.session.get(f'{SkyblockNews}?id={uuid}', headers = self.headers)
        elif player != None: response: requests.Response = self.session.get(f'{SkyblockNews}?player={player}', headers = self.headers)
        elif profile != None: response: requests.Response = self.session.get(f'{SkyblockNews}?profile={profile}', headers = self.headers)
        else: raise WrongInputParams("Some data is missing, this is usually a field.")
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getSkyblockAuctions(self, page: int) -> dict:
        response: requests.Response = self.session.get(f'{Status}?page={page}', headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)
    
    def getSkyblockAuctionsEnded(self) -> dict:
        response: requests.Response = self.session.get(SkyblockAuctionsEnded, headers = self.headers)
        checkStatusCode(response.status_code)
        return json.loads(response.content)